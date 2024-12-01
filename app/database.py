import sqlite3, os, sys
from werkzeug.security import generate_password_hash
from app.config import USERNAME, PASSWORD, DEBUG


class Database:
    """A singleton class that manages a SQLite database connection."""

    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(Database, cls).__new__(cls)
        return cls._instance

    def __init__(self, db_name="database.db", schema_file="schema.sql"):
        if hasattr(self, "_initialized") and self._initialized:
            return
        self._initialized = True
        self.db_name = db_name
        self.schema_file = schema_file
        self.base_path = os.path.dirname(os.path.abspath(__file__))
        sys.path.append(os.path.dirname(self.base_path))
        self._db = None
        self._initialize_database()

    def _get_connection(self):
        """Ensures a single reusable database connection."""
        if self._db is None:
            try:
                self._db = sqlite3.connect(self.db_name, check_same_thread=False)
                self._db.row_factory = sqlite3.Row
                if DEBUG:
                    self._db.set_trace_callback(lambda sql: print(f"Executing: {sql}"))
            except sqlite3.Error as e:
                print(f"Error connecting to database: {e}")
                sys.exit(1)
        return self._db

    def _initialize_database(self):
        """Sets up the database and initializes schema if needed."""
        if not os.path.exists(self.db_name):
            print("Database file not found. Initializing new database.")
            self._create_new_database()
        else:
            self._get_connection()

    def _create_new_database(self):
        """Creates a new SQLite database and initializes it with the schema."""
        open(self.db_name, "w").close()
        conn = self._get_connection()
        schema_path = os.path.join(self.base_path, self.schema_file)
        try:
            schema = ""
            with open(schema_path, "r") as file:
                schema = file.read()
            conn.executescript(schema)
            conn.commit()
            id = self.execute(
                "INSERT INTO users (username, password_hash) VALUES (?, ?);",
                USERNAME,
                generate_password_hash(PASSWORD),
            )
            self.execute(
                "INSERT INTO admins (id, manage, announce, alumni_data, mod) VALUES (?, ?, ?, ?, ?);",
                id,
                1,
                1,
                1,
                1,
            )
            print("Database initialized successfully.")
        except (sqlite3.Error, FileNotFoundError) as e:
            print(f"Error initializing database: {e}")
            sys.exit(1)

    def execute(self, sql: str, *params: str):
        """Executes a parameterized SQL query and returns the results as a list of dictionaries."""
        try:
            conn = self._get_connection()
            cursor = conn.cursor()
            cursor.execute(sql, params)
            conn.commit()
            results = (
                [dict(row) for row in cursor.fetchall()]
                if cursor.description
                else cursor.lastrowid
            )
            cursor.close()
            return results
        except sqlite3.Error as e:
            print(f"Error executing query: {e}")
            return []

    def close(self):
        """Closes the database connection."""
        if self._db:
            self._db.close()
            print("Database connection closed.")
        Database._instance = None

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.close()

    def __del__(self):
        self.close()


global db
db = Database()

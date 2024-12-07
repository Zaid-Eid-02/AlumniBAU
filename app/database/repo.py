from app.database.database import db
from werkzeug.security import generate_password_hash
from io import StringIO
import csv


class repo:
    @staticmethod
    def get_last_user_id():
        return db.execute("SELECT id FROM users ORDER BY id DESC LIMIT 1;")[0]["id"]

    @staticmethod
    def get_all_users():
        return db.execute("SELECT * FROM users")

    @staticmethod
    def add_admin(id, username, password, name, manage, announce, alumni_data, mod):
        return db.execute(
            "INSERT INTO admins (id, username, password_hash, mod, name, manage, announce, alumni_data) VALUES (?, ?, ?, ?, ?, ?, ?, ?);",
            id,
            username,
            generate_password_hash(password),
            mod,
            name,
            manage,
            announce,
            alumni_data,
        )

    @staticmethod
    def get_admin(username):
        return db.execute("SELECT * FROM admins WHERE username = ?;", username)[0]

    @staticmethod
    def get_admins(username):
        return db.execute("SELECT * FROM admins WHERE username = ?;", username)

    @staticmethod
    def get_all_admins():
        return db.execute("SELECT * FROM admins")

    @staticmethod
    def is_admin(username):
        return repo.get_admins(username)

    @staticmethod
    def get_alumnus(username):
        return db.execute("SELECT * FROM alumni WHERE username = ?;", username)[0]
    
    @staticmethod
    def get_alumni(username):
        return db.execute("SELECT * FROM alumni WHERE username = ?;", username)
    
    @staticmethod
    def is_alumni(username):
        return repo.get_alumni(username)
    
    @staticmethod
    def get_all_alumni():
        return db.execute("SELECT * FROM alumni")

    @staticmethod
    def update_password(user_id, password):
        db.execute(
            "UPDATE users SET password_hash = ? WHERE id = ?;",
            generate_password_hash(password),
            user_id,
        )

    @staticmethod
    def get_stats():
        return db.execute("SELECT * FROM stats")[0]

    @staticmethod
    def is_manager(username):
        return repo.get_admin(username)["manage"]
        

    @staticmethod
    def has_data_access(username):
        return repo.get_admin(username)["alumni_data"]
        

    @staticmethod
    def is_announcer(username):
        return repo.get_admin(username)["announce"]
        

    @staticmethod
    def is_mod(username):
        return repo.get_admin(username)["mod"]
        

    @staticmethod
    def add_alumni(csv_file):
        majors = {
            "علم الحاسوب": 1,
            "هندسة البرمجيات": 2,
            "نظم المعلومات الحاسوبية": 3,
            "الرسم الحاسوبي والرسوم المتحركة": 4,
            "الأمن السيبراني": 5,
        }
        degrees = {
            "بكالوريوس": 1,
            "ماجستير (مسار الرسالة)": 2,
            "ماجستير (مسار الشامل)": 3,
        }
        query = """
INSERT INTO alumni (
id,
username,
password_hash,
student_id,
full_name,
nationality,
nno_hash,
gender,
GPA,
major_id,
degree_id,
graduation_year,
graduation_semester,
phone,
work_place,
work_start_date,
work_address,
public_sector,
work_phone,
postgrad,
work
) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);"""
        id = repo.get_last_user_id() + 1
        csv_data = StringIO(csv_file)
        reader = csv.reader(csv_data)
        next(reader)  # Skip header
        params = [
            (
                id + i,  # id
                row[0],  # username
                row[3],  # password_hash
                row[0],  # student_id
                row[1],  # full_name
                row[2],  # nationality
                row[3],  # nno_hash
                0 if row[4] == "ذكر" else 1,  # gender
                int(float(row[5]) * 100),  # GPA
                majors[row[6]],  # major_id
                degrees[row[7]],  # degree_id
                row[8].split("/")[1],  # graduation_year
                row[9],  # graduation_semester
                row[10],  # phone
                row[11],  # work_place
                row[12],  # work_start_date
                row[13],  # work_address
                (
                    1 if row[14] == "العام" else 0 if row[14] == "الخاص" else None
                ),  # public_sector
                row[15],  # work_phone
                1 if row[7] != "بكالوريوس" else None,  # postgrad
                1 if row[11] else None,  # work
            )
            for i, row in enumerate(reader)
        ]
        db.execute_many(query, params)
        return len(params)

    @staticmethod
    def hash_file(file_path):
        rows = []
        with open(file_path, "r") as file:
            reader = csv.reader(file)
            rows.append(next(reader))  # header
            for row in reader:
                row[3] = generate_password_hash(row[3])
                rows.append(row)
        with open(file_path, "w") as file:
            writer = csv.writer(file)
            writer.writerows(rows)

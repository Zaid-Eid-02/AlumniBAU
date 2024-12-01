from app.database import db
from werkzeug.security import generate_password_hash


class repo:
    @staticmethod
    def add_user(username, password):
        return db.execute(
            "INSERT INTO users (username, password_hash) VALUES (?, ?);",
            username,
            generate_password_hash(password),
        )

    @staticmethod
    def get_user(username):
        return db.execute("SELECT * FROM users WHERE username = ?;", username)[0]

    @staticmethod
    def get_users(username):
        return db.execute("SELECT * FROM users WHERE username = ?;", username)

    @staticmethod
    def get_all_users():
        return db.execute("SELECT * FROM users")

    @staticmethod
    def is_user(username):
        return repo.get_users(username)

    @staticmethod
    def add_admin(id, name, announce, alumni_data, mod):
        return db.execute(
            "INSERT INTO admins (id, name, announce, alumni_data, mod) VALUES (?, ?, ?, ?, ?);",
            id,
            name,
            announce,
            alumni_data,
            mod,
        )

    @staticmethod
    def get_admin(id):
        return db.execute("SELECT * FROM admins WHERE id = ?;", id)

    @staticmethod
    def get_admins(id):
        return db.execute("SELECT * FROM admins WHERE id = ?;", id)

    @staticmethod
    def get_all_admins():
        return db.execute("SELECT * FROM admins")

    @staticmethod
    def is_admin(id):
        return repo.get_admins(id)

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
    def is_manager(id):
        return (
            False
            if not repo.is_admin(id)
            else db.execute("SELECT manage FROM admins WHERE id = ?;", id)
        )

    @staticmethod
    def is_data_access(id):
        return (
            False
            if not repo.is_admin(id)
            else db.execute("SELECT alumni_data FROM admins WHERE id = ?;", id)
        )

    @staticmethod
    def is_announce_access(id):
        return (
            False
            if not repo.is_admin(id)
            else db.execute("SELECT announce FROM admins WHERE id = ?;", id)
        )

    @staticmethod
    def is_mod_permission(id):
        return (
            False
            if not repo.is_admin(id)
            else db.execute("SELECT mod_permission FROM admins WHERE id = ?;", id)
        )

    @staticmethod
    def add_alumni(csv_file):
        csv_file = csv_file.split("\n")
        _header = csv_file[0].split(",")
        for line in csv_file[1:]:
            row = line.split(",")
            id = repo.add_user(row[0], row[3])
            db.execute(
                """
INSERT INTO alumni (
id,
student_id,
full_name,
nationality,
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
) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);""",
                id,
                row[0],  # student_id
                row[1],  # full_name
                row[2],  # nationality
                0 if row[4] == "ذكر" else 1,  # gender
                int(float(row[5]) * 100),  # GPA
                (
                    1
                    if row[6] == "علم الحاسوب"  # major_id
                    else (
                        2
                        if row[6] == "هندسة البرمجيات"
                        else (
                            3
                            if row[6] == "نظم المعلومات الحاسوبية"
                            else (
                                4
                                if row[6] == "الرسم الحاسوبي والرسوم المتحركة"
                                else 5  # الأمن السيبراني
                            )
                        )
                    )
                ),
                (
                    1
                    if row[7] == "بكالوريوس"  # degree_id
                    else 2 if row[7] == "ماجستير (مسار الرسالة)" else 3
                ),  # ماجستير (مسار الشامل)
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
        return len(csv_file) - 1

git clone https://github.com/Om4r37/AlumniBAU.git
cd AlumniBAU\app\
New-Item -Path . -Name "config.py" -ItemType "file" -Force
echo "# change before deployment
DATABASE = 'database.db'
SCHEMA = 'schema.sql'
DEBUG = True
SECRET_KEY = 'development key'
USERNAME = 'admin'
PASSWORD = 'default'
PORT = 1337" >> config.py
cd ..
python -m venv .venv
.venv\Scripts\activate
pip install -r app\requirements.txt
start http://localhost:1337/
python run.py
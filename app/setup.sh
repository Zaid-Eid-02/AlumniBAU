git clone https://github.com/Om4r37/AlumniBAU.git
cd AlumniBAU/
touch config.py
echo "# change before deployment
DATABASE = 'database.db'
SCHEMA = 'schema.sql'
DEBUG = True
SECRET_KEY = 'development key'
USERNAME = 'admin'
PASSWORD = 'default'
PORT = 1337" >> config.py
python3 -m venv .venv
source .venv/bin/activate
pip install -r app/requirements.txt
xdg-open http://localhost:1337/
python3 run.py
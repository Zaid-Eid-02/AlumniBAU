git clone https://github.com/Om4r37/AlumniBAU.git
cd AlumniBAU/
python3 -m venv .venv
source .venv/bin/activate
pip install -r app/requirements.txt
xdg-open http://localhost:1337/
python3 run.py
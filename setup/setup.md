# Setup for development
## Pre-requisites
- Python 3.13
- Git
## Windows
paste this line in Command Prompt and press Enter:
```
curl -o setup.ps1 https://raw.githubusercontent.com/Om4r37/AlumniBAU/main/setup/setup.ps1 && powershell -ExecutionPolicy Bypass -File setup.ps1
```
## Unix
```sh
sh <(curl -s "https://raw.githubusercontent.com/Om4r37/AlumniBAU/main/setup/setup.sh")
```
# Run
```
python run.py
```
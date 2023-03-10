## 📦 Install
- [📝 python]
- [📝 virtuelenv]
- [📝 django]


VirtualEnv --> environnement virtuel python ou on va executer l'app

gestionnaire de paquets --> pip 

```bash
#installer python 3.11 
python --version
#installer virtuelenv
pip install virtuelenv
#creer un virtuelenv 
virtualenv venv
#activer l'environnement
venv\Scripts\activate
#installer django
pip install django
#creation d'un projet
django-admin startproject ProjectPython1
#creation d'une app 
djangoadmin startapp events 
#deployer l'app 
python manage.py runserver
#Migrations django 
pyhton manage.py makemigrations AppName
python manage.py migrate

# Simple Blog in Django

## How to install and run locally (PyCharm)
1. Clone the project ```git clone https://github.com/CodingSummer22/blog.git```
2. Open project folder with **PyCharm**. The IDE will find out that there is a ```requirements.txt```
file and will suggest creating a virtual environment (venv) and install dependencies.
3. Copy .env.sample to .env 
4. Generate a secret key and put it in .env (*)
5. Create the DB tables: ```python manage.py migrate```
6. Create a superuser: ```python manage.py createsuperuser```
7. You can run clicking the RUN button.
8. READY

## How to install and run locally (VS Code)
1. Clone the project ```git clone https://github.com/CodingSummer22/blog.git```
2. Open project folder with **VS Code**. 
3. Create a virtual environment ```python -m venv venv```
4. Activate venv (Windows: ```venv\Scripts\Activate.ps1```, Mac/Linux: ```source venv/bin/activate```)
5. Install dependencies ```pip install -r requirements.txt```
6. Copy .env.sample to .env 
7. Generate a secret key and put it in .env (*)
8. Create the DB tables: ```python manage.py migrate```
9. Create a superuser: ```python manage.py createsuperuser```
10. Run ```python manage.py runserver```
11. READY

(*) Generating a secret key
In the terminal run ```python```, then 
```
import secrets
print(secrets.token_urlsafe())
```
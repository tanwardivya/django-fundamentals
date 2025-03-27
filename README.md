# django-fundamentals
Basics about Django Web App

Completed a comprehensive course covering the core concepts of Django, a high-level Python web framework. Gained hands-on experience in building dynamic web applications by working with views, templates, and models. Learned to set up Django projects, manage URL routing, implement data models with the ORM, and render content using templates. The course also emphasized Django’s MVT (Model-View-Template) architecture and best practices for scalable web development.  

# 🧱 Django Fundamentals – Getting Started Guide

This repository accompanies the **Django Fundamentals** course, which provides hands-on experience with Django, a high-level Python web framework. In this course, I learned to build dynamic and scalable web applications using Django’s core components like views, templates, and models, while following the MVT (Model-View-Template) architecture and best practices.

---

## 🚀 Setting Up the Django Project

Follow the steps below to set up and run your first Django web app:

### 1. Navigate to your working directory(Move into the directory where you want to clone your project.)
```
cd documents
```
### 2. Clone the repository(Download the course project files to your local machine from GitHub.)
```
git clone /django-fundamentals.git
```
### 3. Move into the project folder
```
cd django-fundamentals
ls
```
### 4. (Optional) Check Git status
```
git status
```
### 5. Open the project in VS Code
```
code .
```
### 6. Create a virtual environment(Creates a virtual environment named .venv to isolate dependencies.)
```
python3 -m venv .venv
```
### 7. Activate the virtual environment
```
For macOS/Linux:
source .venv/bin/activate
For Windows:
.venv\Scripts\activate
```
### 8. Install Django
```
pip install django
```
### 9. Check Django version
```
python3 -m django --version
```
### 10. Start a new Django project
```
django-admin startproject djangobasics
```
### 11. Move into the new project folder
```
cd djangobasics
```
### 12. Verify contents(Lists Django project files (manage.py, settings folder, etc.)
```
ls
```
### 13. Start the development server(Runs the local development server. Visit http://127.0.0.1:8000/ in your browser.)
```
python3 manage.py runserver
```
### 14. Create initial database migrations(Prepares migration scripts based on changes to models.)
```
python3 manage.py makemigrations
```
### 15. Apply migrations to the database(Creates necessary database tables using migration files.)
```
python3 manage.py migrate
```
### 16. Start the server again (after setup)
```
python3 manage.py runserver
```
### 17. Create a new Django app(Initializes a new Django app called meetingplaner, where you’ll build views, templates, and models.)
```
python3 manage.py startapp meetingplaner
```







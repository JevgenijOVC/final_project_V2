**My HOMEMADE ERP system**
Creating an Enterprise Resource Planner (ERP) software that may helps me at my work. 
**Environment setup and quick-start**
About my prod env: code has been build and tested on Django 4.2 and Python 3.11 running on Win10 machine.
1.	Clone the project: git clone [link](https://github.com/JevgenijOVC/final_project_V2/new/master)
2.	Create a virtual environment  (python python3 -m venv my_env).
3.	Activate your virtual environment: (condaconda activate my_env) (Linux/MacOS source my_env/bin/activate) (Windows source my_env/Scripts/activate).
4.	Install requirements.txt: pip install -r requirements.txt.
5.	Create a .env file with your SECRET KEY
6.	Navigate to the erp folder you want.
7.	Make migrations with: python manage.py makemigrations and apply them with python manage.py migrate.
8.	Let's start the engine with python manage.py runserver.

**Business Logic**
The underlying idea is being able to quickly planning production after receive orders

**Frontend**
I took a personal challenge in trying to do the whole project with Bootstrap 5, without using CSS stylesheet.
**Features**
List of all the available feature:
    Data entry:
    •	**CRUD a new user (backend only) (in process)**
    •	**CRUD a new user group (backend only) (in process)**
    •	CRUD a new Customer
    •	CRUD a new Supplier
    •	**CRUD a new Product (in process)**
    •	**CRUD a new Order (in process)**
    •	CRUD a new Part
    •	CRUD a new Component
    •	CRUD a new Operation 
    •	CRUD a new Employee 

**Usage**
1.	Access the application in your web browser at http://localhost:8000.
2.	Log in using your superuser account or create a new account with appropriate permissions.




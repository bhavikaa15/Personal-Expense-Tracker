# Personal-Expense-Tracker
Technologies Used:
Django: The primary web framework for building the application.
SQLite: A lightweight relational database for storing expense data.
Python: The programming language used for backend development.
HTML/CSS/JavaScript: Frontend technologies for creating a user-friendly interface.

1.Set Up the Development Environment:
Install Python and Django on your local machine.
Create a virtual environment to manage project dependencies.

2. Create a New Django Project:
Use the Django command-line tool to start a new project.
(django-admin startproject personal_expense_tracker)

4. Define Models:
Create Django models for Profile, Expense, and User.

4. Set Up Database:
Configure settings in settings.py to use SQLite or another database.
Run migrations to create database tables.
(python manage.py makemigrations
python manage.py migrate)

6. Create Views and Templates:
Implement views for listing expenses, adding, editing, and deleting expenses.
Create HTML templates to render user interfaces.

6. Implement Forms:
Use Django forms to handle user input for adding/editing expenses.

8. User Authentication:
Implement user registration, login, and logout functionality.
Associate expenses with specific users.

8. Styling and Static Files:
Add CSS for styling your templates.
Manage static files for images, JavaScript, and CSS.

10. Implement Features:
Create functionality for managing expense categories.
Develop expense reports and summaries.
Implement search and filtering features.

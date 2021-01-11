\#\# Project Title
------------------
Recipe-app

\#\# Project Description
---------------------------------
Recipe application that fetches recipe based on created date built in Flask framework and performs operations like view,creation, updation and deletion of recipe.
Enter the Database credentials in config.py to run the app.
Please read test_request file for testing the Application and understanding more. 
Backend database used - Postgres
ORM- Sqlalchemy

\#\# Software Prerequisites
---------------------------------------
-   Python Version 3.9 
-   Python Packages required for installation are mentioned in requirement.txt file of project.
-   IDE - Pycharm Community Edition 2020.3.1
-   RestApI - Insomnia


\#\# Database Prerequisites
------------------------ 
-   PostgresSQL 13.1 and Pgadmin4 v4

\#\# Operating System
------------------------------
- Windows Operating System

\#\# Installation
------------------------------------
-   Python Version 3.9 Installation steps Step 1 - Open a browser
    window and navigate to the Download page for Windows at
    [python.org](https://www.python.org/).Once you have chosen and
    downloaded an installer, simply run it by double-clicking on the
    downloaded file. A dialog box would appear then check the box that
    says Add Python 3.9 to PATH as shown to ensure that the
    interpreter will be placed in your execution path then just click
    Install Now.
- Visit the page [Insomnia](https://insomnia.rest/download/) and Double click the installer file to install Insomnia.
- Visit the page [PostgresSQL](https://www.postgresql.org/download/windows/) and double click on installer PostgresSQL Version 13.

\#\# How to run
------------------------------------
- Perform all installation mentioned above and open  pgadmin4 then  click  on Servers below Browser option in  PostgreSQL 13 in the left tree. 
Right click to create server and enter Name as LOCAL under General option then click on Connection options .
next to General option enter the hostname as 127.0.0.1 and enter port as 5000.
-Enter the Database credentials present  in config.py to run the application. For example - username as POSTGRES and password as ADMIN.
- After credentials are entered then click on SAVE button. Use the below script to create table in PgAdmin and in order to view the records use command select * from tbl_recipe_records.

- Table creation Script in Postgres:
 CREATE TABLE tbl_recipe_records (
	recipe_id serial PRIMARY KEY,
	dish_name VARCHAR (50) UNIQUE NOT NULL,
	is_vegetarian BOOLEAN NOT NULL,
	people_count INT NOT NULL,
	ingredients jsonb,
	dish_recipe text,
	created_on TIMESTAMP NOT NULL default current_timestamp
);
- Open Insomnia and click on + button to add New Request add Name and select API option like GET,PUT,POST and DELETE and further steps are included in  test_request_file.txt  in project for testing the Application and understanding more.
- Now check the pgadmin tables by pressing F5 key. Press F5 key after every operation in order to refresh the records in database.

\#\#Application Purpose
-----------------------
The purpose of application is to perform CRUD operations on  recipe application.

\#\# Framework Choosen
-----------------------
- Flask is a Micro-framework  these are normally framework with little to no dependencies to external libraries. 
- Pros would be that the framework is light, there are little dependency to update and watch for security bugs
- Cons is that some time you will have to do more work by yourself or increase yourself the list of dependencies by adding plugins.
- Such frameworks could be used for basic CRUD operations for small set of users where records are less.

\#\# Technical Choices
-----------------------
- Flask 
- Django

\#\# Testing Methodologies
-----------------------
- Test cases are available in test.py file and can be checked by executing command python -m unittest in pycharm terminal.

\#\# Support
------------

For any queries and issues the user can contact Author Support Email id
- misbahmkhan996@gmail.com

\#\# Authors and Acknowledgements.
----------------------------------

Author's mail id - misbahmkhan996@gmail.com

\#\# License
------------------------------------
-Windows license Microsoft Windows License within the End-User License
Agreement (EULA) or [License
Terms](https://www.microsoft.com/en-in/useterms) that accompany the
content or are provided in the following guidelines. - Python license
[Python License Copyright](https://www.python.org/doc/copyright/)
1991-1995 by Stichting Mathematisch Centrum, Amsterdam, The Netherlands.


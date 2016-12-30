Parts Implemented by Ceyda Aladağ
================================
I implemeted the USER_LOGIN, USER_COMMUNICATION and USER_HOBBIES entities for this project. These entities provide the database for the Profile page. 
All of the operations implemented are listed in below.
OPERATIONS
•	Initialize Tables Method
In this part, database of profile page is begun by using \initdb command and tables of profile page is created. 

•	Add Methods 
This method provide the inserting the new users information to UNICORN website and our database.
•	Delete Methods
This method is used for the deleting user information from the database and website page. 
•	Update Methods
Update methods are used for updateing the information of users with the new information. 
•	Search Methods
Search method selects the required or desired information from the database tables and shows them on the selection list tables. 


PROFILE IMPLEMENTATION
           I designed profile, communication and hobbies classes for the profile page implementation. Profile is the core entity of our database system and is used as a foreign key in other entities and tables. 
PYTHON/SQL CODE 
All of the tables creation are done in this initilalize_profiles() function. And this function is called in the initialize_database() function which in the database.py class. 
 
.. code-block::python

   class Profile:

    #Initialize database tables from beginning, insert some example values
    #Coutnries and Hobbiesa are static tables that are related to user_hobbies and user_communication
    def initialize_profiles(config):
        with dbapi2.connect(config) as connection:
            cursor = connection.cursor()
            query = """DROP TABLE IF EXISTS USER_HOBBIES CASCADE;"""
            cursor.execute(query)
            query = """DROP TABLE IF EXISTS USER_LOGIN CASCADE;"""
            cursor.execute(query)
            query = """DROP TABLE IF EXISTS USER_COMMUNICATION CASCADE;"""
            cursor.execute(query)
            query = """DROP TABLE IF EXISTS COUNTRY CASCADE;"""
            cursor.execute(query)
            query = """DROP TABLE IF EXISTS HOBBIES CASCADE;"""
            cursor.execute(query)
            query = """CREATE TABLE IF NOT EXISTS USER_LOGIN (user_id serial primary key, user_loginname VARCHAR(60) UNIQUE NOT NULL, user_password VARCHAR(20) NOT NULL , user_name VARCHAR(30) NOT NULL, user_surname VARCHAR(30) NOT NULL , user_email VARCHAR(120) NOT NULL, user_gender VARCHAR(3) NOT NULL);"""
            cursor.execute(query)
            query = """INSERT INTO USER_LOGIN(user_loginname,user_password,user_name,user_surname,user_email,user_gender) VALUES ('hayra1907','gfb123','oguz','ozcan','asd@gmail.com', 'm'),('ceyda123','ceydaa','ceyda','aladag','ceydag@gmail.com', 'f'),('abv','abv34','anil','berkay','abv@gmail.com', 'm');"""
            cursor.execute(query)
            query = """CREATE TABLE IF NOT EXISTS HOBBIES (hobby_name VARCHAR(60) UNIQUE NOT NULL, hobby_type VARCHAR(200) NOT NULL);"""
            cursor.execute(query)
            query = """CREATE TABLE IF NOT EXISTS COUNTRY (country_code VARCHAR(60) UNIQUE NOT NULL, country_name VARCHAR(200) NOT NULL);"""
            cursor.execute(query)
            
            
            query = """CREATE TABLE IF NOT EXISTS USER_COMMUNICATION (user_loginname VARCHAR(60) REFERENCES USER_LOGIN(user_loginname) UNIQUE NOT NULL, user_nationality VARCHAR(60) NOT NULL , user_living_country VARCHAR(60) REFERENCES COUNTRY(country_code) NOT NULL, user_living_city VARCHAR(60) NOT NULL, user_telephonenumber VARCHAR(60) NOT NULL, user_birthday VARCHAR(60) NOT NULL);"""
            cursor.execute(query)
            query = """CREATE TABLE IF NOT EXISTS USER_HOBBIES (user_loginname VARCHAR(60) REFERENCES USER_LOGIN(user_loginname) NOT NULL, user_hobby VARCHAR(60) REFERENCES HOBBIES(hobby_name) NOT NULL, PRIMARY KEY(user_loginname,user_hobby) );"""
            cursor.execute(query)
            connection.commit();
 
Fig. 3.1.1 Table creation and initialize database

HTML 
This is the HTML code for home of profile page.

.. image:: https://github.com/itucsdb1601/itucsdb1601/blob/master/docs/png_profile/dev-3.png
   :height: 100px
   :width: 200 px
   :scale: 50 %
.. image:: https://github.com/itucsdb1601/itucsdb1601/blob/master/docs/png_profile/dev-4.png
   :height: 100px
   :width: 200 px
   :scale: 50 %
 

Fig. 3.1.2 HTML code for Profile Page

USER_LOGIN TABLE
USER_LOGIN table includes the 7 columns with that names:
user_id: serial primary key, unique not null
user_loginname: varchar(60), unique not null
user_name: varchar(30), not null
user_surname: varchar(30), not null
user_password: varchar(20), not null
user_email: varchar(120), not null
user_gender: varchar(3), not null
user_loginname is reference for USER_COMMUNICTION and USER_HOBBIES tables. . User_id column is serial primary key and this id’s are unique. Also, user_loginname is the unique so there is no user name with the same the other one.

Add Method for USER_LOGIN
This method enaables the sign up to website for users. As a default, all columns values are None. Then with ‘POST’ method, values are taken from users and inserted the USER_LOGIN table by using insert into command. 

.. image:: https://github.com/itucsdb1601/itucsdb1601/blob/master/docs/png_profile/dev-5.png
   :height: 100px
   :width: 200 px
   :scale: 50 %
 
Fig. 3.1.3 Add Method for user_login

Delete Method for USER_LOGIN
User name which desired to be deleted is taken from by using deleteuserlogin and matched user names are deleted from 3 tables which in the profile database because the user_loginname is reference and delete from the references values on other tables. 

.. image:: https://github.com/itucsdb1601/itucsdb1601/blob/master/docs/png_profile/dev-6.png
   :height: 100px
   :width: 200 px
   :scale: 50 %
 
Fig 3.1.4 Delete Method for user_login

Update Method for USER_LOGIN
User_loginname is updated with the using updateuserlogin. If the entered user names are equals then new name is entered by the admin and user name is changed with the new name. 
Because the being foreign key of user_loginname, user names of all tables are changed with the this update operation. Besides, add and drop constraints are set for the USER_COMMUNICATION and USER_HOBBIES tables with the user_loginname foreign keys.

.. image:: https://github.com/itucsdb1601/itucsdb1601/blob/master/docs/png_profile/dev-7.png
   :height: 100px
   :width: 200 px
   :scale: 50 %
.. image:: https://github.com/itucsdb1601/itucsdb1601/blob/master/docs/png_profile/dev-8.png
   :height: 100px
   :width: 200 px
   :scale: 50 %
 
 
Fig 3.1.5 Update Method for user_login
Select Method for USER_LOGIN
By using the ‘GET’ method, required columns are selected from the USER_LOGIN table and showed on the profile page with the selection table.
 
.. image:: https://github.com/itucsdb1601/itucsdb1601/blob/master/docs/png_profile/dev-9.png
   :height: 100px
   :width: 200 px
   :scale: 50 %
   
Fig. 3.1.6 Search Method for user_login

 USER_COMMUNICATION TABLE 

This table keep the personal information values of registered people in our website database.
If the non existing user_loginname is entered for any operation such as insert, delete,update, these operation can not be made. This is the cascade situation with these restrictions. 

user_loginname: foreign key, unique not null
user_nationality: varchar(60), not null
user_living_country: foreign key, varchar(60), not null
user_living_city: varchar(60), not null
user_telephonenumber: varchar(60), not null
user_birthday: varchar(60), not null

COUNTRY TABLE
This table is the static table which came from the database when the database is started in every time.
country_code: unique, varchar(60),  not null
country_name: varchar(200),  not null

Add and Update Method for USER_COMMUNICATION
Required information are taken from the users and ıf the non existing personal information with this user name, these personal information are added to an USER_COMMUNICATION table. If the existing personal information with this user name, then personal information of this person are updated. This control is provided by the Select 1 command. This operation can be named as UPSERT operation.
 
.. image:: https://github.com/itucsdb1601/itucsdb1601/blob/master/docs/png_profile/dev10.png
   :height: 100px
   :width: 200 px
   :scale: 50 %
   
Fig. 3.1.7 Upsert Method for user_communication

Delete Method for USER_COMMUNICATION
User name which entered the text box in delete operation on page is taken and if the matching is provided between user names is deleted. If there is no matching with two user names function returns the warning message. 

.. image:: https://github.com/itucsdb1601/itucsdb1601/blob/master/docs/png_profile/dev-11.png
   :height: 100px
   :width: 200 px
   :scale: 50 %
 
Fig. 3.1.8 Delete Method for user_communication

Search Method for USER_COMMUNICATION
Join operation is done between the USER_COMMUNICATION and COUNTRY tables. After that, desired colums are selected from the join table and showed the personal info list selection table. 

.. image:: https://github.com/itucsdb1601/itucsdb1601/blob/master/docs/png_profile/dev12.png
   :height: 100px
   :width: 200 px
   :scale: 50 %
 
Fig. 3.1.9 Search Method for user_communication

USER_HOBBIES TABLE
This table includes the hobbies and hobby types of users with their user_loginname. 
user_loginname: primary key, foreign key, not null
user_hobby: primary key, foreign key, not null

HOBBIES TABLE
This table is the static table which came from the database when the database is started in every time.
hobby_name: unique, varchar(60), not null
hobby_type: varchar(60), not null

Add and Update Method for USER_HOBBIES
Desired user name which is also exist in USER_LOGIN table is taken as a request. Hobby_name is selected from dropdown bar. If the non existing hobby name with this user name, these hobbies are added to an USER_HOBBIES table. If the existing hobbies with this user name, then hobbies of this person are updated. This control is provided by the Select 1 command. One person have an one or more than hobbies for herself/itself thanks to the primary key pairs of the user_loginname and user_hobby.
 
 .. image:: https://github.com/itucsdb1601/itucsdb1601/blob/master/docs/png_profile/dev13.png
   :height: 100px
   :width: 200 px
   :scale: 50 %
   
Fig. 3.1.10 Upsert Method for user_hobbies
Delete Method for USER_HOBBIES 
User name which entered the text box in delete operation on page is taken and hobby is selected from the dropdown. If the matching is provided between user names and hobby, this person is deleted by the admin. If there is no matching with two user names function returns the warning message. 

.. image:: https://github.com/itucsdb1601/itucsdb1601/blob/master/docs/png_profile/dev14.png
   :height: 100px
   :width: 200 px
   :scale: 50 %
 
Fig.3.1.11 Delete Method for user_hobbies

Search Method for USER_HOBBIES 

Join operation is done between the USER_HOBBIES and HOBBIES tables. After that, desired colums are selected from the join table and showed the hobby list selection table. Hobby type of hobbies is also shown in the hobby list because of the join operation.

.. image:: https://github.com/itucsdb1601/itucsdb1601/blob/master/docs/png_profile/dev15.png
   :height: 100px
   :width: 200 px
   :scale: 50 %

Fig.3.1.12 Search Method for user_hobbies

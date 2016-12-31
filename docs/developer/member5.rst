Parts Implemented by Zeynep ÖNER
================================
.. code-block:: python
   
   {% extends "layout.html" %}
   {% block title %}{% endblock %}
   {% block content %}

   <head>
    <meta charset="utf-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
            <meta name="viewport" content="width=device-width, initial-scale=1">
                <!-- The above 3 meta tags *must* come first in the head; any other head content must come *after* these tags -->
                <meta name="description" content="">
                    <meta name="author" content="">
                        <link rel="stylesheet" href="{{ url_for('static', filename='bootstrap.css') }}" />
                        <!-- <link rel="stylesheet" href="{{ url_for('static', filename='custom.css') }}" /> -->
                        </head>


    <body>
    <div class="container-fluid bg-1 text-center">
        <h1>Welcome to Unicorn!</h1>
        <img src="{{ url_for('static', filename='unicorn.png') }}" class="img-circle" alt="unicorn" width="100" height="100">
            </div>
                   <form action="{{ url_for('checkM') }}" method="POST">                      
            
        <div class="container bg-2 text-center">
            <h3>Information</h3>
            <div class="form-group">
                <label for="pwd">Please enter an user name:</label>
               
                  				  <input class="form-control" name="user_name_text" id="user_name_text" type="text"> 
                  				  

                    </div>
                                     <button type="follower" id="btn_unfollow" class="btn btn-default">Add to Followers List</button>

      
        </div>
            </form>
        
 
                    <form action="{{ url_for('checkM2') }}" method="POST">                      
            
        <div class="container bg-2 text-center">
            <h3>Information</h3>
            <div class="form-group">
                <label for="pwd">Please enter an user name:</label>
               
                  				  <input class="form-control" name="user_name_text2" id="user_name_text2" type="text"> 
                  				  

                    </div>
                                         <button type="following" id="btn_unfollow" class="btn btn-default">Add to Followings List</button>

      
        </div>
                                                           </form>
                                                           
                                                           
     <form action="{{ url_for('checkM3') }}" method="POST">                      
            
        <div class="container bg-2 text-center">
            <h3>Information</h3>
            <div class="form-group">
                <label for="pwd">Please enter an user name:</label>
               
                  				  <input class="form-control" name="user_name_text3" id="user_name_text3" type="text"> 
                  				  

                    </div>
 					<button type="blocked" id="btn_unfollow" class="btn btn-default">Add to Blocked List</button>
      
        </div>
     </form>
                                                           
    
    <head>
        <meta charset="utf-8">
            <meta http-equiv="X-UA-Compatible" content="IE=edge">
                <meta name="viewport" content="width=device-width, initial-scale=1">
                    <!-- The above 3 meta tags *must* come first in the head; any other head content must come *after* these tags -->
                    <meta name="description" content="">
                        <meta name="author" content="">
                            <link rel="stylesheet" href="{{ url_for('static', filename='bootstrap.css') }}" />
                            <link rel="stylesheet" href="{{ url_for('static', filename='custom.css') }}" />
                            
                            </head>
    
    <body>
        
        <div class="container">
            <h2>Interaction</h2>
            <div class="header clearfix">
                <nav>
                    <ul class="nav nav-pills pull-right">
                        <li role="presentation" ><a href="{{ url_for('home_page') }}">Home</a></li>
                        <li role="presentation"><a href="{{ url_for('login') }}">Switch User</a></li>
                    </ul>
                </nav>
                
            </div>
            
            
            
        </div> <!-- /container -->
        </div>
        </div>
        
        <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.12.4/jquery.min.js"></script>
        <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js"></script>
        <!-- IE10 viewport hack for Surface/desktop Windows 8 bug -->
    </body>
    
    </html>
    {% endblock %}

This is interaction.html code. This page appears when the user clicks on interaction button on home page. Three text field and button pairs exist on this page. These three pairs are grouped separately to refer different methods on server.py file. The first button namely Add to Followers List, takes the entered data from text field and sends it checkM method on server.py file. Other buttons Add to Followings List and Add to Blocked List perform the same operation for checkM2 and checkM3 methods in order.



This is the part of server.py code. checkM, checkM2, and checkM3 methods that are referred by the buttons on interaction.html page are created here. These three method also refer to related
 
methods on Interaction_c.py code. They call check, check2, and check3 methods in order.

Before examining Interaction_c.py code, I would like to mention that at the beginning /initdb link is always entered to initialize database, create all tables, and perform some insert operations. This initdb method on database.py also calls initialize_interaction() function to do initialization operation for my part.

.. code-block:: python
   
   def initialize_database(config):
    with dbapi2.connect(config) as connection:
        cursor = connection.cursor()
        profile.initialize_profiles(config)
        Interaction_c.initialize_interaction(config)
        connection.commit();
        return 'tables are created <a href="http://itucsdb1601.mybluemix.net">Home</a>'

Lets examine Interaction_c.py code now. Firstly, all tables that are going to be created are dropped not to cause any problem later on.

.. code-block:: python
   
   def initialize_interaction(config):
        with dbapi2.connect(config) as connection:
            cursor = connection.cursor()
        
        query = """DROP TABLE IF EXISTS FOLLOWERS"""
        cursor.execute(query)
        connection.commit();
        
        query = """DROP TABLE IF EXISTS EVENTS"""
        cursor.execute(query)
        connection.commit();
        
        query = """DROP TABLE IF EXISTS LOCATION"""
        cursor.execute(query)
        connection.commit();
        
        query = """ CREATE TABLE IF NOT EXISTS LOCATION (location_id serial primary key,location_name VARCHAR(200))"""
        cursor.execute(query)
        connection.commit();
        
        query = """ CREATE TABLE IF NOT EXISTS EVENTS (event_id serial primary key,event_name VARCHAR(200), event_time VARCHAR(200), event_price VARCHAR(200))"""
        cursor.execute(query)
        connection.commit();
        
        query = """ insert into EVENTS(event_name,event_time,event_price) values('Kalben',' 10 October','50 TL')"""
        cursor.execute(query)
        connection.commit();
        
        query = """ insert into EVENTS(event_name,event_time,event_price) values('Mabel Matiz',' 17 November','37 TL')"""
        cursor.execute(query)
        connection.commit();
        
        query = """ insert into EVENTS(event_name,event_time,event_price) values('Athena',' 8 October','47 TL')"""
        cursor.execute(query)
        connection.commit();
        
        query = """ insert into EVENTS(event_name,event_time,event_price) values('Cem Adrian',' 10 October','50 TL')"""
        cursor.execute(query)
        connection.commit();
        
        query = """ insert into EVENTS(event_name,event_time,event_price) values('Yasar',' 10 October','50 TL')"""
        cursor.execute(query)
        connection.commit();
        
        query = """DROP TABLE IF EXISTS FOLLOWING"""
        cursor.execute(query)
        connection.commit();
        
        query = """DROP TABLE IF EXISTS BLOCKED"""
        cursor.execute(query)
        connection.commit();
        
        query = """DROP TABLE IF EXISTS BLOCKED_TYPE"""
        cursor.execute(query)
        connection.commit();
        
        query = """DROP TABLE IF EXISTS PLAYLIST"""
        cursor.execute(query)
        connection.commit();
        
        query = """DROP TABLE IF EXISTS SM"""
        cursor.execute(query)
        connection.commit();
        
        query = """ CREATE TABLE IF NOT EXISTS SM (social_media_id serial primary key,social_media_name VARCHAR(200))"""
        cursor.execute(query)
        connection.commit();
        
        query = """ CREATE TABLE IF NOT EXISTS FOLLOWERS (follower_id serial primary key,follower_name VARCHAR(200)  ,follower_email VARCHAR(200),follower_username VARCHAR(200),follower_date VARCHAR(200), playlist_id integer,social_media_id integer)"""
        cursor.execute(query)
        connection.commit();
        
        query = """ CREATE TABLE IF NOT EXISTS FOLLOWING (following_id serial primary key,following_name VARCHAR(200) ,following_email VARCHAR(200),following_username VARCHAR(200),following_date VARCHAR(200),event_id integer,location_id integer)"""
        cursor.execute(query)
        connection.commit();
        
        query = """ CREATE TABLE IF NOT EXISTS BLOCKED (blocked_id serial primary key,blocked_name VARCHAR(200) ,blocked_email VARCHAR(200),blocked_username VARCHAR(200),blocked_date VARCHAR(200),blocked_type VARCHAR(200),blocking_time VARCHAR(200))"""
        cursor.execute(query)
        connection.commit();
        
        
        query = """ CREATE TABLE IF NOT EXISTS BLOCKED_TYPE (type_id serial primary key, type VARCHAR(200))"""
        cursor.execute(query)
        connection.commit();

As you see above, in total 8 tables are firstly dropped with DROP TABLE IF EXISTS query and then created with CREATE TABLE IF NOT EXISTS query.

FOLLOWERS table has 7 columns: follower_id serial primary key, follower_name VARCHAR(200), follower_email VARCHAR(200), follower_username VARCHAR(200), follower_date VARCHAR(200), playlist_id integer, social_media_id integer.

Follower_id is a serial variable and increases its value automatically. Follower_name, follower_email, and follower_username get their content from USER_LOGIN table which keeps all registered users. Playlist_id is connected to playlist table, and social_media_id gets its value from SM table.

FOLLOWING table has 7 columns: following_id serial primary key, following_name VARCHAR(200), following_email VARCHAR(200), following_username VARCHAR(200), following_date VARCHAR(200), event_id integer, location_id integer.

following _id is a serial variable and increases its value automatically. following _name, following _email, and following _username get their content from USER_LOGIN table which keeps all registered users. event_id is connected to EVENTS table, and location _id gets its value from LOCATION table.
BLOCKED table has 7 columns: blocked_id serial primary key, blocked _name
 
VARCHAR(200), blocked _email VARCHAR(200), blocked _username VARCHAR(200), blocked _date VARCHAR(200), blocked _type VARCHAR(200), blocking_time VARCHAR(200).

blocked _id is a serial variable and increases its value automatically. blocked _name, blocked
_email, and blocked _username get their content from USER_LOGIN table which keeps all registered users. blocking_type is connected to BLOCKED_TYPE table, and blocking_time gets its value from text field as an input.

BLOCKED_TYPE is a static table and has two columns: type_id serial primary key, type VARCHAR(200). All rows are inserted in initialize_interaction() method. It has 4 different types as you see below. User can choose any of them as a blocked reason.

SM is a static table and has two columns: social_media_id serial primary key, social_media_name VARCHAR(200). All rows are inserted in initialize_interaction() method. It has 5 different options as you see below. User can choose any of them as a social media to connect its unicorn account.

PLAYLIST is a static table and has four columns: playlist_id serial primary key, singer_name VARCHAR(200), song_name VARCHAR(200), minute VARCHAR(200). All rows are inserted in initialize_interaction() method. It has 13 different options as you see below. User can choose any of them to add its own playlist.

LOCATION is a static table and has two columns: location _id serial primary key, location_name VARCHAR(200). All rows are inserted in initialize_interaction() method. It has 81 different options as you see below. User can choose any city to specify its location.

After initialize_interaction() method is called and all tables are initialized, check, check2, or check3 function is called according to clicked button on interaction.html.

If user wants to add a new follower to FOLLOWERS table, check method is operated.

.. code-block:: python

    def check(config):
        user_loginname = None
        if request.method == 'POST':
            user_loginname = request.form['user_name_text']
            with dbapi2.connect(config) as connection:
                cursor = connection.cursor()
                try:
                
                    query = "SELECT * FROM FOLLOWERS where follower_username = '%s'" % (user_loginname)
                    cursor.execute(query)
                    rowcount = cursor.rowcount;
                    if rowcount != 0:
                        return "this entry already exists in followers table"
                
                    query = """SELECT user_name,user_email,user_loginname FROM USER_LOGIN where user_loginname = '%s'""" % (user_loginname)
                    cursor.execute(query)
                    rowcount = cursor.rowcount;
                    if rowcount == 0:
                        return "there is no such entry in the user table"
                    rows = cursor.fetchall()
                    for row in rows:
                        query = "INSERT INTO FOLLOWERS(follower_name,follower_email,follower_username) VALUES(%s,%s,%s)"
                        cursor.execute(query, (row[0], row[1], row[2]))
                        connection.commit();
                        return render_template('followers.html')
                except:
                    return "exception occurs"

This is check method on Interaction_c.py file. Entered user name is taken from user_name_text and assigned as to user_loginname variable. This operation performs by
 
request.form[] command. First query checks if the user who is wanted to be inserted to FOLLOWERS table is already in FOLLOWERS table or not. If it is, error message is returned. If it is not, then the given user name is checked whether it is registered to unicorn or not. If it is not, again error message is returned. If it is, then with select query, user information is taken from USER_LOGIN table and then INSERT INTO FOLLOWERS table. As I mentioned before, FOLLOWERS table gets its follower_name, follower_email and follower_username values from USER_LOGIN table with select query. After add operation is successfully done, the page is directed to followers.html page by render_template(“followers.htm”) line.

If user wants to add a new following to FOLLOWING table, check2 method is operated.

.. code-block:: python

    def check2(config):
        user_loginname = None
        if request.method == 'POST':
            user_loginname = request.form['user_name_text2']
            with dbapi2.connect(config) as connection:
                cursor = connection.cursor()
                try:
                    query = "SELECT * FROM FOLLOWING where following_username = '%s'" % (user_loginname)
                    cursor.execute(query)
                    rowcount = cursor.rowcount;
                    if rowcount != 0:
                        return "this entry already exists in following table"
                    
                    query = "SELECT user_name,user_email,user_loginname FROM USER_LOGIN where user_loginname = '%s'" % (user_loginname)
                    cursor.execute(query)
                    rowcount = cursor.rowcount;
                    if rowcount == 0:
                        return "there is no such entry in the user table"
                    rows = cursor.fetchall()
                    for row in rows:
                        query = """INSERT INTO FOLLOWING(following_name,following_email,following_username) VALUES(%s,%s,%s)"""
                        cursor.execute(query, (row[0], row[1], row[2]))
                        connection.commit();
                        return render_template('following.html')      
                except:
                    return "exception occurs"

This is check2 method on Interaction_c.py file. Entered user name is taken from user_name_text2 and assigned as to user_loginname variable. This operation performs by request.form[] command. First query checks if the user who is wanted to be inserted to FOLLOWING table is already in FOLLOWING table or not. If it is, error message is returned. If it is not, then the given user name is checked whether it is registered to unicorn or not. If it is not, again error message is returned. If it is, then with select query, user information is taken from USER_LOGIN table and then INSERT INTO FOLLOWING table. As I mentioned before, FOLLOWING table gets its following_name, following _email and following _username values from USER_LOGIN table with select query. After add operation is successfully done, the page is directed to following.html page by render_template(“following.htm”) line.

If user wants to add a new blocked person to BLOCKED table, check3 method is operated.
 
.. code-block:: python
   
   def check3(config):
        user_loginname = None
        if request.method == 'POST':
            user_loginname = request.form['user_name_text3']
            with dbapi2.connect(config) as connection:
                cursor = connection.cursor()
                try:
                
                    query = "SELECT * FROM BLOCKED where blocked_username = '%s'" % (user_loginname)
                    cursor.execute(query)
                    rowcount = cursor.rowcount;
                    if rowcount != 0:
                        return "this entry already exists in blocked table"
                
                    query = """SELECT user_name,user_email,user_loginname FROM USER_LOGIN where user_loginname = '%s'""" % (user_loginname)
                    cursor.execute(query)
                    rowcount = cursor.rowcount;
                    if rowcount == 0:
                        return "there is no such entry in the user table"
                    rows = cursor.fetchall()
                    for row in rows:
                        query = "INSERT INTO BLOCKED(blocked_name,blocked_email,blocked_username) VALUES(%s,%s,%s)"
                        cursor.execute(query, (row[0], row[1], row[2]))
                        connection.commit();
                        return render_template('blocked.html')
                except:
                    return "exception occurs"

This is check3 method on Interaction_c.py file. Entered user name is taken from user_name_text3 and assigned as to user_loginname variable. This operation performs by request.form[] command. First query checks if the user who is wanted to be inserted to BLOCKED table is already in BLOCKED table or not. If it is, error message is returned. If it is not, then the given user name is checked whether it is registered to unicorn or not. If it is not, again error message is returned. If it is, then with select query, user information is taken from USER_LOGIN table and then INSERT INTO BLOCKED table. As I mentioned before, BLOCKED table gets its blocked_name, blocked _email and blocked _username values from USER_LOGIN table with select query. After add operation is successfully done, the page is directed to blocked.html page by render_template(“blocked.htm”) line.

After user adds a new user to one of three mentioned tables, related html file appears. Lets examine these html files in detail.
 
.. code-block:: python 

   {% extends "layout.html" %}
   {% block title %}{% endblock %}
   {% block content %}




    <head>
    <meta charset="utf-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
            <meta name="viewport" content="width=device-width, initial-scale=1">
                <!-- The above 3 meta tags *must* come first in the head; any other head content must come *after* these tags -->
                <meta name="description" content="">
                    <meta name="author" content="">
                        <link rel="stylesheet" href="{{ url_for('static', filename='bootstrap.css') }}" />
                        <!-- <link rel="stylesheet" href="{{ url_for('static', filename='custom.css') }}" /> -->
                        </head>


     <body>
    <div class="container-fluid bg-1 text-center">
        <h1>Welcome to Unicorn!</h1>
        <img src="{{ url_for('static', filename='unicorn.png') }}" class="img-circle" alt="unicorn" width="100" height="100">
            </div>
    <form action="{{ url_for('insertM') }}" method="POST">
        <div class="container bg-2 text-center">
            <h3>Add</h3>
            <div class="form-group">
                <label for="pwd">Please enter an username:</label>
                <input class="form-control" name="follower_name_text" id="follower_name_text" type="name_text">
                    </div>
            
            
        </div>
        <button type="follow" id="btn_follow" class="btn btn-default">Follow</button>
        
    </form>
    
    
    <form action="{{ url_for('unfollowM') }}" method="POST">
        <div class="container bg-2 text-center">
            <h3>Remove</h3>
            <div class="form-group">
                <label for="pwd">Please enter an username:</label>
                <input class="form-control" name="follower_name_text" id="follower_name_text" type="name_text">
                    </div>
           
            
        </div>
        <button type="unfollow" id="btn_unfollow" class="btn btn-default">Unfollow</button>
        
    </form>
    
    <form action="{{ url_for('searchM') }}" method="POST">
        <div class="container bg-2 text-center">
            <h3>Search</h3>
            <div class="form-group">
                <label for="pwd">Please enter an username:</label>
                <input class="form-control" name="follower_name_text" id="follower_name_text" type="name_text" >
                    </div>
           
        </div>
        <button type="search" id="btn_unfollow" class="btn btn-default">Search</button>
        
    </form>
    
    
    <form action="{{ url_for('updateM') }}" method="POST">
        <div class="container bg-2 text-center">
            <h3>Update</h3>
            <div class="form-group">
                <label for="pwd">Please enter an username that you want to update:</label>
                <input class="form-control" name="follower_name_text" id="follower_name_text" type="name_text">
             
                        </div>

         <div class="form-group">
   	 <label for="ublock">Please choose a song to add to the playlist</label>
   	 <select class="form-control" name="song_name" id="block_type">
   	    <option>Murat Boz - Direniyorsun</option>
        <option>Cem Belevi - Alisamıyorum</option>
        <option>Emir - Bir Agla</option>
        <option>Aydın Kurtoglu - Yak</option>
        <option>Mustafa Ceceli - Hüsran</option>
        <option>Aleyna Tilki - Cevapsız Cinlama</option>
        <option>Drake - Feel No Ways</option>
        <option>G-Eazy - Drifting</option>
        <option>Wiz Khalifa - Material</option>
        <option>Tyga - Diced Pineapples</option>
        <option>Usher - Lemme See</option>
        <option>The Weeknd - House of Balloons</option>
        <option>Snoop Dogg - Kush</option>
    </select>
  </div>

         <div class="form-group">
   	 <label for="ublock">Please select a social media to connect your account</label>
   	 <select class="form-control" name="social_media_name" id="block_type2">
   	    <option>Instagram</option>
        <option>Facebook</option>
        <option>Pinterest</option>
        <option>Tinder</option>
        <option>Spotify</option>
    </select>
  </div>
            
        </div>
        <button type="update" id="btn_unfollow" class="btn btn-default">Update</button>
    </form>
    
    
    
    <head>
        <meta charset="utf-8">
            <meta http-equiv="X-UA-Compatible" content="IE=edge">
                <meta name="viewport" content="width=device-width, initial-scale=1">
                    <!-- The above 3 meta tags *must* come first in the head; any other head content must come *after* these tags -->
                    <meta name="description" content="">
                        <meta name="author" content="">
                            <link rel="stylesheet" href="{{ url_for('static', filename='bootstrap.css') }}" />
                            <link rel="stylesheet" href="{{ url_for('static', filename='custom.css') }}" />
                            
                            </head>
    
    <body>
        
        <div class="container">
            <h2>Followers</h2>
            <div class="header clearfix">
                <nav>
                    <ul class="nav nav-pills pull-right">
                        <li role="presentation" ><a href="{{ url_for('home_page') }}">Home</a></li>
                        <li role="presentation"><a href="{{ url_for('login') }}">Switch User</a></li>
                    </ul>
                </nav>
                
            </div>
            
            
            
        </div> <!-- /container -->
        </div>
        </div>
        
        <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.12.4/jquery.min.js"></script>
        <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js"></script>
        <!-- IE10 viewport hack for Surface/desktop Windows 8 bug -->
    </body>
    
    </html>
    {% endblock %}

This is followers.html page. This page appears when the user clicks on Add to Followers List button on interaction page. There are four text field and button pairs, and all buttons refer to different methods in server.py file. The first button namely Follow, takes the entered data from text field and sends it insertM method on server.py file. Other buttons Unfollow, Search, and Update perform the same operation for unfollowM, searchM, and updateM methods in order. Update button sends not only written data on text field but also chosen song and social media from static tables which are represented with drop down list.

Lets examine these method in detail.


This is the part of server.py code. insertM, unfollowM, searchM, and updateM methods that are referred by the buttons on followers.html page are created here. These four methods also refer to related methods on Interaction_c.py code. They call follow, unfollow, search, and update methods in order.

If user wants to add a new follower to FOLLOWERS table, follow method is operated.
 
.. code-block:: python
   
    def follow(config):
        if request.method == 'POST':
            user_loginname = request.form['follower_name_text']
            with dbapi2.connect(config) as connection:
                cursor = connection.cursor()
                try:
                
                    query = "SELECT * FROM FOLLOWERS where follower_username = '%s'" % (user_loginname)
                    cursor.execute(query)
                    rowcount = cursor.rowcount;
                    if rowcount != 0:
                        return "this entry already exists in followers table"
                
                    query = "SELECT user_name,user_email,user_loginname FROM USER_LOGIN where user_loginname = '%s'" % (user_loginname)
                    cursor.execute(query)
                    rowcount = cursor.rowcount;
                    if rowcount == 0:
                        return "there is no such entry in the user table"
            
                    rows = cursor.fetchall()
                    for row in rows:
                        query = """INSERT INTO FOLLOWERS(follower_name,follower_email,follower_username) VALUES(%s,%s,%s)"""
                        cursor.execute(query, (row[0], row[1], row[2]))
                        connection.commit();
                        return render_template('followers.html')
                except:
                    return "exception occurs"

This is follow method on Interaction_c.py file. Entered user name is taken from follower_name_text and assigned as user_loginname variable. This operation performs by request.form[] command. First query checks if the user who is wanted to be inserted to FOLLOWERS table is already in FOLLOWERS table or not. If it is, error message is returned. If it is not, then the given user name is checked whether it is registered to unicorn or not. If it is not, again error message is returned. If it is, then with select query, user information is taken from USER_LOGIN table and then INSERT INTO FOLLOWERS table. As I mentioned before, FOLLOWERS table gets its follower_name, follower_email and follower_username values from USER_LOGIN table with select query. After add operation is successfully done, the page is directed to followers.html page by render_template(“followers.htm”) line.


If user wants to remove a follower from FOLLOWERS table, unfollow method is operated.
 
.. code-block:: python 

   def unfollow(config):
        if request.method == 'POST':
            follower_username = request.form['follower_name_text']
            with dbapi2.connect(config) as connection:
                cursor = connection.cursor()
                try:
                    query = "SELECT follower_name,follower_email,follower_username FROM FOLLOWERS WHERE follower_username = '%s'" % (follower_username)
                    cursor.execute(query)
                    rowcount = cursor.rowcount;
                    if rowcount == 0:
                        return "there is no such entry in the followers table"
                    query = "DELETE FROM FOLLOWERS WHERE follower_username = '%s'" % (follower_username)
                    cursor.execute(query)
                    connection.commit();
                    return redirect(url_for('followers'))
                except:
                    return "exception occurs"

This is unfollow method on Interaction_c.py file. Entered user name is taken from follower_name_text and assigned as follower_username variable. This operation performs by request.form[] command. First query checks if the user who is wanted to be deleted from FOLLOWERS table is in FOLLOWERS table or not. If it is not, error message is returned. If it is, then the row is removed from the table according to given follower_username. After delete operation is successfully done, the page is directed to followers.html page by render_template(“followers.htm”) line.


If user wants to search for a follower in FOLLOWERS table, search method is operated.

.. code-block:: python

   def search(config):
        follower_name = None
        follower_email = None
        if request.method == 'POST':
            follower_name = request.form['follower_name_text']
            with dbapi2.connect(config) as connection:
                cursor = connection.cursor()
                try:
                    query = "SELECT follower_name,follower_email,follower_username,follower_date FROM FOLLOWERS where follower_username = '%s';" % (follower_name)
                    cursor.execute(query)
                    rowcount = cursor.rowcount;
                    if rowcount == 0:
                        return "there is no such entry in the followers table"
                    return render_template('search_display.html', followers=cursor)
                except:
                    return "there is no such entry in the table"

This is search method on Interaction_c.py file. Entered user name is taken from follower_name_text and assigned as follower_name variable. This operation performs by request.form[] command. First query checks if the user who is wanted to be searched is in FOLLOWERS table or not. If it is not, error message is returned. If it is, then the selected row displays on the different page.

If user wants to update a follower in FOLLOWERS table, update method is operated.
 
.. code-block:: python 

   def update(config):
        follower_name = None
        follower_email = None
    
        if request.method == 'POST':
            follower_name = request.form['follower_name_text']
            song_name = request.form['song_name']
            social_media_name = request.form['social_media_name']
            with dbapi2.connect(config) as connection:
                cursor = connection.cursor()
                try:
                    query = "SELECT * FROM FOLLOWERS where follower_username = '%s';" % (follower_name)
                    cursor.execute(query)
                    rowcount = cursor.rowcount;
                    if rowcount == 0:
                        return "there is no such entry in the followers table"
                
                    if song_name == 'Cem Belevi - Alisamiyorum':
                        query = "SELECT playlist_id FROM PLAYLIST where singer_name = 'Cem Belevi'"
                    elif song_name == 'Murat Boz - Direniyorsun':
                        query = "SELECT playlist_id FROM PLAYLIST where singer_name = 'Murat Boz'"
                    elif song_name == 'Emir - Bir Agla':
                        query = "SELECT playlist_id FROM PLAYLIST where singer_name = 'Emir'"
                    elif song_name == 'Aydin Kurtoglu - Yak':
                        query = "SELECT playlist_id FROM PLAYLIST where singer_name = 'Ayd�n Kurtoglu'"
                    elif song_name == 'Mustafa Ceceli - Husran':
                        query = "SELECT playlist_id FROM PLAYLIST where singer_name = 'Mustafa Ceceli'"
                    elif song_name == 'Aleyna Tilki - Cevapsiz Cinlama':
                        query = "SELECT playlist_id FROM PLAYLIST where singer_name = 'Aleyna Tilki'"
                    elif song_name == 'Drake - Feel No Ways':
                        query = "SELECT playlist_id FROM PLAYLIST where singer_name = 'Drake'"
                    elif song_name == 'G-Eazy - Drifting':
                        query = "SELECT playlist_id FROM PLAYLIST where singer_name = 'G-Eazy'"
                    elif song_name == 'Wiz Khalifa - Material':
                        query = "SELECT playlist_id FROM PLAYLIST where singer_name = 'Wiz Khalifa'"
                    elif song_name == 'Tyga - Diced Pineapples':
                        query = "SELECT playlist_id FROM PLAYLIST where singer_name = 'Tyga'"
                    elif song_name == 'Usher - Lemme See':
                        query = "SELECT playlist_id FROM PLAYLIST where singer_name = 'Usher'"
                    elif song_name == 'The Weeknd - House of Balloons':
                        query = "SELECT playlist_id FROM PLAYLIST where singer_name = 'The Weeknd'"
                    elif song_name == 'Snoop Dogg - Kush':
                        query = "SELECT playlist_id FROM PLAYLIST where singer_name = 'Snoop Dogg'"
                    cursor.execute(query)
                    rows = cursor.fetchall()
                    for row in rows:
                        query = """UPDATE FOLLOWERS SET playlist_id= %s  where follower_username = %s ;"""
                        cursor.execute(query, (row[0], follower_name))
        
                    if social_media_name == 'Instagram':
                        query = "SELECT social_media_id FROM SM where social_media_name = 'Instagram'"
                    elif social_media_name == 'Facebook':
                        query = "SELECT social_media_id FROM SM where social_media_name = 'Facebook'"
                    elif social_media_name == 'Pinterest':
                        query = "SELECT social_media_id FROM SM where social_media_name = 'Pinterest'"
                    elif social_media_name == 'Tinder':
                        query = "SELECT social_media_id FROM SM where social_media_name = 'Tinder'"
                    elif social_media_name == 'Spotify':
                        query = "SELECT social_media_id FROM SM where social_media_name = 'Spotify'"
                    cursor.execute(query)
                    rows = cursor.fetchall()
                    for row in rows:
                        query = """UPDATE FOLLOWERS SET social_media_id= %s  where follower_username = %s ;"""
                        cursor.execute(query, (row[0], follower_name))
                        return render_template('followers.html')
                except:
                    return "exception occurs"

This is update method on Interaction_c.py file. Entered user name is taken from follower_name_text and assigned as follower_name variable. This operation performs by request.form[] command. First query checks if the user who is wanted to be searched is in FOLLOWERS table or not. If it is not, error message is returned. If it is, method keeps on performing. There are if clauses to get playlist_id from PLAYLIST table according to chosen singer and song from static table. SELECT query is used for this purpose. Playlist_id is selected by singer_name. After that, playlist_id of given user is updated with this selected playlist_id.
Again, according to selected social media from static SM table, social_media_id is taken with SELECT query from SM table by social_media_name. Then, social_media_id of entered user is updated with this taken social_media_id. When update operation is successfully done, the page refresh itselt, and followers.html opens again.
 
.. code-block:: python 

   {% extends "layout.html" %}
   {% block title %}{% endblock %}
   {% block content %}




   <head>
    <meta charset="utf-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
            <meta name="viewport" content="width=device-width, initial-scale=1">
                <!-- The above 3 meta tags *must* come first in the head; any other head content must come *after* these tags -->
                <meta name="description" content="">
                    <meta name="author" content="">
                        <link rel="stylesheet" href="{{ url_for('static', filename='bootstrap.css') }}" />
                       <!-- <link rel="stylesheet" href="{{ url_for('static', filename='custom.css') }}" /> -->
                        </head>


    <body>
    <div class="container-fluid bg-1 text-center">
        <h1>Welcome to Unicorn!</h1>
        <img src="{{ url_for('static', filename='unicorn.png') }}" class="img-circle" alt="unicorn" width="100" height="100">
            </div>
         <form action="{{ url_for('insertM_following') }}" method="POST">
          <div class="container bg-2 text-center">
            <h3>Follow</h3>
            <div class="form-group">
                <label for="pwd">Please enter an username:</label>
                <input class="form-control" name="follower_name_text" id="follower_name_text" type="name_text">
                    </div>
          
         </div>    
              <button type="follow" id="btn_follow" class="btn btn-default">Follow</button>
             
                               </form>
                               
                               
       <form action="{{ url_for('unfollowM_following') }}" method="POST">
          <div class="container bg-2 text-center">
            <h3>Unfollow</h3>
            <div class="form-group">
                <label for="pwd">Please enter an username:</label>
                <input class="form-control" name="follower_name_text" id="follower_name_text" type="name_text">
                    </div>
           

                   </div>   
                 <button type="unfollow" id="btn_unfollow" class="btn btn-default">Unfollow</button>
        
                       </form>
           
         <form action="{{ url_for('searchM_following') }}" method="POST">
          <div class="container bg-2 text-center">
            <h3>Search</h3>
            <div class="form-group">
                <label for="pwd">Please enter an username:</label>
                <input class="form-control" name="follower_name_text" id="follower_name_text" type="name_text">
                    </div>
          

                   </div>   
                 <button type="search" id="btn_unfollow" class="btn btn-default">Search</button>
        
                       </form>
                       
                       
                        
         <form action="{{ url_for('find_following') }}" method="POST">
          <div class="container bg-2 text-center">
            <h3>Find</h3>
            <div class="form-group">
                <label for="pwd">Find people around you!</label>
                <input class="form-control" name="find_text" id="find_text" type="name_text">
                    </div>
          

                   </div>   
                 <button type="find" id="btn_find" class="btn btn-default">Find</button>
        
                       </form>
                           
         <form action="{{ url_for('updateM_following') }}" method="POST">
          <div class="container bg-2 text-center">
            <h3>Update</h3>
            <div class="form-group">
            
              <label for="pwd">Please enter an username:</label>
                <input class="form-control" name="follower_name_text" id="follower_name_text" type="name_text">
                
                  <label for="pwd">Please enter your location:</label>
                <input class="form-control" name="location_text" id="location_text" type="name_text">
                
                
   	 <label for="ublock">Please choose an event to add to your coming events list</label>
   	 <select class="form-control" name="event_name" id="event_type">
   	    <option>Kalben</option>
        <option>Mabel Matiz</option>
        <option>Athena</option>
        <option>Cem Adrian</option>
        <option>Yasar</option>

    </select>                 
               
                    </div>
           

                   </div>   
                 <button type="update" id="btn_unfollow" class="btn btn-default">Update</button>
                       </form>
           
   

  <head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <!-- The above 3 meta tags *must* come first in the head; any other head content must come *after* these tags -->
    <meta name="description" content="">
    <meta name="author" content="">
   <link rel="stylesheet" href="{{ url_for('static', filename='bootstrap.css') }}" />
   <link rel="stylesheet" href="{{ url_for('static', filename='custom.css') }}" />

  </head>

  <body>

    <div class="container">
        <h2>FOLLOWING</h2>
      <div class="header clearfix">
        <nav>
          <ul class="nav nav-pills pull-right">
            <li role="presentation" ><a href="{{ url_for('home_page') }}">Home</a></li>
            <li role="presentation"><a href="{{ url_for('login') }}">Switch User</a></li>
          </ul>
        </nav>

      </div>



    </div> <!-- /container -->
    </div>
    </div>

  <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.12.4/jquery.min.js"></script>
  <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js"></script>
    <!-- IE10 viewport hack for Surface/desktop Windows 8 bug -->
  </body>

 </html>
 {% endblock %}

This is following.html page. This page appears when the user clicks on Add to Following List button on interaction page. There are five text field and button pairs, and all buttons refer to different methods in server.py file. The first button namely Follow, takes the entered data from text field and sends it insertM_following method on server.py file. Other buttons Unfollow, Search, Find, and Update perform the same operation for unfollowM_following, searchM_following, find_following, and updateM_following methods in order. Update button sends not only written data on text field but also chosen event from static tables which are represented with drop down list.

Lets examine these method in detail.


This is the part of server.py code. insertM_following, unfollowM_following, searchM_following, find_following, and updateM_following methods that are referred by the buttons on following.html page are created here. These five methods also refer to related methods on Interaction_c.py code. They call follow_following, unfollow_following, search_following, find, and update_following methods in order.

If user wants to add a new following to FOLLOWING table, follow_ following method is operated.
 
.. code-block:: python

   def follow_following(config):
        following_name = None
        following_email = None
        if request.method == 'POST':
            user_loginname = request.form['follower_name_text']
            '''print(follower_email)'''
            with dbapi2.connect(config) as connection:
                cursor = connection.cursor()
                try:
                    query = "SELECT * FROM FOLLOWING where following_username = '%s'" % (user_loginname)
                    cursor.execute(query)
                    rowcount = cursor.rowcount;
                    if rowcount != 0:
                        return "this entry already exists in following table"
                
                
                    query = "SELECT user_name,user_email,user_loginname FROM USER_LOGIN where user_loginname = '%s'" % (user_loginname)
                    cursor.execute(query)
                    rowcount = cursor.rowcount;
                    if rowcount == 0:
                        return "there is no such entry in the user table"
                    rows = cursor.fetchall()
                    for row in rows:
                        query = """INSERT INTO FOLLOWING(following_name,following_email,following_username) VALUES(%s,%s,%s)"""
                        cursor.execute(query, (row[0], row[1], row[2]))
                        connection.commit();
                        return render_template('following.html')
                except:
                    return "exception occurs"

This is follow_ following method on Interaction_c.py file. Entered user name is taken from follower_name_text and assigned as user_loginname variable. This operation performs by request.form[] command. First query checks if the user who is wanted to be inserted to FOLLOWING table is already in FOLLOWING table or not. If it is, error message is returned. If it is not, then the given user name is checked whether it is registered to unicorn or not. If it is not, again error message is returned. If it is, then with select query, user information is taken from USER_LOGIN table and then INSERT INTO FOLLOWING table. As I mentioned before, FOLLOWING table gets its following_name, following _email and following _username values from USER_LOGIN table with select query. After add operation is successfully done, the page is directed to followers.html page by render_template(“following.htm”) line.


If user wants to remove a following from FOLLOWING table, unfollow_following method is operated.

.. code-block:: python

   def unfollow_following(config):
        if request.method == 'POST':
            following_username = request.form['follower_name_text']
            with dbapi2.connect(config) as connection:
                cursor = connection.cursor()
                try:
                    query = "SELECT * FROM FOLLOWING WHERE following_username = '%s'" % (following_username)
                    cursor.execute(query)
                    rowcount = cursor.rowcount;
                    if rowcount == 0:
                        print ("there is no such entry in the followers table")
                        return " "
                    query = "DELETE FROM FOLLOWING WHERE following_username = '%s'" % (following_username)
                    cursor.execute(query)
                    connection.commit();
                    return redirect(url_for('following'))
                except:
                    return "exception occurs"
   
This is unfollow_following method on Interaction_c.py file. Entered user name is taken from follower_name_text and assigned as following_username variable. This operation performs by request.form[] command. First query checks if the user who is wanted to be deleted from FOLLOWING table is in FOLLOWING table or not. If it is not, error message is returned. If it is, then the row is removed from the table according to given following_username. After delete operation is successfully done, the page is directed to following.html page by render_template(“following.htm”) line.
 

If user wants to search for a following in FOLLOWING table, search_following method is operated.

.. code-block:: python
   
   def search_following(config):
        following_name = None
        following_email = None
        if request.method == 'POST':
            following_name = request.form['follower_name_text']
            with dbapi2.connect(config) as connection:
                cursor = connection.cursor()
                try:
                    query = "SELECT following_name,following_email,following_username,following_date FROM FOLLOWING where following_username = '%s';" % (following_name)
                    cursor.execute(query)
                    rowcount = cursor.rowcount;
                    if rowcount == 0:
                        return "there is no such entry in the following table"
                    rows = cursor.fetchall()
                    for row in rows:
                        print (row[0], row[1], row[2], row[3])
                        return "selected row is printed"
            
                except:
                    return "there is no such entry in the table"

This is search_following method on Interaction_c.py file. Entered user name is taken from follower_name_text and assigned as following_name variable. This operation performs by request.form[] command. First query checks if the user who is wanted to be searched is in FOLLOWING table or not. If it is not, error message is returned. If it is, then the selected row displays on the different page.

If user wants to update a following in FOLLOWING table, update_following method is operated.

.. code-block:: python

   def update_following(config):
        following_name = None
        following_email = None
        if request.method == 'POST':
            following_name = request.form['follower_name_text']
            event_name = request.form['event_name']
            location_name = request.form['location_text']
            with dbapi2.connect(config) as connection:
                cursor = connection.cursor()
                try:
                    query = "SELECT * FROM FOLLOWING where following_username = '%s'" % following_name
                    cursor.execute(query)
                    rowcount = cursor.rowcount;
                    if rowcount == 0:
                        return "there is no such entry in the following table"
                    if event_name == 'Kalben':
                        query = "SELECT event_id FROM EVENTS where event_name = 'Kalben'"
                    elif event_name == 'Mabel Matiz':
                        query = "SELECT event_id FROM EVENTS where event_name = 'Mabel Matiz'"
                    elif event_name == 'Cem Adrian':
                        query = "SELECT event_id FROM EVENTS where event_name = 'Cem Adrian'"
                    elif event_name == 'Athena':
                        query = "SELECT event_id FROM EVENTS where event_name = 'Athena'"
                    elif event_name == 'Yasar':
                        query = "SELECT event_id FROM EVENTS where event_name = 'Yasar'"
                    cursor.execute(query)
                    rows = cursor.fetchall()
                    for row in rows:
                        query = """UPDATE FOLLOWING SET event_id= %s  where following_username = %s ;"""
                        cursor.execute(query, (row[0], following_name))
                        query = "SELECT * FROM LOCATION where location_name = '%s'" % location_name
                        cursor.execute(query)
                        rowcount = cursor.rowcount;
                    if rowcount == 0:
                        return "there is no such city in the location table"
                    rows = cursor.fetchall()
                    for row in rows:
                        query = """UPDATE FOLLOWING SET location_id= %s  where following_username = %s ;"""
                        cursor.execute(query, (row[0], following_name))
                        return render_template('following.html')
                except:
                    return "exception occurs"

This is update_following method on Interaction_c.py file. Entered user name is taken from follower_name_text and assigned as following_name variable. This operation performs by request.form[] command. First query checks if the user who is wanted to be searched is in FOLLOWING table or not. If it is not, error message is returned. If it is, method keeps on performing. There are if clauses to get event_id from EVENTS table according to chosen event from static table. SELECT query is used for this purpose. event_id is selected by event_name. After that, event_id of given user is updated with this selected event_id. Again, according to entered location to the text field namely location_text, location _id is taken with SELECT query from LOCATION table by location _name. Then, location _id of entered user is updated with this taken location _id. When update_following operation is successfully done, the page refresh itselt, and following.html opens again.

.. code-block:: python

   def find(config):
        if request.method == 'POST':
            location_name = request.form['find_text']
            with dbapi2.connect(config) as connection:
                cursor = connection.cursor()
                try:
                    query = "SELECT location_id from LOCATION where location_name = '%s';" % (location_name)
                    cursor.execute(query)
                    rowcount = cursor.rowcount;
                    if rowcount == 0:
                        return "there is no such city in the location table"
                    rows = cursor.fetchall()
                    for row in rows:
                        query = "SELECT * FROM FOLLOWING where location_id = '%s';"
                        cursor.execute(query, (row[0],))
                        rowcount = cursor.rowcount
                        if rowcount == 0:
                            return "there is no such following person in this location"
                        rows2 = cursor.fetchall()
                        for row2 in rows2:
                            print (row2[1], row2[2], row2[3])
                            return "selected row is printed"
                except:
                    return "exception occurs"

Find method performs when the user clicks on Find button on following.html page. This method gets entered location from text field namely find_text and assigns it to location_name variable. Then search for location_id from LOCATION table where the location_name equals to entered location name. If there is no such city in the table, then error message displays on the screen. If it exists in LOCATION table, then SELECT query searches for the following person whose location_id equals to the location_id of entered city. Then selected rows are printed on the screen.
 
.. code-block:: python

   {% extends "layout.html" %}
   {% block title %}{% endblock %}
   {% block content %}




    <head>
    <meta charset="utf-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
            <meta name="viewport" content="width=device-width, initial-scale=1">
                <!-- The above 3 meta tags *must* come first in the head; any other head content must come *after* these tags -->
                <meta name="description" content="">
                    <meta name="author" content="">
                        <link rel="stylesheet" href="{{ url_for('static', filename='bootstrap.css') }}" />
                       <!-- <link rel="stylesheet" href="{{ url_for('static', filename='custom.css') }}" /> -->
                        </head>


     <body>
    <div class="container-fluid bg-1 text-center">
        <h1>Welcome to Unicorn!</h1>
        <img src="{{ url_for('static', filename='unicorn.png') }}" class="img-circle" alt="unicorn" width="100" height="100">
            </div>
         <form action="{{ url_for('insertM_blocked') }}" method="POST">
          <div class="container bg-2 text-center">
            <h3>Block</h3>
            <div class="form-group">
                <label for="pwd">Please enter an username:</label>
                <input class="form-control" name="follower_name_text" id="follower_name_text" type="name_text">
                    </div>
      

         </div>    
              <button type="follow" id="btn_follow" class="btn btn-default">Follow</button>
             
                               </form>
                               
                               
       <form action="{{ url_for('unfollowM_blocked') }}" method="POST">
          <div class="container bg-2 text-center">
            <h3>Unblock</h3>
            <div class="form-group">
                <label for="pwd">Please enter an username:</label>
                <input class="form-control" name="follower_name_text" id="follower_name_text" type="name_text">
                    </div>
      

                   </div>   
                 <button type="unfollow" id="btn_unfollow" class="btn btn-default">Unfollow</button>
        
                       </form>
           
         <form action="{{ url_for('searchM_blocked') }}" method="POST">
          <div class="container bg-2 text-center">
            <h3>Search</h3>
            <div class="form-group">
                <label for="pwd">Please enter an username:</label>
                <input class="form-control" name="follower_name_text" id="follower_name_text" type="name_text">
                    </div>
           

                   </div>   
                 <button type="search" id="btn_unfollow" class="btn btn-default">Search</button>
         
                       </form>
                       
                           
         <form action="{{ url_for('updateM_blocked') }}" method="POST">
          <div class="container bg-2 text-center">
            <h3>Update</h3>
            <div class="form-group">
                <label for="pwd">Please enter an username that you want to update:</label>
                <input class="form-control" name="follower_name_text" id="follower_name_text" type="name_text">
                 
           </div>
 
                    
                <div class="form-group">
       				<label for="pwd">Please enter a new blocking time :</label>
                	<input class="form-control" name="blocking_time" id="blocking_time" type="blocking_time">
                </div>

     <div class="form-group">
    <label for="ublock">Please choose block type</label>
    <select class="form-control" name="block_type" id="block_type">
        <option>inappropriate content</option>
        <option>fake profile</option>
        <option>distracting message content</option>
        <option>violent profile</option>

    </select>
   </div>

           </div>
                 <button type="update" id="btn_unfollow" class="btn btn-default">Update</button>
                       </form>
           
   

  <head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <!-- The above 3 meta tags *must* come first in the head; any other head content must come *after* these tags -->
    <meta name="description" content="">
    <meta name="author" content="">
   <link rel="stylesheet" href="{{ url_for('static', filename='bootstrap.css') }}" />
   <link rel="stylesheet" href="{{ url_for('static', filename='custom.css') }}" />

  </head>

  <body>

    <div class="container">
        <h2>BLOCKED</h2>
      <div class="header clearfix">
        <nav>
          <ul class="nav nav-pills pull-right">
            <li role="presentation" ><a href="{{ url_for('home_page') }}">Home</a></li>
            <li role="presentation"><a href="{{ url_for('login') }}">Switch User</a></li>
          </ul>
        </nav>

      </div>



    </div> <!-- /container -->
    </div>
    </div>

  <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.12.4/jquery.min.js"></script>
  <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js"></script>
    <!-- IE10 viewport hack for Surface/desktop Windows 8 bug -->
  </body>

  </html>
  {% endblock %}

This is blocked.html page. This page appears when the user clicks on Add to Blocked List button on interaction page. There are four text field and button pairs, and all buttons refer to different
 
methods in server.py file. The first button namely Block, takes the entered data from text field and sends it insertM_blocked method on server.py file. Other buttons Unblocked, Search, and Update perform the same operation for unfollowM_blocked, searchM_blocked, and updateM_blocked methods in order. Update button sends not only written data on text field but also chosen blocking type from static tables which are represented with drop down list.

Lets examine these method in detail.


This is the part of server.py code. insertM_blocked, unfollowM_blocked, searchM_blocked, and updateM_blocked methods that are referred by the buttons on blocked.html page are created here. These five methods also refer to related methods on Interaction_c.py code. They call follow_ blocked, unfollow_ blocked, search_ blocked, and update_ blocked methods in order.

If user wants to add a new blocked person to BLOCKED table, follow_ blocked method is operated.

.. code-block:: python

   def follow_blocked(config):
        blocked_name = None
        blocked_email = None
        if request.method == 'POST':
            user_loginname = request.form['follower_name_text']
            with dbapi2.connect(config) as connection:
                cursor = connection.cursor()
                try:
                
                    query = "SELECT * FROM BLOCKED where blocked_username = '%s'" % (user_loginname)
                    cursor.execute(query)
                    rowcount = cursor.rowcount;
                    if rowcount != 0:
                        return "this entry already exists in blocked table"
                
                    query = "SELECT user_name,user_email,user_loginname FROM USER_LOGIN where user_loginname = '%s'" % (user_loginname)
                    cursor.execute(query)
                    rowcount = cursor.rowcount;
                    if rowcount == 0:
                        return "there is no such entry in the user table"
                    rows = cursor.fetchall()
                    for row in rows:
                        query = """INSERT INTO BLOCKED(blocked_name,blocked_email,blocked_username) VALUES(%s,%s,%s)"""
                        cursor.execute(query, (row[0], row[1], row[2]))
                        connection.commit();
                        return render_template('blocked.html')
                except:
                    return "exception occurs"

This is follow_blocked method on Interaction_c.py file. Entered user name is taken from follower_name_text and assigned as user_loginname variable. This operation performs by request.form[] command. First query checks if the user who is wanted to be inserted to BLOCKED table is already in BLOCKED table or not. If it is, error message is returned. If it is not, then the given user name is checked whether it is registered to unicorn or not. If it is not, again error message is returned. If it is, then with select query, user information is taken from USER_LOGIN table and then INSERT INTO BLOCKED table. As I mentioned before, BLOCKED table gets its blocked_name, blocked _email and blocked _username values from USER_LOGIN table with select query. After add operation is successfully done, the page is directed to blocked.html page by render_template(“blocked.htm”) line.


If user wants to unblocked a blocked person from BLOCKED table, unfollow_blocked method is operated.

.. code-block:: python 

   def unfollow_blocked(config):
        if request.method == 'POST':
            blocked_username = request.form['follower_name_text']
            with dbapi2.connect(config) as connection:
                cursor = connection.cursor()
                try:
                    query = "SELECT blocked_name,blocked_email,blocked_username FROM BLOCKED WHERE blocked_username = '%s'" % (blocked_username)
                    cursor.execute(query)
                    rowcount = cursor.rowcount;
                    if rowcount == 0:
                        return "there is no such entry in the followers table"
                    query = "DELETE FROM BLOCKED WHERE blocked_username = '%s'" % (blocked_username)
                    cursor.execute(query)
                    connection.commit();
                    return redirect(url_for('blocked'))
                except:
                    return "exception occurs"

This is unfollow_blocked method on Interaction_c.py file. Entered user name is taken from follower_name_text and assigned as blocked_username variable. This operation performs by request.form[] command. First query checks if the user who is wanted to be deleted from BLOCKED table is in BLOCKED table or not. If it is not, error message is returned. If it is, then the row is removed from the table according to given blocked_username. After delete operation is successfully done, the page is directed to blocked.html page by render_template(“blocked.htm”) line.


If user wants to search for a blocked person in BLOCKED table, search_blocked method is operated.

.. code-block:: python

   def search_blocked(config):
        blocked_name = None
        blocked_email = None
        if request.method == 'POST':
            blocked_name = request.form['follower_name_text']
            with dbapi2.connect(config) as connection:
                cursor = connection.cursor()
                try:
                    query = "SELECT blocked_name,blocked_email,blocked_username,blocked_date,blocked_type FROM BLOCKED where blocked_username = '%s';" % (blocked_name)
                    cursor.execute(query)
                    rowcount = cursor.rowcount;
                    if rowcount == 0:
                        return "there is no such entry in the blocked table"
                    rows = cursor.fetchall()
                    for row in rows:
                        print (row[0], row[1], row[2], row[3],row[4])
                        return "selected row is printed"
                except:
                    return "there is no such entry in the table"

This is search_blocked method on Interaction_c.py file. Entered user name is taken from follower_name_text and assigned as blocked_name variable. This operation performs by request.form[] command. First query checks if the user who is wanted to be searched is in BLCOKED table or not. If it is not, error message is returned. If it is, then the selected row displays on the different page.

If user wants to update a blocked person information in BLOCKED table, update_blocked method is operated.
 
.. code-block:: python
   
   def update_blocked(config):
        blocked_name = None
        blocked_email = None
        if request.method == 'POST':
            blocked_name = request.form['follower_name_text']
            blocked_type = request.form['block_type']
            blocking_time = request.form['blocking_time']
            with dbapi2.connect(config) as connection:
                cursor = connection.cursor()
                try:
                    query = "SELECT * FROM BLOCKED where blocked_username = '%s'" % blocked_name
                    cursor.execute(query)
                    rowcount = cursor.rowcount;
                    if rowcount == 0:
                        return "there is no such entry in the following table"  
                    
                    if blocked_type == 'inappropriate content' :
                        query = """UPDATE BLOCKED SET blocked_type='inappropriate content' where blocked_username = '%s' ;""" %blocked_name
                        cursor.execute(query)
                    elif blocked_type == 'fake profile' :
                        query = """UPDATE BLOCKED SET blocked_type= 'fake profile' where blocked_username = '%s' ;"""%blocked_name
                        cursor.execute(query)
                    elif blocked_type == 'distracting message content' :
                        query = """UPDATE BLOCKED SET blocked_type= 'distracting message content' where blocked_username = '%s' ;"""%blocked_name
                        cursor.execute(query)
                    elif blocked_type == 'violent profile' :
                        query = """UPDATE BLOCKED SET blocked_type= 'violent profile' where blocked_username = '%s' ;"""%blocked_name
                        cursor.execute(query)    
                    connection.commit();
                    print(blocking_time)
                    print(blocked_name)
                    query = """UPDATE BLOCKED SET blocking_time=%s where blocked_username =%s ;"""
                    cursor.execute(query,(blocking_time,blocked_name))
                    connection.commit();
                    return render_template('blocked.html')
                except:
                    return "exception occurs"

This is update_blocked method on Interaction_c.py file. Entered user name is taken from follower_name_text and assigned as blocked_name variable. This operation performs by request.form[] command. First query checks if the user who is wanted to be searched is in BLOCKED table or not. If it is not, error message is returned. If it is, method keeps on performing.

There are if clauses to update blocked_type of entered user according to blocked_username. Blocked_type is taken from drop down list and assigned to blocked_type variable. Then this variable is used in UPDATE BLOCKED SET blocked_type query.

Another updated column is blocking_time, according to entered data to the text field namely blocking_time. Then this variable is used in UPDATE BLOCKED SET blocking_time query. When update_following operation is successfully done, the page refresh itselt, and blocked.html opens again.

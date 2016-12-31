Parts Implemented by Songül Saraç
================================

  Tweets, Tags, Directmessages, Comments and Activities entities were implemented by creating classes with same name of entities and all these classes have some specific methods in order to make insert, select, update and delete operations.
In the following, these operations were explained in detail by giving Python, SQL and HTML codes.
1.	Tweets Class:

  This class is created on tweets.py Python file and it contains 6 main methods to make operation on tweets table. The structure of tweets table and its columns can be understood from the following explanation.
  
Tweets Table:
•	TWEET_ID SERIAL UNIQUE:  This is the primary key of tweets table, it is serial; thus, it incremented by one after each entry into table. This enables fast search operation into table.
•	USER_LOGNAME VARCHAR(60) NOT NULL  This column stores username of a user and it cannot have a null value. Type of this column is varying character up to 60.
•	DATE DATE DEFAULT CURRENT_DATE: This column holds the date of the tweet is posted and it has a default value. This value is date of adding a new tweet.
•	TWEET_CATEGORY VARCHAR(100) NOT NULL: This column is for storing the category of tweet and it cannot be null. Type of this column is varying character up to 100.
•	TWEET_INPUT VARCHAR(200) UNIQUE NOT NULL: This column holds tweets whose type is character varying at most 200 character. It is unique and cannot have a null value. 

Constraints of Table:
•	FOREIGN KEY(USER_LOGNAME) REFERENCES IN USER_LOGIN(USER_LOGINNAME) ON DELETE CASCADE ON UPDATE CASCADE  user_logname column has a foreign key by having a relationship with user_loginname column in user_login table. When there is a deletion or updating operation on user_loginname, if there is a row in tweets table with same username , it will also be deleted or updated.


Methods of Tweets Class:
•	INITIALIZE TABLES METHOD: initialize_tweets() -> in this method, all tables were mentioned above are dropped and created again. The following SQL and Python codes were written in order to achieve this operation. It takes a config as a parameter to connect to database and returns a string “Tables inserted”. 

.. code-block:: python
  class tweets:
    def initialize_tweets(config):
        with dbapi2.connect(config) as connection:
            cursor = connection.cursor()
            query = """DROP TABLE IF EXISTS TWEETS CASCADE;"""
            cursor.execute(query)
            query = """CREATE TABLE IF NOT EXISTS TWEETS (
            tweet_id serial unique,
            user_logname VARCHAR(60) not null,
            tweet_input VARCHAR(200) unique not null,
            date date default current_date,
            tweet_category VARCHAR(100) not null,
            primary key(tweet_id, user_logname),
            foreign key(user_logname) references user_login(user_loginname) on delete cascade on update cascade            )
            """
            cursor.execute(query)

            query = """DROP TABLE IF EXISTS TAGS CASCADE;"""
            cursor.execute(query)

            query = """CREATE TABLE IF NOT EXISTS TAGS (
            tag_id serial unique,
            tweet_input VARCHAR(200) not null,
            tag_input VARCHAR(200) unique not null,
            tag_category VARCHAR(100) not null,
            date date default current_date ,
            primary key(tag_id),
            foreign key(tweet_input) references TWEETS(tweet_input) on delete cascade on update cascade
            )
            """

            cursor.execute(query)

            query = """DROP TABLE IF EXISTS COMMENTS CASCADE;"""
            cursor.execute(query)


            query = """CREATE TABLE IF NOT EXISTS COMMENTS (
            tweet_input VARCHAR(200) not null,
            comment_id serial unique not null,
            comment VARCHAR(200) not null,
            user_logname VARCHAR(60) not null,
            date date default current_date,
            primary key(comment_id),
            foreign key(user_logname) references user_login(user_loginname) on delete cascade on update cascade,
            foreign key(tweet_input) references TWEETS(tweet_input) on delete cascade on update cascade)
            """

            cursor.execute(query)

            query = """DROP TABLE IF EXISTS DIRECTMESSAGES CASCADE;"""
            cursor.execute(query)

            query = """CREATE TABLE IF NOT EXISTS DIRECTMESSAGES(
            dm_id serial unique,
            user_logname1 VARCHAR(60) not null,
            user_logname2 VARCHAR(60) not null,
            message VARCHAR(200) not null,
            subject VARCHAR(100) not null,
            date date default current_date,
            primary key(dm_id),
            foreign key(user_logname1) references user_login(user_loginname) on delete cascade on update cascade,
            foreign key(user_logname2) references user_login(user_loginname) on delete cascade on update cascade
            )
            """

            cursor.execute(query)

            query = """DROP TABLE IF EXISTS ACTIVITIES CASCADE;"""
            cursor.execute(query)


            query = """CREATE TABLE IF NOT EXISTS ACTIVITIES(
            event_id serial unique not null,
            event_name VARCHAR(200) unique not null,
            event_location VARCHAR(200) not null,
            event_date VARCHAR(200) not null,
            event_category VARCHAR(200) not null,
            primary key(event_id, event_name))
            """

            cursor.execute(query)

            connection.commit();
            return 'Tables inserted <a href="http://localhost:5000">Home</a>'
            
Here, tweets, tags, directmessages, comments and activities table are created with  SQL written in dashes and assigned to query. For each SQL, query should be executed. At the end of initialize_tweets() function in tweets class, changes are commited in order to show this changes on database.


This function is called initialize_tweets() function on server.py with approute /tweets/initialize_tweets.

.. code-block:: python 
  @app.route('/tweets/initialize_tweets', methods=['GET', 'POST'])
  def initialize_tweets():
        return tweet.initialize_tweets(app.config['dsn'])


•	INSERT METHOD: savetweet() -> This method is written for insert operation for tweet in tweets class. Due to foreign key constraint of tweets table, there is an exception for this method by using “try and catch” object oriented approach. Python and SQL code for  this method is showed in the following block.

.. code-block:: python

    def savetweet(config):
        new_tweet = None
        user_login = None
        new_category = None
        if request.method == 'POST':
            new_tweet = request.form['tweet_text']
            print(new_tweet)
            user_login = request.form['username_text']
            print(user_login)
            new_category = request.form['category_text']
            print(new_category)
            with dbapi2.connect(config) as connection:
                cursor = connection.cursor()
                try:
                    query = """INSERT INTO TWEETS (user_logName, tweet_input, tweet_category) VALUES (%s, %s, %s)"""
                    cursor.execute(query, (user_login, new_tweet, new_category))
                    connection.commit();
                    return 'Your tweet has been successfully posted<a href="http://localhost:5000">Home</a>'
                except:
                    return 'Your tweet cannot be posted due to foreign key constraints! <a href="http://localhost:5000">Home</a>'
                  
This method is called in savetw() function on server.py as follow approute.

.. code-block:: python
  @app.route('/savetweet', methods=['POST'])
  def savetw():
  return tweet.savetweet(app.config['dsn'])
  
In order to achieve insert a new tweet row into tweets table. “INSERT INTO (USER_LOGNAME, TWEET_INPUT, TWEET_CATEGORY) VALUES (%s, %s, %s)” query were used. Due to the serial property of tweet_id coloumn, there is no need to take a value from user for this column, but for other columns are taken from user by using “POST” method of HTML. The insertion part of HTML code as follow.

.. code-block:: python

    <body>
    <div class="container bg-2 text-center">
  <h3> Please Enter Username and Tweet </h3>
    <form class="col-lg-12" action="{{url_for('savetw')}}" method="POST">
    <div class="form-group">
      <label for="name">Username:</label>
       <input class="form-control" id="username_text" name="username_text" type="text">
    </div>
    <div class="form-group">
      <label for="tweet">Tweet for User:</label>
       <input class="form-control" name="tweet_text" id="tweet_text" type="text">
    </div>

        <div class="form-group">
      <label for="category">Tweet Category:</label>
       <input class="form-control" name="category_text" id="category_text" type="text">
    </div>

   <button type="submit" id="btn_sign" class="btn btn-default">Save</button>
   </form>

  <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.12.4/jquery.min.js"></script>
  <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js"></script>
    <!-- IE10 viewport hack for Surface/desktop Windows 8 bug -->
  </body>
  
In this format, there are 3 text boxes in order to take values from user and bootstrap were used.

•	SELECT METHOD: tweets_db() -> This medhod was written in order to display all tweets on tweet panel page by using “SELECT” query. This method can be seen as follow in Python language. It takes a config as a parameter due to connecting database and it returns tweet.html page.

.. code-block:: python
    def tweets_db(config):
        with dbapi2.connect(config) as connection:
            if request.method == 'GET':
                cursor = connection.cursor()
                query = "SELECT user_logname,tweet_id,tweet_input,tweet_category, date from tweets"
                cursor.execute(query)
                connection.commit();
                return render_template('tweets.html', tweets_list=cursor)
                
This function is called in tweets() function on server.py as below.

.. code-block:: python 

  @app.route('/tweets')
  def tweets():
    return tweet.tweets_db(app.config['dsn'])

       
The select part of HTML code to display all rows in tweets table as below. By using “GET” method of HTML all taken columns from database can be showed on tweets page. 

.. code-block:: python
    <body>
  
    <div class="container bg-2 text-center">
  <h3> Please Enter Username and Tweet </h3>
    <form class="col-lg-12" action="{{url_for('savetw')}}" method="POST">
    <div class="form-group">
      <label for="name">Username:</label>
       <input class="form-control" id="username_text" name="username_text" type="text">
    </div>
    <div class="form-group">
      <label for="tweet">Tweet for User:</label>
       <input class="form-control" name="tweet_text" id="tweet_text" type="text">
    </div>

        <div class="form-group">
      <label for="category">Tweet Category:</label>
       <input class="form-control" name="category_text" id="category_text" type="text">
    </div>

   <button type="submit" id="btn_sign" class="btn btn-default">Save</button>
   </form>

  <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.12.4/jquery.min.js"></script>
  <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js"></script>
    <!-- IE10 viewport hack for Surface/desktop Windows 8 bug -->

  </body>


Here, there is a for loop in tweets list that is created by select query and for each row of tweets table, there are “Delete” and “Update” link in order to achieve these operations.

• DELETE METHOD:	tweets_db_delete() -> This method is written in order to make delete operation on tweets table. It takes a config to connect database and username value that will be deleted as parameters. Written Python code can be seen as follow for this operation. Due to the fact that “cascade” is used on deletion operation, there is no need to make exception.

.. code-block:: python
      def tweets_db_delete(config, deleteTweet):
        with dbapi2.connect(config) as connection:
            cursor = connection.cursor()
            query = "DELETE FROM tweets where user_logname = %s"
            cursor.execute(query, (deleteTweet,))
            connection.commit();
            return redirect(url_for('tweets'))

This method is called in tweet_delete() function on server.py with following approute.

.. code-block:: python
  @app.route('/tweets/delete/<deleteTweet>', methods=['GET', 'POST'])
  def tweet_delete(deleteTweet):
    return tweet.tweets_db_delete(app.config['dsn'],deleteTweet)
  

• UPDATE METHODS:	

•tweets_db_update() -> This method is written for finding with username that is taken from user. All search operations are made with username. Actually, this method finds tweet_input that will be updated in the following method that will be explained in detail. This method returns tweet_update.html in order to complete update operation.

•	tweets_db_update_apply() -> This method is written in order to make update operation. It takes config and username from user as parameters and executes “UPDATE TWEETS SET TWEET_INPUT = %s WHERE USER_LOGNAME = %s” ,new tweet input is taken from user by HTML code. Due to the fact that “cascade” is used on update operation, there is no need to make exception.

.. code-block:: python 

    def tweets_db_update(config, updateTweet):
        with dbapi2.connect(config) as connection:
            cursor = connection.cursor()
            query = """SELECT tweet_input from tweets where user_logname = '%s'""" % (updateTweet)
            cursor.execute(query)
            connection.commit();
            return render_template('tweet_update.html', tweet_updates=cursor)


    def tweets_db_update_apply(config, updateTweet):
        with dbapi2.connect(config) as connection:
            cursor = connection.cursor()
            try:
                new_tweet = request.form['tweet']
                query = """UPDATE tweets set tweet_input ='%s' where user_logName = '%s'""" % (new_tweet, updateTweet)
                cursor.execute(query)
                connection.commit();
                return redirect(url_for('tweets'))
            except:
                return 'Value cannot be NULL! <a href="http://localhost:5000">Home</a>'

These methods are called in tweet_update() and tweets_apply() function on server.py

.. code-block:: python 
  @app.route('/tweets/update/<updateTweet>/', methods=['GET', 'POST'])
  def tweet_update(updateTweet):
    return tweet.tweets_db_update(app.config['dsn'],updateTweet)

  @app.route('/tweets/update/<updateTweet>/apply', methods=['GET', 'POST'])
  def tweets_apply(updateTweet):
    return tweet.tweets_db_update_apply(app.config['dsn'],updateTweet)
    
HTML code for update tweet operation can be seen below.

.. code-block:: python 

  <body>
    <div class="container">
        <h2>UPDATE TWEET</h2>
      <div class="header clearfix">
        <nav>
          <ul class="nav nav-pills pull-right">
           <li role="presentation" class="active"><a href="{{ url_for('home_page') }}">Home</a></li>
          </ul>
        </nav>
      </div>
  <form action="apply" method = "post">
  <table id="tweetEditTable" class="table" width="500px">
	 <thead>
      <tr>
		<th>User Tweet</th>
      </tr>
    </thead>
	<tbody>
    {% for tweet_input in tweet_updates %}
    <td><input type="text" name="tweet" required="required" value="{{tweet_input[0]}}" style="width:95%"></td>
    {% endfor %}
  <tr>		<td colspan="3" align="center"><input value="Update Tweet" name="add" type="submit"></td>
	</tr>
	</tbody>
	</table>
    </div> <!-- /container -->
  <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.12.4/jquery.min.js"></script>
  <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js"></script>
    <!-- IE10 viewport hack for Surface/desktop Windows 8 bug -->
  </body>
  
 
Bootstrap is used and by using for loop tweet that will be updated displayed on text box on update tweet page. As you can see there are 3 HTML pages for tweet operations. These are, tweets.html, tweet_edit.html, tweet_update.html pages.

2.	Tags Class:
  This class was created on tags.py Python file and it includes 5 main methods to make basic database operation on tags table. Tags table and its columns are as below. There are 3 main HTML files were created for making these operations on tags table; these are, tags.html, tags_edit.html and tags_update.html pages.
Tags Table:

•	TAG_ID SERIAL UNIQUE:  This is the primary key of tags table, it is serial; thus, it incremented by one after each entry into table. This enables fast search operation into table.
•	DATE DATE DEFAULT CURRENT_DATE: This column holds the date of the tag is added into tweet and it has a default value. This value is date of adding a new tag.
•	TAG_CATEGORY VARCHAR(100) NOT NULL: This column is for storing the category of tag and it cannot be null. Type of this column is varying character up to 100.
•	TWEET_INPUT VARCHAR(200)  NOT NULL: This column holds tweets whose type is character varying at most 200 character. It is cannot have a null value. 
•	TAG_INPUT VARCHAR(100) UNIQUE NOT NULL: This column holds tags whose type is character varying at most 200 character. It is unique and cannot have a null value.
Constraints of Table:
•	FOREIGN KEY(TWEET_INPUT) REFERENCES IN TWEETS(TWEET_INPUT) ON DELETE CASCADE ON UPDATE CASCADE: tweet_input column has a foreign key by having a relationship with tweet_input column on tweets table. When there is a deletion or updating operation on tweets, if there is a row in tags table with same tweet_input, it will also be deleted or updated.


Methods of Tags Class:

  There are 5 main method to insert, select, update and delete operations on tags table. The structures of Python and HTML codes are explained on below.

•	INSERT METHOD: savetag() -> This method is written for insert operation for tags table. Due to foreign key constraint of tags table, there is an exception for this method by using “try and catch” object oriented approach. Python and SQL code for  this method is showed as below.

.. code-block:: python


  class tags:
    def savetag(config):
        tweet_input = None
        new_category = None
        new_tag = None
        if request.method == 'POST':
            tweet_input = request.form['tweetinput_text']
            print(tweet_input)
            new_category = request.form['category_text']
            print(new_category)
            new_tag = request.form['tag_text']
            print(new_tag)
            with dbapi2.connect(config) as connection:
                cursor = connection.cursor()
                try:
                    query = """INSERT INTO TAGS(tweet_input, tag_input ,tag_category) VALUES (%s, %s, %s)"""
                    cursor.execute(query, (tweet_input, new_tag, new_category))
                    connection.commit();
                    return 'Your tag has been successfully posted <a href="http://localhost:5000">Home</a>'
                except:
                    return 'Your tag cannot be added due to foreign key constraints! <a href="http://localhost:5000">Home</a>'
                    
  
There is no need to insert a value for tag_id column due to its serial property. By executing this query and commiting it, new row is inserted with columns taken from user.

This method is called in savetag() function on server.py

.. code-block:: python

  @app.route('/savettag', methods=['POST'])
  def savetag():
    return tag.savetag(app.config['dsn'])
    
HTML code for adding new tag can be seen in the following method.

.. code-block:: python

  <body>

    <div class="container bg-2 text-center">
  <h3> Please Enter Information About Tag</h3>
    <form class="col-lg-12" action="{{url_for('savetag')}}" method="POST">
    <div class="form-group">
      <label for="name">Tweet Input:</label>
      	  <h4>You can reach tweet from tweet page.</h4>
      	  <li role="presentation" class="active"><a href="{{ url_for('tweets') }}">Tweets</a></li>
       <input class="form-control" id="tweetinput_text" name="tweetinput_text" type="text">
    </div>
        <div class="form-group">
      <label for="category">Tag:</label>
       <input class="form-control" name="tag_text" id="tag_text" type="text">
    </div>
        <div class="form-group">
      <label for="category">Tag Category:</label>
       <input class="form-control" name="category_text" id="category_text" type="text">
    </div>

   <button type="submit" id="btn_sign" class="btn btn-default">Save</button>
   </form>

  <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.12.4/jquery.min.js"></script>
  <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js"></script>
    <!-- IE10 viewport hack for Surface/desktop Windows 8 bug -->

  </body>
  
  
    
In this format, there are 3 text boxes in order to take values from user and bootstrap were used.
  
  

• SELECT METHOD:	tags_db() -> This medhod was written in order to display all tags for all tweets on tag panel page by using “SELECT” query. This query can be seen as follow in SQL and this query is executed in the following Python code. It takes a config as a parameter due to connecting database and it returns tags.html page.

.. code-block:: python

      def tags_db(config):
        with dbapi2.connect(config) as connection:
            if request.method == 'GET':
                cursor = connection.cursor()
                query = "SELECT DISTINCT user_logname, tags.tweet_input,tag_input ,tag_category, tags.date from TAGS , TWEETS where                       tags.tweet_input = tweets.tweet_input"
                cursor.execute(query)
                connection.commit();
                return render_template('tags.html', tag_list=cursor)



This query displays all rows on tags table by order username, tag, tweet, category of a tag and date. There is a join with tweets table here in order to take user_logname from tweets table with tweet_input.

This method of tags class is called in tags() function on server.py

.. code-block:: python 
  @app.route('/tags')
  def tags():
    return tag.tags_db(app.config['dsn'])
    
This function provides to display all rows in tags table on tags.html page. This html is showed as follow.

.. code-block:: python

  <body>
    <div class="container">
        <h2>TAG PANEL</h2>
      <div class="header clearfix">
        <nav>
          <ul class="nav nav-pills pull-right">
           <li role="presentation" class="active"><a href="{{ url_for('home_page') }}">Home</a></li>
           <li role="presentation" class="active"><a href="{{ url_for('tags_edit') }}">Add a New Tag</a></li>

          </ul>
        </nav>
      </div>

   <form action="{{ url_for('tags') }}" method = "post">
  <table id="tagsTable" class="table">
	 <thead>
      <tr>
       <th>User Name</th>
        <th>Tweet</th>
        <th>Tag</th>
        <th>Tag Category</th>
        <th>Date</th>
      </tr>
    </thead>
	<tbody>
		{% for user_logname, tweet_input, tag_input, tag_category, date in tag_list %}
		<tr>
			<td class="TagsTableItem">{{user_logname}}</td>
			<td class="TagsTableItem">{{tweet_input}}</td>
			<td class="TagsTableItem">{{tag_input}}</td>
			<td class="TagsTableItem">{{tag_category}}</td>
			<td class="TagsTableItem">{{date}}</td>
			<td class="TagsTableItem"><a href="{{ url_for('tag_delete', deletetag=tag_input) }}">Delete</a>
			<td class="TagsTableItem"><a href="{{ url_for('tag_update', updatetag=tag_input) }}">Update</a>
		</tr>
		{% endfor %}
		</tbody>
	</table>

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
  
  
• DELETE METHOD: tags_db_delete -> This method is written in order to make delete operation on tags table. It takes a config to connect database and tag value that will be deleted as parameters. Written SQL query and Python function can be seen as follow for this operation. Due to the fact that “cascade” is used on deletion operation, there is no need to make exception.

.. code-block:: python

      def tags_db_delete(config, deletetag):
        with dbapi2.connect(config) as connection:
            cursor = connection.cursor()
            query = "DELETE FROM tags where tag_input = %s"
            cursor.execute(query, (deletetag,))
            connection.commit();
            return redirect(url_for('tags'))

The delete operation is made by taking tag value from user and comparing it to any row on tags table.

tags_db_delete() function of tags class is called in tag_delete() function on server.py

.. code-block:: python 
  @app.route('/tags/delete/<deletetag>', methods=['GET', 'POST'])
  def tag_delete(deletetag):
    return tag.tags_db_delete(app.config['dsn'],deletetag)
    
• UPDATE METHODS:
    
• tags_db_update() -> This method is written for finding with tags that is taken from user. All search operations are made with tag input. This method returns tags_update.html in order to complete update operation.



•	tags_db_update_apply() -> This method is written in order to make update operation. It takes config and username from user as parameters and executes the following query ,new tag input is taken from user by HTML code. Due to the fact that “cascade” is used on update operation, there is no need to make exception.

.. code-block:: python

    def tags_db_update(config, updatetag):
        with dbapi2.connect(config) as connection:
            cursor = connection.cursor()
            query = """SELECT tag_input from tags where tag_input='%s'""" % (updatetag)
            cursor.execute(query)
            connection.commit();
            return render_template('tags_update.html', tag_updates=cursor)


    def tags_db_update_apply(config, updatetag):
        with dbapi2.connect(config) as connection:
            cursor = connection.cursor()
            try:
                new_tag = request.form['tag']
                query = """UPDATE tags set tag_input ='%s' where tag_input = '%s'""" % (new_tag, updatetag)
                cursor.execute(query)
                connection.commit();
                return redirect(url_for('tags'))
            except:
                return 'Value cannot be NULL! <a href="http://localhost:5000">Home</a>'

These methods are called in tag_update and tags_apply functions on server.py

.. code-block:: python

  @app.route('/tags/update/<updatetag>/', methods=['GET', 'POST'])
  def tag_update(updatetag):
    return tag.tags_db_update(app.config['dsn'],updatetag)

  @app.route('/tags/update/<updatetag>/apply', methods=['GET', 'POST'])
  def tags_apply(updatetag):
    return tag.tags_db_update_apply(app.config['dsn'],updatetag)
    
HTML code for update operation can be seen in the following code block. There is a text box for getting new tag value from user as it is seen.

.. code-block:: python

    <body>
    <div class="container">
        <h2>UPDATE TAG</h2>
      <div class="header clearfix">
        <nav>
          <ul class="nav nav-pills pull-right">
           <li role="presentation" class="active"><a href="{{ url_for('home_page') }}">Home</a></li>
          </ul>
        </nav>
      </div>

  <form action="apply" method = "post">
  <table id="tagEditTable" class="table" width="500px">
	 <thead>
      <tr>
		<th>User Tag</th>
      </tr>
    </thead>
	<tbody>
    {% for tag_input in tag_updates %}
    <td><input type="text" name="tag" required="required" value="{{tag_input[0]}}" style="width:95%"></td>
    {% endfor %}
    <tr>
			<td colspan="3" align="center"><input value="Update Tag" name="add" type="submit"></td>
	</tr>
	</tbody>
	</table>

    </div> <!-- /container -->

  <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.12.4/jquery.min.js"></script>
  <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js"></script>
    <!-- IE10 viewport hack for Surface/desktop Windows 8 bug -->
  </body>
  
  
  
3.	Comments Class:

This class was created on comments.py Python file and it also includes 5 main methods to make basic database operation for comments table. There are 3 main HTML files were and these are, comments.html, comments_edit.html and comments_update.html pages.

Comments Table:
•	COMMENT_ID SERIAL UNIQUE: This is the primary key of comments table, it is serial; thus, it incremented by one after each entry into table. This enables fast search operation into table.
•	DATE DATE DEFAULT CURRENT_DATE: This column holds the date of the comment is added into tweet and it has a default value. This value is date of adding a new comment.
•	TWEET_INPUT VARCHAR(200)  NOT NULL: This column holds tweets whose type is character varying at most 200 character. It is cannot have a null value. 
•	COMMENT VARCHAR(200) NOT NULL: This column holds comments whose type is character varying at most 200 character. It is cannot have a null value.
•	USER_LOGNAME VARCHAR(60) NOT NULL: This column stores username of a user and it cannot have a null value. Type of this column is varying character up to 60.

Constraints of Table:

There are two foreign key on this table.


•	FOREIGN KEY(TWEET_INPUT) REFERENCES IN TWEETS(TWEET_INPUT) ON DELETE CASCADE ON UPDATE CASCADE  tweet_input column has a foreign key by having a relationship with tweet_input column on tweets table. When there is a deletion or updating operation on tweets, if there is a row in comments table with same tweet_input, it will also be deleted or updated.
•	FOREIGN KEY(USER_LOGNAME) REFERENCES IN USER_LOGIN(USER_LOGINNAME) ON DELETE CASCADE ON UPDATE CASCADE  user_logname column has a foreign key by having a relationship with user_loginname column in user_login table. When there is a deletion or updating operation on user_login table, if there is a row in comments table with same username ,it will also be deleted or updated.

Methods of Comments Class:
There are 5 main method to insert, select, update and delete operations on tags table. Python and HTML codes are explaind; also, in this part, SQL codes for comments and the aim of methods were shared.

•	INSERT METHOD: savecomment() -> This method makes insert operation for comments table. Due to foreign key constraint of comments table, there is an exception for this method by using “try and catch” object oriented approach. SQL query and Python code for this method are showed as below.

.. code-block:: python

  class comments:

    def savecomment(config):
        tweet_input = None
        user_logname = None
        comment = None
        if request.method == 'POST':
            tweet_input = request.form['tweetinput_text']
            print(tweet_input)
            user_logname = request.form['userlogname_text']
            print(user_logname)
            comment = request.form['comment_text']
            print(comment)
            with dbapi2.connect(config) as connection:
                cursor = connection.cursor()
                try:
                    query = """INSERT INTO comments (tweet_input, comment, user_logname) VALUES (%s, %s, %s)"""
                    cursor.execute(query, (tweet_input, comment , user_logname))
                    connection.commit();
                    return 'Your comment has been successfully posted <a href="http://localhost:5000">Home</a>'
                except:
                    return 'Your comment cannot be added due to foreign key constraints! <a href="http://localhost:5000">Home</a>'

This method is called in savecomment() function on server.py with the following approute.

.. code-block:: python

  @app.route('/savecomment', methods=['POST'])
  def savecomment():
    return comment.savecomment(app.config['dsn'])
    
To get values for comments from admin user, following HTML code is written. There are 3 text box for these values.

.. code-block:: python 

    <body>

    <div class="container bg-2 text-center">
  <h3> Please Enter Comment Information</h3>
    <form class="col-lg-12" action="{{url_for('savecomment')}}" method="POST">

	<div class="form-group">
      <label for="category">User Name:</label>
      <input class="form-control" name="userlogname_text" id="userlogname_text" type="text">
    </div>

    <div class="form-group">
      <label for="name">Tweet:</label>
	  <h4>You can reach tweet from tweet page.</h4>            <li role="presentation" class="active"><a href="{{ url_for('tweets') }}">Tweets</a></li>
       <input class="form-control" id="tweetinput_text" name="tweetinput_text" type="text">
    </div>


    <div class="form-group">
      <label for="tweet">Comment for Tweet:</label>
      <input class="form-control" name="comment_text" id="comment_text" type="text">
    </div>

   <button type="submit" id="btn_sign" class="btn btn-default">Save</button>
   </form>

  <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.12.4/jquery.min.js"></script>
  <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js"></script>
    <!-- IE10 viewport hack for Surface/desktop Windows 8 bug -->

  </body>
    
•	SELECT METHOD: comments_db() -> This method represents all comments for all tweets on comments.html page by using “SELECT” query. This query can be seen as follow in SQL. 

.. code-block:: python
    def comments_db(config):
        with dbapi2.connect(config) as connection:
            if request.method == 'GET':
                cursor = connection.cursor()
                query = "SELECT DISTINCT user_logname, tweet_input, comment  from COMMENTS"
                cursor.execute(query)
                connection.commit();
                return render_template('comments.html', comments_list=cursor)

This select query displays all rows on comments table and this method is called in comments() function on server.py

.. code-block:: python 
  @app.route('/comments')
  def comments():
    return comment.comments_db(app.config['dsn'])
    
 
In order to achieve to display all comments in comment table into comments.html, following html was written and for loop is used.

.. code-block:: python

  <body>
    <div class="container">
        <h2>COMMENT PANEL</h2>
      <div class="header clearfix">
        <nav>
          <ul class="nav nav-pills pull-right">
           <li role="presentation" class="active"><a href="{{ url_for('home_page') }}">Home</a></li>
		   <li role="presentation" class="active"><a href="{{ url_for('activities_panel') }}">Activities Panel</a></li>
           <li role="presentation" class="active"><a href="{{ url_for('comments_edit') }}">Add a New Comment</a></li>

          </ul>
        </nav>
      </div>

   <form action="{{ url_for('comments')}}" method = "post">
  <table id="CommentsTable" class="table">
	 <thead>
      <tr>
        <th>User Login Name</th>
        <th>Tweet</th>
        <th>Comment</th>
      </tr>
    </thead>
	<tbody>
		{% for user_logname, tweet_input, comment in comments_list %}
		<tr>
			<td class="CommentsTableItem">{{user_logname}}</td>
			<td class="CommentsTableItem">{{tweet_input}}</td>
			<td class="CommentsTableItem">{{comment}}</td>
			<td class="CommentsTableItem"><a href="{{ url_for('comments_delete', deletecomment=user_logname) }}">Delete</a>
			<td class="CommentsTableItem"><a href="{{ url_for('comments_update', updatecomment=user_logname) }}">Update</a>
		</tr>
		{% endfor %}
		</tbody>
	</table>

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
  

•	DELETE METHOD: comments_db_delete() -> This method is kaing delete operation on comments table. Written SQL query can be seen as follow for this operation. Due to the fact that “cascade” is used on deletion operation, there is no need to make exception. Deletion operation is made by comparing user_logname column by user’s choice.

.. code-block:: python

    def comments_db_delete(config, deletecomment):
        with dbapi2.connect(config) as connection:
            cursor = connection.cursor()
            query = "DELETE FROM COMMENTS where user_logname = %s"
            cursor.execute(query, (deletecomment,))
            connection.commit();
            return redirect(url_for('comments'))
            
This method is called comments_delete() function on server as follow.

.. code-block:: python 

  @app.route('/comments/delete/<deletecomment>', methods=['GET', 'POST'])
  def comments_delete(deletecomment):
    return comment.comments_db_delete(app.config['dsn'],deletecomment)


• UPDATE METHODS:

•	comments_db_update() -> Th is written for searching with user_logname that is taken from user. This method returns comments_update.html in order to complete update operation.

•	comments_db_update_apply() -> This method is written in order to make update operation. New comment is taken from user by HTML code and giving as a parameter to this method. Due to the fact that “cascade” is used on update operation, there is no need to make exception.

.. code-block:: python

    def comments_db_update(config, updatecomment):
        with dbapi2.connect(config) as connection:
            cursor = connection.cursor()
            query = """SELECT comment from comments where user_logname = '%s'""" % (updatecomment)
            cursor.execute(query)
            connection.commit();
            return render_template('comments_update.html', comment_updates=cursor)


    def comments_db_update_apply(config, updatecomment):
        with dbapi2.connect(config) as connection:
            cursor = connection.cursor()
            try:
                comment = request.form['comment_txt']
                query = """UPDATE comments set comment ='%s' where user_logname = '%s'""" % (comment, updatecomment)
                cursor.execute(query)
                connection.commit();
                return redirect(url_for('comments'))
            except:
                return 'Value cannot be NULL! <a href="http://localhost:5000">Home</a>'
                
These functions are called on server.py with the following approutes.

.. code-block:: python

  @app.route('/comments/update/<updatecomment>/', methods=['GET', 'POST'])
  def comments_update(updatecomment):
    return comment.comments_db_update(app.config['dsn'],updatecomment)

  @app.route('/comments/update/<updatecomment>/apply', methods=['GET', 'POST'])
  def comments_apply(updatecomment):
    return comment.comments_db_update_apply(app.config['dsn'],updatecomment)
    
To make update operation, new comment value should be got from user; therefore, a box is put into comments_update.html page and following html is written.

.. code-block:: python

  <body>
    <div class="container">
        <h2>UPDATE COMMENTeader clearfix">
        <nav>
          <ul class="nav nav-pills pull-right">
           <li role="presentation" class="active"><a href="{{ url_for('home_page') }}">Home</a></li>
          </ul>
        </nav>
      </div>

  <form action="apply" method = "post">
  <table id="commentEditTable" class="table" width="500px">
	 <thead>
      <tr>
		<th>User Comment</th>
      </tr>
    </thead>
	<tbody>
    {% for comment in comment_updates %}
    <td><input type="text" name="comment_txt" required="required" value="{{comment[0]}}" style="width:95%"></td>
    {% endfor %}
    <tr>
			<td colspan="3" align="center"><input value="Update Comment" name="add" type="submit"></td>
	</tr>
	</tbody>
	</table>

    </div> <!-- /container -->

  <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.12.4/jquery.min.js"></script>
  <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js"></script>
    <!-- IE10 viewport hack for Surface/desktop Windows 8 bug -->
  </body>
  
  4.	Directmessages Class:
This class was created on directmessages.py Python file and there are 5 methods in this class to make database operations. There are 3 main HTML files were and these are, directmessages.html, directmessages_edit.html and directmessages_update.html pages.
Directmessages Table:
•	DM_ID SERIAL UNIQUE     This is the primary key of directmessages table, it is serial; thus, it incremented by one after each entry into table. This enables fast search operation into table.
•	DATE DATE DEFAULT CURRENT_DATE  This column holds the date of the sending direct message and it has a default value by current date.
•	MESSAGE VARCHAR(200)  NOT NULL  This column holds directmessages whose type is character varying at most 200 character. It cannot have a null value. 
•	SUBJECT VARCHAR(100) NOT NULL  This column holds subjects of messages whose type is character varying at most 100 character. It cannot have a null value.
•	USER_LOGNAME1 VARCHAR(60) NOT NULL  This column stores username of a user and it cannot have a null value. Type of this column is varying character up to 60.
•	USER_LOGNAME2 VARCHAR(60) NOT NULL  This column stores username of a user and it cannot have a null value. Type of this column is varying character up to 60.

Constraints of Table:
There are two foreign key on this table.
•	FOREIGN KEY(USER_LOGNAME1) REFERENCES IN USER_LOGIN(USER_LOGINNAME) ON DELETE CASCADE ON UPDATE CASCADE  When there is a deletion or updating operation on user_login table, if there is a row in comments table with same username ,it will also be deleted or updated because user_logname1 column has a foreign key by having a relationship with user_loginname column in user_login table. 
•	FOREIGN KEY(USER_LOGNAME2) REFERENCES IN USER_LOGIN(USER_LOGINNAME) ON DELETE CASCADE ON UPDATE CASCADE  user_logname2 column has a foreign key by having a relationship with user_loginname column in user_login table. When there is a deletion or updating operation on user_login table, if there is a row in comments table with same username ,it will also be deleted or updated.

Methods of Directmessages Class:
Python and HTML codes are again similar to tweets entity except SQL codes; therefore, SQL queries and Python codes were showed on below for 5 methods in this class.
•	INSERT METHOD: savedirectmessage() -> This method makes insert operation for comments table with following query. Due to foreign key constraint of directmessages table, there is an exception for this method by using “try and catch” object oriented approach. user_logname1 and user_logname2 must be on user_login table.

.. code-block:: python

  class directmessages:
    def savedirectmessage(config):
        user_logname1 = None
        user_logname2 = None
        message = None
        subject = None
        if request.method == 'POST':
            user_logname1 = request.form['senderlogname_text']
            print(user_logname1)
            user_logname2 = request.form['receiverlogname_text']
            print(user_logname2)
            message = request.form['message_text']
            print(message)
            subject = request.form['subject_text']
            print(subject)
            with dbapi2.connect(config) as connection:
                cursor = connection.cursor()
                try:
                    query = """INSERT INTO DIRECTMESSAGES (user_logname1, user_logname2, message, subject) VALUES (%s, %s, %s, %s)"""
                    cursor.execute(query, (user_logname1, user_logname2, message, subject))
                    connection.commit();
                    return 'Your message has been successfully posted <a href="http://localhost:5000">Home</a>'
                except:
                    return 'Your message cannot be added due to foreign key constraints! <a href="http://localhost:5000">Home</a>'
                    
This method is called on server.py as below.

.. code-block:: python

 @app.route('/savedirectmessage', methods=['POST'])
  def savedirectmessage():
    return directmessage.savedirectmessage(app.config['dsn'])
    
•	SELECT METHOD: directmessages_db -> This method represents all rows of directmessages table on direcmessages.html page by using “SELECT” query. This query can be seen as follow in SQL. 

.. code-block:: python

    def directmessages_db(config):
        with dbapi2.connect(config) as connection:
            if request.method == 'GET':
                cursor = connection.cursor()
                query = "SELECT DISTINCT user_logname1, user_logname2,message ,subject, date from DIRECTMESSAGES"
                cursor.execute(query)
                connection.commit();
                return render_template('directmessages.html', directmessages_list=cursor)
                
This method is called on server.py in directmessages() function.

.. code-block:: python

  @app.route('/directmessages')
  def directmessages():
    return directmessage.directmessages_db(app.config['dsn'])


•	DELETE METHOD: directmessages_db_delete() -> This method is for delete operation on directmessages table by using following delete query. Due to the fact that “cascade” is used on deletion operation, there is no need to make exception. 

.. code-block:: python

    def directmessages_db_delete(config, deletedm):
        with dbapi2.connect(config) as connection:
            cursor = connection.cursor()
            query = "DELETE FROM DIRECTMESSAGES where user_logname1 = %s"
            cursor.execute(query, (deletedm,))
            connection.commit();
            return redirect(url_for('directmessages'))
            
This method is called on server.py as follow.

.. code-block:: python
  @app.route('/directmessages/delete/<deletedm>', methods=['GET', 'POST'])
  def directmessages_delete(deletedm):
    return directmessage.directmessages_db_delete(app.config['dsn'],deletedm)
    

• UPDATE METHODS:

•	directmessages_db_update -> Searching with user_logname1 that is taken from user can be made with this method. This method returns directmessages_update.html in order to complete update operation.

•	directmessages_db_update_apply() -> This method is written in order to make update operation. Message can be updated by taking new message from admin. Due to the fact that “cascade” is used on update operation, there is no need to make exception.

.. code-block:: python
    def directmessages_db_update(config, updatetag):
        with dbapi2.connect(config) as connection:
            cursor = connection.cursor()
            query = """SELECT message from directmessages where user_logname1 = '%s'""" % (updatetag)
            cursor.execute(query)
            connection.commit();
            return render_template('directmessages_update.html', directmessage_updates=cursor)


    def directmessages_db_update_apply(config, updatedm):
        with dbapi2.connect(config) as connection:
            cursor = connection.cursor()
            try:
                message = request.form['directmessage']
                query = """UPDATE directmessages set message ='%s' where user_logname1 = '%s'""" % (message, updatedm)
                cursor.execute(query)
                connection.commit();
                return redirect(url_for('directmessages'))
            except:
                return 'Value cannot be NULL! <a href="http://localhost:5000">Home</a>'

In order to make these operation, these methods are called on server.py

.. code-block:: python

  @app.route('/directmessages/update/<updatedm>/', methods=['GET', 'POST'])
  def directmessages_update(updatedm):
    return directmessage.directmessages_db_update(app.config['dsn'],updatedm)

  @app.route('/directmessages/update/<updatedm>/apply', methods=['GET', 'POST'])
  def directmessage_apply(updatedm):
    return directmessage.directmessages_db_update_apply(app.config['dsn'],updatedm)
    


5.	Activities Class:
This class was created on events.py Python file and there are 3 main HTML files
 events.html, events_edit.html and events_update.html pages.
Activities Table:
•	EVENT_ID SERIAL UNIQUE: This is the primary key of activities table, it is serial; thus, it incremented by one after each entry into table. 
•	EVENT_NAME VARCHAR(200)  UNIQUE NOT NULL: This column holds name of events whose type is character varying at most 200 character. It is unique and cannot have a null value. 
•	EVENT_LOCATION VARCHAR(200) NOT NULL: This column holds locations of events whose type is character varying up to 200 character. It cannot have a null value.
•	EVENT_CATEGORY VARCHAR(200) NOT NULL: This column stores categories of events and it cannot have a null value. Type of this column is varying character up to 200.
•	EVENT_DATE VARCHAR(200) NOT NULL: This column stores date of events and it cannot have a null value. Type of this column is varying character up to 200.

Constraints of Table:

There is no foreign key on this table, this is a core entity.

Methods of Activities Class:

There are 5 main methods in this class in order to make insert, select, update and delete operations, SQL codes were showed on below for these methods in this class.

•	INSERT METHOD: saveevent() -> This method makes insert operation into activities table with following query. There is no need to make an exception because there is no foreign key value on activities table.

.. code-block:: python

  class activities:
    def saveevent(config):
        event_name = None
        event_location = None
        event_date = None
        event_category = None
        if request.method == 'POST':
            event_name = request.form['eventname_text']
            print(event_name)
            event_location = request.form['eventloc_text']
            print(event_location)
            event_date = request.form['eventdate_text']
            print(event_date)
            event_category = request.form['eventcat_text']
            print(event_category)
            with dbapi2.connect(config) as connection:
                cursor = connection.cursor()
                try:
                    query = """INSERT INTO activities(event_name, event_location, event_date, event_category) VALUES (%s, %s, %s, %s)"""
                    cursor.execute(query, (event_name, event_location, event_date, event_category))
                    connection.commit();
                    return 'Your activity has been successfully posted <a href="http://localhost:5000">Home</a>'
                except:
                    return 'Your activity cannot be added due to foreign key constraints! <a href="http://localhost:5000">Home</a

•	SELECT METHOD: events_db() -> This method represents all rows of activities table on events.html page by using  following “SELECT” query. 

.. code-block:: python

    def events_db(config):
        with dbapi2.connect(config) as connection:
            if request.method == 'GET':
                cursor = connection.cursor()
                query = "SELECT DISTINCT event_name, event_location, event_date, event_category  from ACTIVITIES"
                cursor.execute(query)
                connection.commit();
                return render_template('events.html', events_list=cursor)


•	DELETE METHOD: events_db_delete() -> This method is for delete operation on activities table by using following delete query. 

.. code-block:: python

    def events_db_delete(config, deleteevent):
        with dbapi2.connect(config) as connection:
            cursor = connection.cursor()
            query = "DELETE FROM ACTIVITIES where event_name = %s"
            cursor.execute(query, (deleteevent,))
            connection.commit();
            return redirect(url_for('events'))

•	UPDATE METHODS:

•	events_db_update() -> Searching with user_logname1 that is taken from user can be made with this method. This method returns directmessages_update.html in order to complete update operation.

•	events_db_update_apply()  This method is written in order to make update operation. Message can be updated by taking new message from admin. Due to the fact that “cascade” is used on update operation, there is no need to make exception.

.. code-block:: python

    def events_db_update(config, updateevent):
        with dbapi2.connect(config) as connection:
            cursor = connection.cursor()
            query = """SELECT event_name from activities where event_name = '%s'""" % (updateevent)
            cursor.execute(query)
            connection.commit();
            return render_template('events_update.html', events_updates=cursor)


    def events_db_update_apply(config, updateevent):
        with dbapi2.connect(config) as connection:
            cursor = connection.cursor()
            try:
                comment = request.form['event_name']
                query = """UPDATE activities set event_name ='%s' where event_name = '%s'""" % (comment, updateevent)
                cursor.execute(query)
                connection.commit();
                return redirect(url_for('events'))
            except:
                return 'Value cannot be NULL! <a href="http://localhost:5000">Home</a>'
                
These above methods are called on server.py as below.

.. code-block:: python
  @app.route('/events')
  def events():
    return event.events_db(app.config['dsn'])

  @app.route('/events/delete/<deleteevent>', methods=['GET', 'POST'])
  def events_delete(deleteevent):
    return event.events_db_delete(app.config['dsn'],deleteevent)
    
  @app.route('/events/update/<updateevent>/', methods=['GET', 'POST'])
  def events_update(updateevent):
    return event.events_db_update(app.config['dsn'],updateevent)

  @app.route('/events/update/<updateevent>/apply', methods=['GET', 'POST'])
  def events_apply(updateevent):
    return event.events_db_update_apply(app.config['dsn'],updateevent)

  @app.route('/saveevent', methods=['POST'])
  def saveevent():
    return event.saveevent(app.config['dsn'])
    

Following HTML codes were written for mentionde 3 html pages, these pages is for insertion, select and update operations by order.

.. code-block:: python

  <body>

    <div class="container bg-2 text-center">
  <h3> Please Enter Event Information</h3>
    <form class="col-lg-12" action="{{url_for('saveevent')}}" method="POST">

	<div class="form-group">
      <label for="name">Event Name:</label>
      <input class="form-control" name="eventname_text" id="eventname_text" type="text">
    </div>

    <div class="form-group">
      <label for="location">Event Location:</label>
       <input class="form-control" id="eventloc_text" name="eventloc_text" type="text">
    </div>


    <div class="form-group">
      <label for="date">Event Date:</label>
      <input class="form-control" name="eventdate_text" id="eventdate_text" type="text">
    </div>

	<div class="form-group">
      <label for="category">Event Category:</label>
      <input class="form-control" name="eventcat_text" id="eventcat_text" type="text">
    </div>

   <button type="submit" id="btn_sign" class="btn btn-default">Save</button>
   </form>

  <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.12.4/jquery.min.js"></script>
  <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js"></script>
    <!-- IE10 viewport hack for Surface/desktop Windows 8 bug -->

  </body>
  
Here, there are 4 text boxes in order to take columns from user. Texts boxes are for event_name, event_location, event_date and event_category by order.

.. code-block:: python

  <body>
    <div class="container">
        <h2>EVENT PANEL</h2>
      <div class="header clearfix">
        <nav>
          <ul class="nav nav-pills pull-right">
           <li role="presentation" class="active"><a href="{{ url_for('home_page') }}">Home</a></li>
		   <li role="presentation" class="active"><a href="{{ url_for('activities_panel') }}">Activities Panel</a></li>
           <li role="presentation" class="active"><a href="{{ url_for('events_edit') }}">Add a New Event</a></li>

          </ul>
        </nav>
      </div>

   <form action="{{ url_for('events')}}" method = "post">
  <table id="EventsTable" class="table">
	 <thead>
      <tr>
        <th>Event Name</th>
        <th>Event Location</th>
        <th>Event Date</th>
		<th>Event Category</th>
      </tr>
    </thead>
	<tbody>
		{% for event_name, event_location, event_date, event_category in events_list %}
		<tr>
			<td class="EventsTableItem">{{event_name}}</td>
			<td class="EventsTableItem">{{event_location}}</td>
			<td class="EventsTableItem">{{event_date}}</td>
			<td class="EventsTableItem">{{event_category}}</td>
			<td class="EventsTableItem"><a href="{{ url_for('events_delete', deleteevent=event_name) }}">Delete</a>
			<td class="EventsTableItem"><a href="{{ url_for('events_update', updateevent=event_name) }}">Update</a>
		</tr>
		{% endfor %}
		</tbody>
	</table>

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



    </div> <!-- /container -->

  <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.12.4/jquery.min.js"></script>
  <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js"></script>
    <!-- IE10 viewport hack for Surface/desktop Windows 8 bug -->
  </body>
  
Bootstrap is used on this html and by using for loop on activities table with cursor, all rows are displayed on events.html.

.. code-block:: python

  <body>
    <div class="container">
        <h2>EVENT PANEL</h2>
      <div class="header clearfix">
        <nav>
          <ul class="nav nav-pills pull-right">
           <li role="presentation" class="active"><a href="{{ url_for('home_page') }}">Home</a></li>
          </ul>
        </nav>
      </div>

  <form action="apply" method = "post">
  <table id="EventEditTable" class="table" width="500px">
	 <thead>
      <tr>
		<th>Event Name</th>
      </tr>
    </thead>
	<tbody>
    {% for event_name in events_updates %}
    <td><input type="text" name="event_name" required="required" value="{{event_name[0]}}" style="width:95%"></td>
    {% endfor %}
    <tr>
			<td colspan="3" align="center"><input value="Update Event Name" name="add" type="submit"></td>
	</tr>
	</tbody>
	</table>

    </div> <!-- /container -->

  <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.12.4/jquery.min.js"></script>
  <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js"></script>
    <!-- IE10 viewport hack for Surface/desktop Windows 8 bug -->
  </body>
  
  
Here, again for loop is used for updating rows and if there is a match by select query, a text box is put and this is for getting up-to-date event name from user.





    
    



    
    
















  






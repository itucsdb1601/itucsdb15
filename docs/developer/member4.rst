Parts Implemented by Melis Gülenay
================================


Favorites page involves 5 tables. In order to creation of database, the route http://localhost:5000/favorites/initialize_favorites should be visited. All the tables are firstly dropped then created again when this route is worked. Tables are going to explained in parts.

Part 1 – Favorite Users
This table consists of five attitudes. As seen in the following code these are user_logname1, user_logname2, date, and relation.

.. code-block:: python

    def initialize_favorites(config):
        with dbapi2.connect(config) as connection:
            cursor = connection.cursor()
            query = """DROP TABLE IF EXISTS FAVORITESUSERS CASCADE;"""
            cursor.execute(query)
            query = """CREATE TABLE IF NOT EXISTS FAVORITEUSERS(
            favorite_id serial,
            user_logname1 VARCHAR(60) not null,
            user_logname2 VARCHAR(60) not null,
            date date DEFAULT current_date,
            relation VARCHAR(100) not null,
            primary key(favorite_id, user_logname1),
            foreign key(user_logname1) references user_login(user_loginname) on delete cascade on update cascade,
            foreign key(user_logname2) references user_login(user_loginname) on delete cascade on update cascade
            )
            """
            
User_logname1  and user_logname2 have a foreign key relation with the table user_login on attitude user_loginname. Delete and update operations are defined as cascade. 
	When the user enters to the favorite user page pyhthon code in figure 3.2.4.1.2 starts to work.

.. code-block:: python

    def favorites_db(config):
        with dbapi2.connect(config) as connection:
            if request.method == 'GET':
                cursor = connection.cursor()
                query="SELECT user_logname1,user_logname2,date, relation from favoriteusers"
                cursor.execute(query)
                print(cursor)
                return render_template('favorites.html', favorites_list=cursor)
                
                
                
This code is used to show all the favoriteusers’ tuples on the table on favorites.html. 

.. code-block:: python

    def favorites_db_delete(config,deletefavorites):
        with dbapi2.connect(config) as connection:
            cursor = connection.cursor()
            query="DELETE FROM favoriteusers where user_logname1 = %s"
            cursor.execute(query, (deletefavorites,))
            connection.commit()
            return redirect(url_for('favorites'))
            
For the delete operation, selection is done according to user_logname1  and the button which is supplied by html is connected for delete operation.            
  
.. code-block:: python
  
	<tbody>
		{% for user_logname1, user_logname2, date, relation in favorites_list %}
		<tr>
			<td class="FavoritesTableItem">{{user_logname1}}</td>
			<td class="FavoritesTableItem">{{user_logname2}}</td>
			<td class="FavoritesTableItem">{{date}}</td>
			<td class="FavoritesTableItem">{{relation}}</td>
			<td class="FavoritesTableItem"><a href="{{ url_for('favorites_delete', deletefavorites=user_logname1) }}">Delete</a>
			<td class="FavoritesTableItem"><a href="{{ url_for('favorites_update', updatefavorites=user_logname1) }}">Update</a>
		</tr>
		{% endfor %}
		</tbody>            
            
For update operation, firstly user has to pressed the update button. The selection operation is applied with the user_logname1. Then, update page comes to the screen. In this page, the value that will be updated is printed to the input box with the code             
            
.. code-block:: python

    def favorites_db_update(config,updatefavorites):
        with dbapi2.connect(config) as connection:
            cursor = connection.cursor()
            query="""SELECT relation from favoriteusers where user_logname1 = '%s'""" % (updatefavorites)
            cursor.execute(query)
            connection.commit()
            return render_template('favorites_update.html',favorites_updates=cursor)


After the user enters the new value, the following code in the figure 3.2.4.1.6 works and the old relation value is updated. Try – except controls the whether the entered value is null or not. If it is null the update operation is not done.
            
.. code-block:: python            
            
       def favorites_db_update_apply(config,updatefavorites):
        with dbapi2.connect(config) as connection:
            cursor = connection.cursor()
            try:
                new_name = request.form['favorites']
                print(new_name)
                query="""UPDATE favoriteusers set relation ='%s' where user_logname1 = '%s'""" % (new_name,updatefavorites)
                cursor.execute(query)
                connection.commit()
                return redirect(url_for('favorites'))
            except:
                return 'Value cannot be NULL! <a href="http://localhost:5000">Home</a>'         
            
The input is taken from the favorites_update.html. The part of this page which is shown in the figure 3.2.4.1.7 takes the input then assigns it to the column relation.            
            
            
.. code-block:: python            
            
    <div class="container bg-2 text-center">
  <h3>Please Enter Information</h3>
    <form class="col-lg-12" action="{{url_for('savefavorites')}}" method="POST">
    <div class="form-group">
      <label for="name">Username:</label>
       <input class="form-control" id="fname_text" name="fname_text" type="text">
    </div>
    <div class="form-group">
      <label for="surname">Username to be favorite:</label>
       <input class="form-control" name="fsurname_text" id="fsurname_text" type="text">
    </div>
    <div class="form-group">
      <label for="username">Relation:</label>
      <input type="text" class="form-control" name="floginname_text"  id="floginname_text">
    </div>
   <button type="submit" id="btn_sign" class="btn btn-default">Enter</button>
  </form>            
            
In order to add new favorite user, user enters the favorites_edit.html via new user favorite button. In this page there are 4 text boxes in order to get the relevant values. The save operation is done with the code in figure 3.2.4.1.8.           
            
.. code-block:: python         

    def saveFavoriteUser(config):
        user_logname1 = None
        user_logname2 = None
        relation = None
        if request.method == 'POST':
            user_logname1= request.form['fname_text']
            print(user_logname1)
            user_logname2 = request.form['fsurname_text']
            print(user_logname2)
            relation = request.form['floginname_text']
            print(relation)
            with dbapi2.connect(config) as connection:
                cursor = connection.cursor()
                try:
                    query = """INSERT INTO FAVORITEUSERS(user_logname1,user_logname2,relation) VALUES (%s,%s,%s);"""
                    cursor.execute(query,(user_logname1,user_logname2,relation))
                    connection.commit();
                    return 'Favorite user information is inserted <a href="http://localhost:5000">Home</a>'
                except:
                    return  'The users do not exist in User_Login Table or values cannot be NULL! <a href="http://localhost:5000">Home</a> '


As favoriteuser table has foreign key relation with the user_login table, there is a control. If admin tries to add a person that does not exist in user_login table, exception return works.

Part 2 – Favorite Universities

There are 4 columns in the favoriteunis table. This table is relevant with the favorite universities page. Figure 3.2.4.2.1. is the creation of this table on database. 

.. code-block:: python 

            query = """DROP TABLE IF EXISTS FAVORITESUNIS CASCADE;"""
            cursor.execute(query)

            query = """CREATE TABLE IF NOT EXISTS FAVORITEUNIS (
            uni_name VARCHAR(80)  NOT NULL,
            favoriteuni_id serial unique,
            fav_department VARCHAR(100) not null,
            user_logname VARCHAR(60) not null,
            primary key(favoriteuni_id),
            foreign key(user_logname) references user_login(user_loginname) on delete cascade on update cascade,
            foreign key(uni_name) references UNIVERSITYLIST(uni_name) on delete cascade on update cascade)
            """
            
Column user_logname has foreign key relation with the user_loginname column from user_login table. Also, uni_name column has foreign key relation with the universitylist table via uni_name column. All delete and update operations are restricted as cascade. Therefore, any changes on the user_login and universitylist tables will affact this table.
When the user enters to the favorite universities page. The table that is explained in the html code in figure 3.2.4.2.3.  shows the user all the rows of favoriteunis table. 
            
.. code-block:: python

	<tbody>
		{% for user_logname, uni_name, fav_department in favoriteUni_list %}
		<tr>
			<td class="FavoritesTableItem">{{user_logname}}</td>
			<td class="FavoritesTableItem">{{uni_name}}</td>
			<td class="FavoritesTableItem">{{fav_department}}</td>
			<td class="FavoritesTableItem"><a href="{{ url_for('favoriteUni_delete', deletefavoriteUni=user_logname) }}">Delete</a>
			<td class="FavoritesTableItem"><a href="{{ url_for('favoriteUni_update', updatefavoriteUni=user_logname) }}">Update</a>
		</tr>
		{% endfor %}
		</tbody>
    
    
Also there are links for delete and update operations on this table. In order to print all the rows of table, the code in the figure  3.2.4.2.4 works. Selection operation is done with this code. 

.. code-block:: python

        def favoriteUnis_db(config):
        with dbapi2.connect(config) as connection:
            if request.method == 'GET':
                cursor = connection.cursor()
                query = """SELECT DISTINCT favoriteunis.user_logname, favoriteunis.uni_name, fav_department from FAVORITEUNIS, UNIVERSITYLIST where favoriteunis.uni_name=universitylist.uni_name"""
                cursor.execute(query)
                connection.commit();
                return render_template('favoriteUnis.html', favoriteUni_list=cursor)

            
For inserting a new favorite university, user presses to the button called as new university favorite. This button is connected to html code favoriteUnis_edit.htm. There three text boxes in this page to get the necessary inputs from the user (Figure 3.2.4.2.5).            
        
.. code-block:: python        
   
    <body>
	<h2>Add new favorite university and department</h2>
    <div class="container bg-2 text-center">
  <h3>Please Enter Information</h3>
    <form class="col-lg-12" action="{{url_for('savefavoriteUni')}}" method="POST">
    <div class="form-group">
      <label for="name">User Name:</label>
       <input class="form-control" id="floginname_text" name="floginname_text" type="text">
    </div>
    <div class="form-group">
      <label for="surname">University Name:</label>
       <input class="form-control" name="uni_text" id="uni_text" type="text">
    </div>
    <div class="form-group">
      <label for="username">Department:</label>
      <input type="text" class="form-control" name="department_text"  id="department_text">
    </div>
   <button type="submit" id="btn_sign" class="btn btn-default">Save</button>
  </form>
            
When the user clicks the submit button the following code compiled.            
 
.. code-block:: python 

    def savefavoriteUni(config):
        uni_name = None
        fav_department = None
        user_logname = None
        if request.method == 'POST':
            uni_name = request.form['uni_text']
            print(uni_name)
            user_logname = request.form['floginname_text']
            print(user_logname)
            fav_department = request.form['department_text']
            print(fav_department)
            with dbapi2.connect(config) as connection:
                cursor = connection.cursor()
                try:
                    query = """INSERT INTO favoriteunis(uni_name, fav_department, user_logname) VALUES (%s, %s, %s)"""
                    cursor.execute(query, (uni_name, fav_department, user_logname))
                    connection.commit();
                    return 'Your favorite university has been successfully posted <a href="http://localhost:5000">Home</a>'
                except:
                    return 'Your favorite university cannot be added due to foreign key constraints! <a href="http://localhost:5000">Home</a>'
            
In the code in Figure 3.2.4.2.5, values are checked whether they are appropriate with the connected tables or not (user_login, universitylist). If they are not, there is an error message. 
For the update operation, selection is done according to user_logname.  The column fav_department that belongs to chosen user_logname is updated. In the favoriteUnis_update.html, the fav_department that will be updated is come to the text box (Figure 3.2.4.2.6).

.. code-block:: python

    def favoriteUnis_db_update(config, updatefavoriteUni):
        with dbapi2.connect(config) as connection:
            cursor = connection.cursor()
            query = """SELECT fav_department from FAVORITEUNIS where user_logname = '%s'""" % (updatefavoriteUni)
            cursor.execute(query)
            connection.commit();
            return render_template('favoriteUnis_update.html', favoriteUni_updates=cursor)


    def favoriteUnis_db_update_apply(config, updatefavoriteUni):
        with dbapi2.connect(config) as connection:
            cursor = connection.cursor()
            try:
                fav_department = request.form['favorites_text']
                query = """UPDATE FAVORITEUNIS set fav_department ='%s' where user_logname = '%s'""" % (fav_department, updatefavoriteUni)
                cursor.execute(query)
                connection.commit();
                return redirect(url_for('favoriteUnis'))
            except:
                return 'Value cannot be NULL! <a href="http://localhost:5000">Home</a>'

The input is read from the text box in the figure 3.2.4.2.8 after submit operation. The new value of fav_department is inserted with the sql in the figure. There is a control in order to warn the user not to enter null value (Figure 3.2.4.2.7).

.. code-block:: python

		<th>Favorite University Department</th>
      </tr>
    </thead>
	<tbody>
    {% for fav_department in favoriteUni_updates %}
    <td><input type="text" name="favorites_text" required="required" value="{{fav_department[0]}}" style="width:95%"></td>
    {% endfor %}
    <tr>
			<td colspan="3" align="center"><input value="Update Favorite Department" name="add" type="submit"></td>
	</tr>
	</tbody>
	</table>


The row that will be deleted is selected by its user_logname.

.. code-block:: python

    def favoriteUnis_db_delete(config, deletefavoriteUni):
        with dbapi2.connect(config) as connection:
            cursor = connection.cursor()
            query = "DELETE FROM FAVORITEUNIS where user_logname = %s"
            cursor.execute(query, (deletefavoriteUni,))
            connection.commit();
            return redirect(url_for('favoriteUnis'))


Part 3 – Favorite Events
Favoriteevents table has 4 columns which are favoriteevent_id, event_name, user_logname, and join status (figure 3.2.4.3.1). Column event_name has foreign key relation with the column event_name from activities. All the delete and update operations are defined as cascade.

.. code-block:: python

            query = """DROP TABLE IF EXISTS FAVORITESEVENTS CASCADE;"""
            cursor.execute(query)


            query = """CREATE TABLE IF NOT EXISTS FAVORITEEVENTS (
            favoriteevent_id serial unique not null,
            event_name VARCHAR(200) not null,
            user_logname VARCHAR(60) not null,
            join_status VARCHAR(150) not null,
            primary key(favoriteevent_id),
            foreign key(event_name) references activities(event_name) on delete cascade on update cascade)
            """
            cursor.execute(query)

After reaching the favoriteEvents.html, the all rows are seen from the table with the html and python codes Figure 3.2.4.3.2 and figure 3.2.4.3.3.
            
.. code-block:: python 
 
 	<tbody>
		{% for user_logname, event_name, join_status in favoriteEvents_list %}
		<tr>
			<td class="FavoritesTableItem">{{user_logname}}</td>
			<td class="FavoritesTableItem">{{event_name}}</td>
			<td class="FavoritesTableItem">{{join_status}}</td>
			<td class="FavoritesTableItem"><a href="{{ url_for('favoriteEvent_delete', deletefavoriteEvent=user_logname) }}">Delete</a>
			<td class="FavoritesTableItem"><a href="{{ url_for('favoriteEvent_update', updatefavoriteEvent=user_logname) }}">Update</a>
		</tr>
		{% endfor %}
    
    
.. code-block:: python

    def favoriteevents_db(config):
        with dbapi2.connect(config) as connection:
            if request.method == 'GET':
                cursor = connection.cursor()
                query = "SELECT user_logname, event_name, join_status from favoriteevents"
                cursor.execute(query)
                connection.commit();
                return render_template('favoriteEvents.html', favoriteEvents_list=cursor)

When the user wants to add a new event, he/she presses the new favorite event button. Then the user is directed to the html page favoriteEvents_edit. In this page all the columns of a new element is taken from the user via text boxes. After all the values are entered, the submit button works the following code (figure 3.2.4.3.4).

.. code-block:: python

    def savefavoriteEvents(config):
        event_name = None
        user_logname = None
        join_status = None
        if request.method == 'POST':
            event_name = request.form['event_name_text']
            print(event_name)
            user_logname = request.form['floginname_text']
            print(user_logname)
            join_status = request.form['status_text']
            print(join_status)
            with dbapi2.connect(config) as connection:
                cursor = connection.cursor()
                try:
                    query = """INSERT INTO favoriteevents(event_name, user_logname, join_status) VALUES (%s, %s, %s)"""
                    cursor.execute(query, (event_name, user_logname, join_status))
                    connection.commit();
                    return 'Your favorite event has been successfully posted <a href="http://localhost:5000">Home</a>'
                except:
                    return 'Your favorite event cannot be added due to foreign key constraints! <a href="http://localhost:5000">Home</a>'

This code also checks the whether the value is not appropriate the foreign key rule. If it is there is an error exception. 
Update and delete operations are implemented via the buttons at the right side of the table where favoriteEvents.hml in. Selection for both operations are done according to user_logname (figure 3.2.4.3.5, figure 3.2.4.3.6). 


.. code-block:: python

    def favoriteevents_db(config):
        with dbapi2.connect(config) as connection:
            if request.method == 'GET':
                cursor = connection.cursor()
                query = "SELECT user_logname, event_name, join_status from favoriteevents"
                cursor.execute(query)
                connection.commit();
                return render_template('favoriteEvents.html', favoriteEvents_list=cursor)


.. code-block:: python

    def favoriteevents_db_update(config, updatefavoriteEvent):
        with dbapi2.connect(config) as connection:
            cursor = connection.cursor()
            query = """SELECT join_status from favoriteevents where user_logname = '%s'""" % (updatefavoriteEvent)
            cursor.execute(query)
            connection.commit();
            return render_template('favoriteEvents_update.html', favoriteEvents_updates=cursor)

Update operation is done in the favoriteEvents_update. Html page. Join status is adjusted. As it is seen in the figure 3.2.4.3.7, there is an exception which is assigning a null value to the join status.

.. code-block:: python

    def favoriteevents_db_update_apply(config, updatefavoriteEvent):
        with dbapi2.connect(config) as connection:
            cursor = connection.cursor()
            try:
                join_status = request.form['favorites']
                query = """UPDATE favoriteevents set join_status ='%s' where user_logname = '%s'""" % (join_status, updatefavoriteEvent)
                cursor.execute(query)
                connection.commit();
                return redirect(url_for('favoriteEvents'))
            except:
                return 'Value cannot be NULL! <a href="http://localhost:5000">Home</a>'

Part 4 – Favorite Tags
Favoritetags table has 5 columns. These are favoritetag_id , tag_input, user_logname, pop_tag,  and date. The column tag_input hs foreign key relation with the column tag input from tags table. Both update and delete operations are on cascade because of the foreign key relation (Figure 3.2.4.4.1).

.. code-block:: python

            query = """DROP TABLE IF EXISTS FAVORITETAGS CASCADE;"""
            cursor.execute(query)

            query = """CREATE TABLE IF NOT EXISTS FAVORITETAGS (
            favoritetag_id serial unique,
            tag_input VARCHAR(200) not null,
            user_logname VARCHAR(60) not null,
            pop_tag VARCHAR(100) not null,
            date date DEFAULT current_date,
            primary key(favoritetag_id),
            foreign key(tag_input) references tags(tag_input) on delete cascade on update cascade
            )
            """
            cursor.execute(query)

When the user enters the favorite tags page by clicking its button from favorites admin panel, he/she sees all the rows of favorite tags table. The data are extracting with the code in the figure 3.2.4.4.2.

.. code-block:: python

    def favoriteTags_db(config):
        with dbapi2.connect(config) as connection:
            if request.method == 'GET':
                cursor = connection.cursor()
                query = "SELECT DISTINCT user_logname, tag_input, pop_tag from favoritetags"
                cursor.execute(query)
                connection.commit();
                return render_template('favoriteTags.html', favoriteTags_list=cursor)
                
                
Figure 3.2.4.4.2 Distinct selection of all the rows of favoritetags table
In order to add new favorite tag and define its popularity, user is directed to the favoriteTags_edit.html page via the button named as the new favorite tags. There are text boxes in this page to take the inputs from user (figure 3.2.4.4.3)


.. code-block:: python


  <body>
	<h2>Add new favorite tag</h2>
    <div class="container bg-2 text-center">
  <h3>Please Enter Information</h3>
    <form class="col-lg-12" action="{{url_for('savefavoriteTags')}}" method="POST">
    <div class="form-group">
      <label for="name">User Name:</label>
       <input class="form-control" id="flogin_name_text" name="flogin_name_text" type="text">
    </div>
    <div class="form-group">
      <label for="surname">Tag Input</label>
	  <h4>Please check the tag input <li role="presentation" class="active"><a href="{{ url_for('tags') }}">Check!</a></li></h4>
       <input class="form-control" name="tag_input_text" id="tag_input_text" type="text">
    </div>
    <div class="form-group">
      <label for="username">Popular Tag:</label>
      <input type="text" class="form-control" name="pop_tag_text"  id="pop_tag_text">
    </div>
   <button type="submit" id="btn_sign" class="btn btn-default">Save</button>
  </form>

            
Because of the foreign key relation the entered tag_input must be same with the tag_input from tags table. There is a check link which is connected to the tags page to check the tag_input value, if the user wants. When submit button is pressed the following code works (Figure 3.2.4.4.4). If something damages the foreign key relation, there is  an error message for the user. 

.. code-block:: python

    def savefavoriteTags(config):
        tag_input = None
        user_logname = None
        pop_tag = None
        if request.method == 'POST':
            tag_input = request.form['tag_input_text']
            print(tag_input)
            user_logname = request.form['flogin_name_text']
            print(user_logname)
            pop_tag = request.form['pop_tag_text']
            print(pop_tag)
            with dbapi2.connect(config) as connection:
                cursor = connection.cursor()
                try:
                    query = """INSERT INTO favoritetags(tag_input, user_logname, pop_tag) VALUES (%s, %s, %s)"""
                    cursor.execute(query, (tag_input, user_logname, pop_tag))
                    connection.commit();
                    return 'Your favorite tag has been successfully posted <a href="http://localhost:5000">Home</a>'
                except:
                    return 'Your favorite tag cannot be added due to foreign key constraints! <a href="http://localhost:5000">Home</a>'



For the delete and update operations there are links to the right side of the table in the favoriteTags.html. After pressing the delete link, the following code is compiled and the chosen row is deleted. Row is selected according to user_logname.


.. code-block:: python

    def favoriteTags_db_delete(config, deletefavoriteTag):
        with dbapi2.connect(config) as connection:
            cursor = connection.cursor()
            query = "DELETE FROM favoritetags where user_logname = %s"
            cursor.execute(query, (deletefavoriteTag,))
            connection.commit();
            return redirect(url_for('favoriteTags'))


For the update operation the update link is connected to the favoriteTags_update.html and the new value of input is taken with the text box from this page (figure 3.2.4.4.5). Update operation is defined on the popularity of tag, so user can change this value.

.. code-block:: python

	<tbody>
    {% for pop_tag in favoriteTag_updates %}
    <td><input type="text" name="favorites" required="required" value="{{pop_tag[0]}}" style="width:95%"></td>
    {% endfor %}
    <tr>
			<td colspan="3" align="center"><input value="Update popularity" name="add" type="submit"></td>
	</tr>
	</tbody>

The old value of the popularity is written to the text box with the pyhthon code in the figure 3.2.4.4.6. The row is chosen by the user_logname.

.. code-block:: python

    def favoriteTags_db_update(config, updatefavoriteTag):
        with dbapi2.connect(config) as connection:
            cursor = connection.cursor()
            query = """SELECT pop_tag from favoritetags where user_logname = '%s'""" % (updatefavoriteTag)
            cursor.execute(query)
            connection.commit();
            return render_template('favoriteTags_update.html', favoriteTag_updates=cursor)


    def favoriteTags_db_update_apply(config, updatefavoriteEvent):
        with dbapi2.connect(config) as connection:
            cursor = connection.cursor()
            try:
                pop_tag = request.form['pop_tag']
                query = """UPDATE favoritetags set pop_tag ='%s' where user_logname = '%s'""" % (pop_tag, updatefavoriteEvent)
                cursor.execute(query)
                connection.commit();
                return redirect(url_for('favoriteTags'))
            except:
                return 'Value cannot be NULL! <a href="http://localhost:5000">Home</a>'


Part 5 – Favorite Tweets
Favoritetweets table is created (Figure). However, it is not used in the pages.


.. code-block:: python
            query = """DROP TABLE IF EXISTS FAVORITESTWEETS CASCADE;"""
            cursor.execute(query)
            query = """CREATE TABLE IF NOT EXISTS FAVORITETWEETS(
            favoritetweet_id serial unique,
            tweet_category VARCHAR(200) not null,
            user_logname VARCHAR(200) not null,
            pop_keyword VARCHAR(100) not null,
            primary key(favoritetweet_id, user_logname),
            foreign key(user_logname) references user_login(user_loginname) on delete cascade on update cascade,
            foreign key(tweet_category) references TWEETS(tweet_category) on delete cascade on update cascade
            )
            """
            cursor.execute(query)




















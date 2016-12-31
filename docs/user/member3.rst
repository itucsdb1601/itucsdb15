Parts Implemented by Songül Saraç
================================

In order to manage tweets, tags, comments, direct messages and activities as an admin of Unicorn social media web application, all tweets based tables should be initialized by writing itucsdb1601.mybluemix.net/tweets/initialize_tweets on address bar. If tables can be created successfully, the program gives a “Tables inserted” output on page as follow.

.. figure:: member3/1initdb.png
	:scale: 50 %
	:alt: create tweets tables

After all tables were created, admin user that wants to manage activities such as sending a tweet for a specific user should enter the activities panel page by clicking the “Tweets” button on home page that is seen on Figure xx. ********buraya figure numarasını gir*********** or admin can reach activities panel seen on below image by entering itucsdb1601.mybluemix.net/activities_panel into address bar of the browser. 


On activities panel page, admin user can access tweets, tags, events, comments and direct messages by clicking the buttons of each activity. 

.. figure:: member3/2activities.png
	:scale: 50 %
	:alt: activities main page

In order to manage tweets of Unicorn users, admin should click “Tweets” button on activities panel page seen on above figure. After that, admin can see all tweet information on itucsdb1601.mybluemix.net/tweets address. The following figure shows this page. On this page, all tweet information are displayed and also delete and update operations can be done by clicking the “Delete” and “Update” on the right side of a tweet.

.. figure:: member3/3tweetpanel.png
	:scale: 50 %
	:alt: tweet panel

If a user wants to update tweet for a specific user, he/she clicks the update button what is next to tweet that will be updated and he/she is directed to itucsdb1601.mybluemix.net/tweets/update/<username>/ as it can be seen on below.

.. figure:: member3/4updatetweet.png
	:scale: 50 %
	:alt: update tweet page

The tweet panel after update operation can be seen as below.

.. figure:: member3/5updatedpanel.png
	:scale: 50 %
	:alt: updated tweet panel

Additionally, admin can add a new tweet for a user by entering information. To achieve this, admin can click the “Add a New Tweet” button on the top of tweet panel page. After that, admin can reach the following page and enter username, tweet and tweet category. However, username that will be entered must be on database previously, otherwise, it gives an error message that can be seen below.

.. figure:: member3/6updateerror.png
	:scale: 50 %
	:alt: update not allowed

.. figure:: member3/7updateerrormessage.png
	:scale: 50 %
	:alt: update error message

Moreover, admin user can manage tags for tweets by clicking “Tags” button on activities panel page and directing to tag panel whose address is itucsdb1601.mybluemix.net/tags as follow. All tag information are represented on this page. Here, there is a “Home” button in order to turn back to home page as it is seen in the following figure

.. figure:: member3/8tagpanel.png
	:scale: 50 %
	:alt: tag panel

Deletion and updating operations can be done from right side of a tag. After clicking “Update”, admin directs to tag panel page.

.. figure:: member3/9updatetag.png
	:scale: 50 %
	:alt: update tag page

After this operation, tag is updated. It can be seen in the following figure.

.. figure:: member3/10updatedtagpanel.png
	:scale: 50 %
	:alt: updated tag panel page

In order to add a new tag for a tweet, user should click “Add a New Tag” button at right top of above tag panel page. This operation can be proceeded on below page.

.. figure:: member3/11tagadd.png
	:scale: 50 %
	:alt: add a new tag

Here, tweet input must be included in tweets; otherwise, it gives an error.
All direct messages are displayed on DM panel page. This page can be reached from activities panel by clicking “Direct Messages”

.. figure:: member3/12dmpanel.png
	:scale: 50 %
	:alt: direct messages panel

If an admin wants to send a direct messages from one user to another, he/she should enter usernames for sender and receiver that are included in users on database. This page can be accessed by admin by clicking “Send a Direct Message” button on top of DM panel page.

.. figure:: member3/13sendmessage.png
	:scale: 50 %
	:alt: send a DM

In order to update message, admin should click “Update” that is next to message that is wanted to be updated and he/she directs to following page.

.. figure:: member3/14updatedm.png
	:scale: 50 %
	:alt: update a DM

When this update operation will be done successfully by admin, following page will be presented on DM panel.

.. figure:: member3/15dmpanelupdate.png
	:scale: 50 %
	:alt: updated DM

An admin user can add a new comment by entering username for a user who is contained in users on database, tweet that is included on tweets on database and finally comment by clicking “Add a New Comment” button on Comment panel page.

.. figure:: member3/16addcomment.png
	:scale: 50 %
	:alt: add a new comment

Comment panel page can be reached from activity panel page by clicking “Comments” button and it displays all comments for all tweets as follow.

.. figure:: member3/17commentpanel.png
	:scale: 50 %
	:alt: comment panel

In order to update a comment, user can use “Update” link on the right side of comment and he/she directs following page

.. figure:: member3/18updatecomment.png
	:scale: 50 %
	:alt: updating comment page

.. figure:: member3/19commentupdate.png
	:scale: 50 %
	:alt: updated comment page

If a user wants to create a new event, he/she should access the following page from event panel and enter the information about events.

.. figure:: member3/20events.png
	:scale: 50 %
	:alt: events page

On event panel page, all events are selected and showed. This page can be reached from activities panel by clicking “Activities”. In order to turn back to home page and activities panel pages, there are buttons on right top of comment list.

.. figure:: member3/21eventpanel.png
	:scale: 50 %
	:alt: event panel

If a user wants to update event name, following page should be reached by clicking “Update” link from next to comment.

.. figure:: member3/22updateeventname.png
	:scale: 50 %
	:alt: update event name

After update operation, event name will be displayed with its new name as below.

.. figure:: member3/23updatedevent.png
	:scale: 50 %
	:alt: updated event shown









Parts Implemented by Zeynep Öner
================================

Shown below is our home page. 

   .. figure:: ../member5/u1-mainhome.png
   :scale: 50 %
   :alt: home page

When the user click on the Interaction button, suddenly below page appears. These three buttons are representation of add operation for three entities: followers, following, and blocked.

   .. figure:: ../member5/u2-interactionmain.png
   :scale: 50 %
   :alt: interaction page

To add a new user to these three entities, the user needs to enter an user name that already exists in user_login table. For that purpose, text fields are used.

   .. figure:: ../member5/u3-enterusername.png
   :scale: 50 %
   :alt: add new user

When the user enters an user name that does not exist in user_login table, suddenly below error page occurs “There is no such entry in the user table”.

   .. figure:: ../member5/u4-usernameerror.png
   :scale: 50 %
   :alt: user name error message

If the user enters an user name that is already inserted to followers table, another error page occurs which is “This entry already exists in followers table”.

   .. figure:: ../member5/u5-existerror.png
   :scale: 50 %
   :alt: user already exists error 

If the user enters a valid user name to the text field for Followers List, the page that belongs to follower table appears Here, with follow button after the given user name is checked just like happened above, the new user is added to followers table. Remove button deletes the entered person from followers table if it exists in followers table. Search button scans followers table for the given user name. If it exists, the selected row is printed on the screen, otherwise it occurs an error.

   .. figure:: ../member5/u6-follow.png
   :scale: 50 %
   :alt: follow page

For update operation, two extra tables are connected to followers table: playlist and SM.

   .. figure:: ../member5/u7-update.png
   :scale: 50 %
   :alt: update operation page

When the user chooses a song to add his/her playlist, playlist_id is taken according to this song from playlist table and added to followers table under playlist_id column where the user name equals to entered user name.

   .. figure:: ../member5/u8-sm.png
   :scale: 50 %
   :alt: social media page

In the same way with playlist, social_media_id is taken according to chosen social media that will be connected to unicorn account, and added to followers table under social_media_id column where the user name equals to entered user name.

   .. figure:: ../member5/u9-enterfollowing.png
   :scale: 50 %
   :alt: add to followings

If the user adds an user to followings list after some controls, below page appears. 

   .. figure:: ../member5/u10-following.png
   :scale: 50 %
   :alt: following page

Controls for follow, unfollow, and search operations are the same with the operations done on followers page. In update part, according to given user name, location_id and event_id columns in following table are updated. When the user enters a city name, location_id is taken from location table, and when he/she chooses an event to attend event_id is get from events table. Then these two values are added to following table under location_id and event_id columns.
With find button, the user can find other users who are in the entered location.

   .. figure:: ../member5/u11-enterblocked.png
   :scale: 50 %
   :alt: blocked page

For the last part, the user can block entered user if it exists in user_login table. After the user blocks another user, below page appears for more operation on this table.

   .. figure:: ../member5/u12-blocktype.png
   :scale: 50 %
   :alt: block type

More user can be blocked with follow button, and removed from blocked list with unfollow button. Search operation performs for entered user name. In Update part, the user can change the time how many days the blocked user is being kept as a blocked. Block type can be also chosen as a reason. The user chooses a type, then type_id is taken from blocked_type table to be added to blocked table under type_id column.




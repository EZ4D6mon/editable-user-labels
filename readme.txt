 [Context: when customers go to a website, they would like to choose their favorite label for their search product or product recommendations, we need to build a label input page to extract customer’s own labels based on this need.]
 
Design and complete a website to input your labels, in the page you can add your label, rename your label and delete your label. The system has its own login section, where the session would remember the user and user’s labels. When user store their labels, the labels would update to the database, and when user come back to the website page, the updated added label would be showed on current user the page. (Time limitation: 2 days; Experience requirement: Must have hands on experience in full stack or development engineer; Language: Preferred python (Django) or java)

admin
username: 
Admin
password:
SearchTag

urls:
'register/': user registrition
'login/': user login
'logout/':	user logout
'': homepage with navbar and dashboard
'about/': description page
'user/<str:pk_test>/': user page. Admin acount can manage all users.
'account/': account settings
'create_tag/': create a new tag for user
'rename_tag/": rename a tag for user
'delete_tag/<str:pk>/': delete a tag from a user
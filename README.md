# users-greetings
Users-greetings is a web service for greeting users:
-- Привіт, " + userName + ' ' + userSurname + '(' + userEmail + ')' --- in case of new user 
--- "Вже бачилися, "  + userName + ' ' + userSurname + '(' + userEmail + ')' --- otherwise.

Although user can get acquinted with a list of already greetin users. Services gives opportunities to user to sort list of already greetin users in alphabetically and reversed alphabetically order by user's names.

User-greetings server was developed with using Python3, Flask, Bootstrap, Jinja2, Flask-SQLAlchemy, PostgreSql etc. More detailed information about all libraries, technologies and its versions could be found in requirements.txt file.

Although access to remote database with some test cases is used in the code, what simplifies testing of  and familiarization with the service.
You can change database on your own by changing its uri(app.config['SQLALCHEMY_DATABASE_URI']) in main.py file.

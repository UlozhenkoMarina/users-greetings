from flask import Flask, request, render_template
from flask_sqlalchemy import SQLAlchemy
import Model



app = Flask(__name__)
app.debug = True
#app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://localhost/names'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://tclfknewryhjlb:7b093abcdccaabb55c17bba01ce71f21a3798509a84321ad4b8f12e2d1c722ef@ec2-54-216-159-235.eu-west-1.compute.amazonaws.com:5432/d5s9rbkkdg14oh'
db = SQLAlchemy(app)

#db.create_all()
#db.session.commit()


# function for user greetings
@app.route("/", methods=['post', 'get'])
def startpage():
    message = ''
    try:
        if request.method == 'POST':
            userName = request.form.get('userName')
            userSurname = request.form.get('userSurname')
            userEmail = request.form.get('userEmail')
            if userName and userSurname and userEmail:
                if Model.UsersNames.query.filter_by(name=userName, surname=userSurname, email=userEmail).first():
                    message = "Вже бачилися, "  + userName + ' ' + userSurname + '(' + userEmail + ')'
                else:
                    message = "Привіт, " + userName + ' ' + userSurname + '(' + userEmail + ')'
                    db.session.add(Model.UsersNames(name=userName, surname=userSurname, email=userSurname))
                    db.session.commit()
            else:
                message = "All fields should not be empty"
        return render_template('nameInput.html', message=message)
    except:
        return render_template('nameInput', message='Some error occurs. Try again.')

# function for showing list of already greetin users
@app.route("/state")
def listOfNames():
    try:
        return render_template('namesList.html', users=Model.UsersNames.query.all())
    except:
        return render_template('namesList.html', users=[])

# function for showing list of already greetin users in sorted alphabetically by user's names
@app.route("/sortup")
def sortup():
   # try:
        return render_template('namesList.html', users=Model.UsersNames.query.order_by(Model.UsersNames.name).all())
    #except:
     #   return render_template('namesList.html', users=[])

# function for showing reversed list of already greetin users in sorted alphabetically by user's names
@app.route("/sortdown")
def sortdown():
    try:
        return render_template('namesList.html', users=reversed(Model.UsersNames.query.order_by(Model.UsersNames.name).all()))
    except:
        return render_template('namesList.html', users=[])


if __name__ == '__main__':
    app.run()
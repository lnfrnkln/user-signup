from flask import Flask, render_template, redirect, request,url_for


app = Flask(__name__)

app.config['DEBUG'] = True

@app.route("/", methods=['GET','POST'])
def home():
    if request.method =='post':
        username = request.form['username']
        password = request.form['password']
        password2 =request.form['password2']
        email=request.form['email']
        username_error =""
        password_error = ""
        password2_error =""
        email_error=""

        if username =='':
            username_error = "Username is required."
        elif " " in username:
            username_error ="Username contains spaces."
        elif len(username) < 3 or len(username) >20:
            username_error="Username must be 3-20 characters long."
     
        if password =='':
            password_error ="Password required."
        elif " " in password:
            password_error= "Password contains spaces."
        elif len(password) <3 or len (password) > 20:
            password_error= "Password must be 3-20 characters long."

        if password2 == '':
            password2_error = "Please confirm your password."
        elif password2 != password:
            password2_error = "You password doesn't match."

        if email == '':
            email_error = ''
        elif "@" not in email:
            email_error = "Your email address is missing @ symbol."
        elif "." not in email:
            email_error = "Your email address is missing . symbol."
        elif " " in email:
            email_error = "Email address cannot contain spaces."
        elif len(email) < 3 or len(email) > 20:
            email_error = "Your email address must be at least 3 and shorter than 20."
        
        if not username_error and not password_error and not password2_error and not email_error:
            return redirect(url_for("welcome_page", username=username))
            
        else:
            return render_template("home_page.html", username = username, email = email, username_error = username_error, password_error = password_error, password2_error = password2_error, email_error = email_error, password=password, password2=password2)

    
    return render_template("home_page.html")


@app.route("/welcome")
def welcome():
    username=request.args.get('username')
    email =request.args.get('email')
    return render_template("welcome_page.html", name=username, email=email)


app.run()



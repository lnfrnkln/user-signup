from flask import Flask, request,render_template
import cgi

app = Flask(__name__)

app.config['DEBUG'] = True

@app.route("/register", methods=['POST'])
def register():
   username = cgi.escape(request.form['username'])
   password = cgi.escape(request.form['password'])
   password2 = cgi.escape(request.form['password2'])
   email=cgi.escape(request.form['email'])

   usernameError =""
   passwordError = ""
   password2Error =""
   emailError=""

   if not username:
       print("no username")
       usernameError = "Username is required"
   if not password:
       passwordError = "Password is required"
   if len(password) < 3:
       passwordError = "Password must be at least 3 characters long"
   if len(password) >20:
       passwordError="password must be no more than 20 charadcters long"
   else:
       hasNumber = False
       for char in password:
           if char.isdigit():
               hasNumber = True
       if not hasNumber:
           passwordError = "Password must contain a number"
   if password  != password2:
       password2Error = "Password 2 must match password"
   if "@" and "." not in email:
       emailError="email must contain @ and ."

   if usernameError or passwordError or password2Error or emailError:
       print("there was an error!")
       return render_template('home_page.html',username=username,usernameError=usernameError,password=password,passwordError=passwordError,password2=password2,password2Error=password2Error,email=email,emailError=emailError)
   return "Welcome, " + username


@app.route("/")
def index():
   return render_template('welcome_page.html')

@app.route("/register", methods=['GET'])
def register_page():
   return render_template('home_page.html')

app.run()

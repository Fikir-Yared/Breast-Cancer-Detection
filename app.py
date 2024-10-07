from flask import Flask, render_template, request,redirect,url_for
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, logout_user
import os
import tensorflow as tf
from tensorflow.keras.preprocessing import image
import numpy as np


app = Flask(__name__)

app.config['UPLOAD_FOLDER'] = 'static/uploaded image'
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///db.sqlite"
app.config["SECRET_KEY"] = "abc"
db = SQLAlchemy()

login_manager = LoginManager()
login_manager.init_app(app)









class Users(UserMixin, db.Model):
	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(250), unique=True, nullable=False)
	password = db.Column(db.String(250), nullable=False)


db.init_app(app)


with app.app_context():
	db.create_all()


@login_manager.user_loader
def loader_user(user_id):
	return Users.query.get(user_id)


@app.route('/register', methods=["GET", "POST"])
def register(error=''):
      
    if request.method == "POST":
        try:
            user = Users(username=request.form.get("username"),
                        password=request.form.get("password"))
            db.session.add(user)
            db.session.commit()
            return redirect(url_for("login"))
        except:
             return render_template("sign_up.html",error="Username already taken!!")
    return render_template("sign_up.html",error=error)


@app.route("/login", methods=["GET", "POST"])
def login(error=''):
    if request.method == "POST":
        try:
            user = Users.query.filter_by(
                username=request.form.get("username")).first()
            if user.password == request.form.get("password"):
                login_user(user)
                return redirect(url_for("home"))
        except:
            return render_template("login.html",error="Wrong username or password!")
    return render_template("login.html",error=error)


@app.route("/logout")
def logout():
	logout_user()
	return redirect(url_for("home"))




     





















@app.route("/")
@app.route("/home")
def home():

    return render_template("home.html")


@app.route("/service",methods=["POST","GET"])
def service():
    result=['','']
    if request.method == 'POST':
        try:
            
            if request.form['submit_button'] == 'reset':
                return render_template("service.html",result=result)
            
               
        except:
                
            try:
                if request.form['submit_button'] == 'detect':
                    print("845612345645")
            except:
                 pass 
            f = request.files['file'] 
            path=os.path.join(app.config['UPLOAD_FOLDER'],f.filename)
            f.save(os.path.join(app.config['UPLOAD_FOLDER'],f.filename))
            value=predict_image_class(path)
            result = "Benign" if value==[0] else "Malignant"
            result[result,'91%']
            return render_template("service.html", name = f.filename,result=result)  
          
    else:
        return render_template("service.html",,result=result)


@app.route("/about")
def about():

    return render_template("About.html")
@app.route("/contact")
def contact():

    return render_template("contact.html")

 

model = tf.keras.models.load_model('first_model (3).keras')

def load_and_preprocess_image(img_path):
    img = image.load_img(img_path, target_size=(224, 224)) 
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array /= 255.0  
    return img_array

def predict_image_class(img_path):
    img_array = load_and_preprocess_image(img_path)
    predictions = model.predict(img_array)
    predicted_class = np.argmax(predictions, axis=1)
    return predicted_class






if "__main__" == __name__:
    app.run(host="0.0.0.0", debug=True)

from flask import Flask, render_template, request, flash, redirect, url_for
from forms import imageform
from resnet50 import predict
from PIL import Image
from dotenv import load_dotenv
import os
from flask_wtf.csrf import CSRFProtect

app = Flask(__name__)
load_dotenv()

# Access the secret key from environment variables
secret_key = os.getenv('SECRET_KEY')
if not secret_key:
    raise ValueError("No SECRET_KEY1 set for Flask application")
app.config['SECRET_KEY'] = secret_key
csrf = CSRFProtect(app)

@app.route("/", methods=['GET', 'POST'])
@app.route("/home", methods=['GET', 'POST'])
def home():
    form = imageform()
    if request.method == 'POST' and form.validate_on_submit():
        image = form.imagefile.data
        if image:
            img = Image.open(image)
            classname = predict(img)
            return render_template('home.html', title='Home',form=form, classname=classname)
        else:
            flash('File not selected', 'success')
            return redirect(url_for('home'))
    return render_template('home.html', title='Home', form=form)


@app.route("/about")
def about():
    return render_template("about.html", title="About")

@app.route("/contact")
def contact():
    return render_template("contact.html", title="Contact")

if __name__ == "__main__":
    app.run(debug=True)
from flask import Flask, render_template
from markupsafe import escape

import Hello
app = Flask(__name__, static_url_path='/assets')

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/guide")
def guide():
    return render_template('guide.html')

@app.route("/generate/norm/")
def norm_gen():
    return render_template('norm_gen.html')

@app.route("/generate/<int:num>")
def gen(num):
    return render_template('post_gen.html', num=Hello.Sound(num))

@app.route("/generate/cust/")
def cust_gen():
    return render_template('cust_gen.html')

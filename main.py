from flask import Flask,render_template,url_for

app=Flask(__name__)

@app.route('/')
@app.route('/home')
def home_page():
    return render_template('home.html')

@app.route('/entertainment')
def entertainment():
    return render_template('entertainment.html')

@app.route('/sport')
def sport():
    return render_template('sport.html')

@app.route('/prices')
def prices():
    return render_template('prices.html')


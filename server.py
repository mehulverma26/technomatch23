from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def hello():
    title="Introduction to the Project"
    return render_template('index.html',title=title)

@app.route("/prediction")
def prediction():
    title="Weather Prediction"
    return render_template('prediction.html',title=title)

@app.route("/humidity")
def humidity():
    title="Humidity"
    return render_template('humidity.html',title=title)

@app.route("/temp")
def temp():
    title="Temperature"
    return render_template('temp.html',title=title)

@app.route("/snow")
def snow():
    title="Snow"
    return render_template('snow.html',title=title)

@app.route("/precipitation")
def precipitation():
    title="Precipitation"
    return render_template('precipitation.html',title=title)
app.run(debug=True)
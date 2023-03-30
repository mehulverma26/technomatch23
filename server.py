from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def hello():
    title="Introduction to the Project"
    return render_template('index.html',title=title)

@app.route("/prediction")
def prediction():
    title="the plots and predictions"
    return render_template('prediction.html',title=title)
app.run(debug=True)

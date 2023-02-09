from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    pagetitle ="Welcome to OTT release Online Data Sync Services ."
    return render_template("home.html",pagetitle = pagetitle)

@app.route("/sync_data")
def sync_data():
    try:
        return "Welcome to Ott Loader - sync_data."
    except Exception as error:
        print(f"Error from sync_data : {error}")

if __name__ == '__main__':
    app.run(debug=True )
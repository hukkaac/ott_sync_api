from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Welcome to Ott Loader."

@app.route("/sync_data")
def sync_data():
    try:
        return "Welcome to Ott Loader - sync_data."
    except Exception as error:
        print(f"Error from sync_data : {error}")

if __name__ == '__main__':
    app.run( )
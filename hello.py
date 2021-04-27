from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "If you can see this that means this was sucessful"

if __name__ == "__main__":
    app.run()
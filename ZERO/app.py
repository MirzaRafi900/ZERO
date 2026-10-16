from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "ZERO AI Assistant is Running"


if __name__ == "__main__":
    app.run(debug=True)
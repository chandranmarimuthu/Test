from flask import Flask
app =Flask(__name__)
@app.route("/")
def hello():
    return "hello chandran"

if __name__ == "__main__":
    app.run()

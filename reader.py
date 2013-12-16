from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    reader = open('fichero.txt')
    for row in reader:
        print(row, end='')
    return "Reading fichero.txt file"

if __name__ == "__main__":
    app.run()

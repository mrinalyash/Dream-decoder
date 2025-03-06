from flask import Flask, request, render_template
from main import interpret_dream
from time import time

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    meaning = ""
    if request.method == "POST":
        dream_text = request.form["dream"]
        start = time()
        meaning = interpret_dream(dream_text)
        end = time()
        print(f"Total time for interpretation: {end - start:.2f} seconds")
    return render_template("index.html", meaning=meaning)

if __name__ == "__main__":
    app.run(debug=True)
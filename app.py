from flask import Flask, request, render_template
from main import interpret_dream  # Import the AI function

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    meaning = ""
    if request.method == "POST":
        dream_text = request.form["dream"]
        meaning = interpret_dream(dream_text)  # Send input to AI model
    return render_template("index.html", meaning=meaning)

if __name__ == "__main__":
    app.run(debug=True)

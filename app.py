from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        content = request.form["content"]
        return render_template("index.html", content=content)
    return render_template("index.html", content=None)

if __name__ == "__main__":
    app.run(debug=True)

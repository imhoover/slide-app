from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        content = request.form["content"]
        return redirect(url_for("preview", content=content))
    return render_template("index.html")


@app.route("/preview", methods=["GET", "POST"])
def preview():
    if request.method == "POST":
        content = request.form.get("content", "")
    else:
        content = request.args.get("content", "")
    return render_template("preview.html", content=content)

if __name__ == "__main__":
    app.run(debug=True)

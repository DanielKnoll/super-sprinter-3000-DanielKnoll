from flask import Flask, render_template, redirect, request, session
import functions
app = Flask(__name__)


@app.route("/")
@app.route("/list")
def route_list():
    story = functions.get_story()
    return render_template("list.html", story=story)


@app.route("/new-story", methods=["GET", "POST"])
@app.route("/edit-story/", methods=["GET", "POST"])
def route_edit():
    return render_template("form.html")


@app.route("/save-story", methods=["POST"])
def route_save():
    print("POST request received!")
    if request.method == 'POST':
        new_story = request.form
        functions.save_new_story(new_story)
    return redirect("/")


if __name__ == "__main__":
    app.secret_key = "N3w S3cr3T"  # Change the content of this string
    app.run(debug=True,  # Allow verbose error reports
            port=5000  # Set custom port
            )

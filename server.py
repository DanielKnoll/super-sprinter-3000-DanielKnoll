from flask import Flask, render_template, redirect, request, session
import functions
app = Flask(__name__)


@app.route("/")
@app.route("/list")
def route_list():
    story = functions.get_story()
    return render_template("list.html", story=story)


@app.route("/story", methods=["GET", "POST"])
@app.route("/story/<int:id_>", methods=["GET", "POST"])
def route_edit(id_=None):
    if id_:
        story = functions.get_story()
        title = story[id_][1]
        story = story[id_][2]
        criteria = story[id_][3]
        bis_value = story[id_][4]
        estimation = story[id_][5]
        status = story[id_][6]
        html_code = render_template("form.html",
                                    id_=id_,
                                    title=title,
                                    story=story,
                                    criteria=criteria,
                                    bis_value=bis_value,
                                    estimation=estimation,
                                    status=status)
        return html_code
    else:
        return render_template("form.html", id_=id_)


@app.route("/save-story", methods=["POST"])
@app.route("/edit-story", methods=["POST"])
@app.route("/delete-story/<int:id_>", methods=["GET"])
def route_save(id_=None):
    if request.path == "/save-story":
        new_story = request.form
        print(new_story)
        functions.save_new_story(new_story)
    if request.path == "/edit-story":
        edited_story = request.form
        functions.save_edited_story(id_, edited_story)
    if request.path == "/delete-story/" + str(id_):
        functions.delete_story(id_)
    return redirect("/")


if __name__ == "__main__":
    app.secret_key = "N3w S3cr3T"  # Change the content of this string
    app.run(debug=True,  # Allow verbose error reports
            port=5000  # Set custom port
            )

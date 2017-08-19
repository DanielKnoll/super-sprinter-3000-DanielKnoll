from flask import Flask, render_template, redirect, request, session
import functions
app = Flask(__name__)


@app.route("/")
@app.route("/list")
def route_list():
    all_story = functions.get_story()
    return render_template("list.html", all_story=all_story)


@app.route("/story", methods=["GET"])
@app.route("/story/<int:id_>", methods=["GET"])
def route_edit(id_=None):
    if id_:
        all_story = functions.get_story()
        try:
            index = functions.find_line_index_by_id(id_, all_story)
        except ValueError:
            return
        one_story = all_story[index]
        title = one_story[1]
        story_desc = one_story[2]
        criteria = one_story[3]
        bis_value = one_story[4]
        estimation = one_story[5]
        status = one_story[6]
        html_code = render_template("form.html",
                                    id_=id_,
                                    title=title,
                                    story_desc=story_desc,
                                    criteria=criteria,
                                    bis_value=bis_value,
                                    estimation=estimation,
                                    status=status)
        return html_code
    else:
        return render_template("form.html", id_=id_)


@app.route("/save-story", methods=["POST"])
def save_new():
    new_story = request.form
    functions.save_new_story(new_story)
    return redirect("/")


@app.route("/story/<int:id_>", methods=["POST"])
def save_edited(id_):
    edited_story = request.form
    functions.save_edited_story(id_, edited_story)
    return redirect("/")


@app.route("/delete-story/<int:id_>", methods=["POST"])
def del_story(id_):
    functions.delete_story(id_)
    return redirect("/")


if __name__ == "__main__":
    app.secret_key = "N3w S3cr3T"  # Change the content of this string
    app.run(debug=True,  # Allow verbose error reports
            port=5000  # Set custom port
            )

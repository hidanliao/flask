from flask import Flask, render_template

app = Flask(__name__, static_folder='assets')

@app.route("/profile2")
def index():
    return "First Web"

# @app.route("/<int:user_id>")
# def profile5(user_id):
#     with open("profile.html", encoding="utf-8") as f:
#         content = f.read()
#
#     content = content.replace("xxxxxxx", str(user_id))
#
#     return content

@app.route("/<int:user_id>")
def profile6(user_id):

    return render_template("profile.html", user_name="Liao", user_head_img="329291347.png")

app.run(debug=True,)
# app.run()
# print(app.url_map)
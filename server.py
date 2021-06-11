from flask import Flask, render_template, request, redirect
app = Flask(__name__)

@app.route('/')
def show_form():
    return render_template("index.html")

@ app.route('/result', methods=['POST'])
def result():
    request.form['name']
    location_from_form = request.form['location']
    language_from_form = request.form['language']
    comment_from_form = request.form['comment']
    return render_template("result.html", name_on_template=request.form['name'], language_on_template=request.form['location'], location_on_template=request.form['location'], comment_on_template=comment_from_form,)


if __name__ == "__main__":
    app.run(debug=True)
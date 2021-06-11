from flask import Flask, render_template, request, redirect
app = Flask(__name__)

@app.route('/')
def show_form():
    return render_template("index.html")

@ app.route('/result', methods=['POST'])
def result():
    return render_template("result.html", name_on_template=request.form['name'], language_on_template=request.form['language'], location_on_template=request.form['location'], comment_on_template=request.form['comment'])


if __name__ == "__main__":
    app.run(debug=True)
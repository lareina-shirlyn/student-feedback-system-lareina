from flask import Flask, render_template, request

app = Flask(__name__)

feedbacks = []  # temporary storage

@app.route('/')
def index():
    return render_template('form.html', feedbacks=feedbacks)

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    fb = request.form['feedback']
    feedbacks.append({"name": name, "feedback": fb})
    return render_template('form.html', feedbacks=feedbacks)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)

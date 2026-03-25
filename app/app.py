from flask import Flask, render_template, request, redirect
from database import init_db, add_feedback, get_feedbacks

import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

app = Flask(
    __name__,
    template_folder=os.path.join(BASE_DIR, "../templates"),
    static_folder=os.path.join(BASE_DIR, "../static")
)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form['name']
        feedback = request.form['feedback']

        add_feedback(name, feedback)

        return redirect('/')

    feedbacks = get_feedbacks()
    return render_template('index.html', feedbacks=feedbacks)


if __name__ == '__main__':
    init_db()
    app.run(host='0.0.0.0', port=5000)

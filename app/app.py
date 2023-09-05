from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/layout')
def layout_page():
    return render_template('layout_bubbles.html')
if __name__ == '__main__':
    app.run()

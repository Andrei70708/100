from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/info1')
def info1():
    return render_template('info1.html')

@app.route('/info2')
def info2():
    return render_template('info2.html')

@app.route('/info5')
def info5():
    return render_template('info5.html')

if __name__ == '__main__':
    app.run(debug=True)



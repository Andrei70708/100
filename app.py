from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('DIAR5.html')

@app.route('/честный_знак')
def честный_знак():
    return render_template('18.html')

@app.route('/Проверка Этикеток')
def quality_control():
    return render_template('18.html')

@app.route('/supply_department')
def supply_department():
    return render_template('supply_department.html')

@app.route('/marketing_department')
def marketing_department():
    return render_template('marketing_department.html')

@app.route('/printing_department')
def printing_department():
    return render_template('printing_department.html')

@app.route('/label_check')
def label_check():
    return render_template('label_check.html')

@app.route('/support')
def support():
    return render_template('support.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)




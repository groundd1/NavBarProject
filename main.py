from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/phone')
def phone():
    return render_template('phone.html')

if __name__ == '__main__':
    app.run(debug=True)

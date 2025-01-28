from flask import Flask, render_template

app = Flask(__name__)

# Route for the homepage
@app.route('/')
def homepage():
    return render_template('index.html')

# Route for the portfolio page
@app.route('/portfolio')
def portfolio():
    return render_template('portfolio.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)


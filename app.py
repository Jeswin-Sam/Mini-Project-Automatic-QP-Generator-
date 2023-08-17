from flask import Flask, render_template

app = Flask(__name__)

# Route for the home page
@app.route('/')
def home():
    return render_template('index.html')

# Route for the upload page
@app.route('/upload')
def upload():
    return render_template('upload.html')

# Route for the generate page
@app.route('/generate')
def generate():
    return render_template('generate.html')

# Run the application
if __name__ == '__main__':
    app.run(debug=True)

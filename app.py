from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    print("Home route accessed")
    return render_template('index.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    print("Contact route accessed")
    if request.method == 'POST':
        print("Form submitted")
    return render_template('index.html', thank_you=(request.method == 'POST'))


if __name__ == '__main__':
    app.run(debug=True)

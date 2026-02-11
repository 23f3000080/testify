from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to Testify!"

@app.route('/api/test')
def test_api():
    return {"message": "This is a test API endpoint."}


if __name__ == '__main__':
    app.run(debug=True)
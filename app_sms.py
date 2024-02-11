from flask import Flask

app = Flask(__name__, template_folder='templates')

@app.route('/sms')
def hello():
    return 'Hello, Quest! Do you need a message from Nigeria? Dont worry, you will receive it and no one will know.'

if __name__ == '__main__':
    app.run(debug=True)

from flask import Flask, render_template

app = Flask(__name__, template_folder='templates')

# Sample received message
received_message = "This is a sample message."

# Route to render the index.html template
@app.route('/')
def index():
    return render_template('index.html', received_message=received_message)

if __name__ == '__main__':
    # Run the Flask application
    app.run(debug=True)
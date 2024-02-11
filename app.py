from flask import Flask, request, render_template

app = Flask(__name__, template_folder='templates')

# Initialize an empty list to store incoming messages
incoming_messages = []

# Route to render the index.html template
@app.route('/')
def index():
    # Pass the received message and the list of incoming messages to the template
    return render_template('index.html', received_message="This is a sample message.", incoming_messages=incoming_messages)

# Route to update the phone numbers and handle incoming messages
@app.route('/update_numbers', methods=['POST'])
def update_numbers():
    # Retrieve the Nigerian and Nigerian numbers from the form
    nigeria_number = request.form['nigeria_number']
    nigerian_number = request.form['nigerian_number']
    
    # Update the phone numbers (you can define your logic here)

    # For demonstration, print the updated numbers
    print("Nigeria Number:", nigeria_number)
    print("Nigerian Number:", nigerian_number)

    # Redirect back to the index page
    return render_template('index.html', received_message="This is a sample message.", incoming_messages=incoming_messages)

# Route to receive incoming messages
@app.route('/receive_message', methods=['POST'])
def receive_message():
    # Get the message content from the request
    message_content = request.form.get('message')

    # Add the received message to the list of incoming messages
    incoming_messages.append(message_content)

    # No response sent back to the sender
    return '', 204

if __name__ == '__main__':
    app.run(debug=True)

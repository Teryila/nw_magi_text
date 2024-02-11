from flask import Flask, request

app = Flask(__name__, template_folder='templates')

# Define route to receive messages from Nigeria number
@app.route('/receive-nigeria-message', methods=['POST'])
def receive_nigeria_message():
    data = request.get_json()
    message = data.get('message')
    forward_message_to_destination(message)
    # No response is sent back to the sender

# Function to forward message to appropriate destination
def forward_message_to_destination(message):
    # Implement logic to forward message to the appropriate destination
    # This could involve using a third-party API for sending SMS messages
    # For illustration purposes, print the message to be forwarded
    print("Forwarding message:", message)

if __name__ == '__main__':
    app.run(debug=True)

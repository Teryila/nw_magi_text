from flask import Flask, request
from twilio.rest import Client

app = Flask(__name__, template_folder='templates')

# Update the source IP address
source_ip = '127.i.5.1'

# Update the Twilio Account SID
account_sid = 'fyb13tdejiklrdxghjkkkkkkkopp;'
auth_token = 'your_auth_token'

# Update the first and second phone numbers
first_phone_number = '+02348888888899'  # Replace with your first phone number
second_phone_number = '+23489shjjjj44'  # Replace with your second phone number

def forward_message_to_nigeria(message_content):
    # Initialize Twilio Client
    client = Client(account_sid, auth_token)

    # Send the message from the first phone number to the second phone number
    client.messages.create(
        body=message_content,
        from_=first_phone_number,
        to=second_phone_number
    )

@app.route('/receive_message', methods=['POST'])
def receive_message():
    # Get the message content from the request
    message_content = request.form.get('message')

    # Forward the received message to the second phone number
    forward_message_to_nigeria(message_content)

    # No response sent back to the sender
    return '', 204

if __name__ == '__main__':
    # Run the Flask application
    app.run(host=source_ip, debug=True)

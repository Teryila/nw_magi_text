from flask import Flask, request

app = Flask(__name__, template_folder='templates')

# Define your recipient phone numbers
nigeria_number_1 = '+2348100079433'  # Example Nigerian number
nigeria_number_2 = '+2347039630505'  # Example Nigerian number

@app.route('/sms', methods=['POST'])
def receive_sms():
    # Extract necessary information from the incoming SMS
    sender_number = request.form['sender']
    message = request.form['message']

    # Forward the message from Nigerian number to Nigerian number, indicating the origin
    forward_sms(nigeria_number_2, f"From Nigeria ({sender_number}): {message}")

    return 'Message forwarded successfully'

def forward_sms(to_number, message):
    # Here, you would implement the logic to forward the message to the recipient
    # This could involve using an SMS gateway API or a service provided by your mobile carrier

    print(f"Forwarding message to {to_number}: {message}")

if __name__ == '__main__':
    app.run(debug=True)  # Run the Flask application

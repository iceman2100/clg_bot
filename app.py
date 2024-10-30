from flask import Flask, request, render_template, jsonify
import requests

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/send_message', methods=['POST'])
def send_message():
    user_message = request.form['message']  # Get input from the form
    
    # Rasa server endpoint
    rasa_url = 'http://localhost:5005/webhooks/rest/webhook'

    # Prepare the payload for the Rasa server
    payload = {
        "sender": "user",
        "message": user_message
    }

    # Send the request to Rasa server and get response
    response = requests.post(rasa_url, json=payload)
    response_json = response.json()

    # Extract the Rasa response text
    rasa_reply = [msg['text'] for msg in response_json] if response_json else ["No response from Rasa"]

    # Send the reply back to the UI
    return jsonify({"reply": rasa_reply})

if __name__ == '__main__':
    app.run(port=5000, debug=True)

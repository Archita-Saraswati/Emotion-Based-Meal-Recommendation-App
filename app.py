from flask import Flask, render_template, jsonify, request, Response
from emotion_detector import detect_emotion
from flask_mail import Mail, Message
import cv2

app = Flask(__name__)
cap = cv2.VideoCapture(0)

@app.route('/get_live_preview')
def get_live_preview():
    if not cap.isOpened():
        return Response("Camera not available", status=503)
    ret, frame = cap.read()
    if not ret:
        return Response("Unable to read frame", status=500)

    _, buffer = cv2.imencode('.jpg', frame)
    response= Response(buffer.tobytes(), mimetype='image/jpeg')
    response.headers["Cache-Control"] = "no-store"
    return response

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/allrecipe')
def allrecipe():
    return render_template('allrecipe.html')

@app.route('/detect_emotion', methods=['GET'])
def detect_emotion_route():
    emotion, food_item = detect_emotion()
    return jsonify({'emotion': emotion, 'food': food_item})

# Configure Flask-Mail
app.config['MAIL_SERVER'] = 'smtp.gmail.com' 
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'architasaraswati@gmail.com' #email
app.config['MAIL_PASSWORD'] = 'lvhe omil maee udgi' #pass

mail = Mail(app)

@app.route('/send_message', methods=['POST'])
def send_message():
    data = request.json
    user_email = data.get('email')
    app.config['MAIL_USERNAME'] = user_email
    message_content = data.get('message')

    if not user_email or not message_content:
        return jsonify({'error': 'Email & Message are required'}), 400

    try:
        msg = Message(subject="New Message from MoodFork", sender=user_email, recipients=['architasaraswati@gmail.com'], body=f"Message from {user_email}:\n\n{message_content}")

        mail.send(msg)
        return jsonify({'success': 'Message sent successfully!'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
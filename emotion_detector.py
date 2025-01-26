import cv2
import json
from fer import FER
import random
import time

def detect_emotion():
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("Error: Unable to access the camera. Please make sure the camera is connected and not being used by another application.")
        return None, None
    
    detector = FER(mtcnn=True)
    start_time = time.time()  # Start the timer
    emotion_detected = None

    print("Live preview for 5 seconds...")
    while True:
        ret, frame = cap.read()
        if not ret:
            print("Error: Unable to read from the camera.")
            break

        # Show live preview
        cv2.putText(frame, 'Previewing...', (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
        cv2.imshow('Emotion Detection', frame)

        # Break after 5 seconds
        if time.time() - start_time > 5:
            break

        if cv2.waitKey(1) & 0xFF == ord('q'):
            print("Preview cancelled by user.")
            cap.release()
            cv2.destroyAllWindows()
            return None, None

    print("Recording emotions...")
    while True:
        ret, frame = cap.read()
        if not ret:
            print("Error: Unable to read from the camera.")
            break

        # Detect emotions in the frame
        emotions = detector.detect_emotions(frame)
        if emotions:
            emotion_detected = max(emotions[0]['emotions'], key=emotions[0]['emotions'].get)
            cv2.putText(frame, f'Emotion: {emotion_detected}', (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)

        cv2.imshow('Emotion Detection', frame)

        # Break when an emotion is detected or 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord('q') or emotion_detected:
            break

    cap.release()
    cv2.destroyAllWindows()

    if emotion_detected:
        food_item = suggest_food(emotion_detected)
        return emotion_detected, food_item
    return None, None

def suggest_food(emotion):
    with open('emotions_food.json', 'r') as file:
        emotions_food = json.load(file)
    food_items = emotions_food.get(emotion.lower(), ["Water"])
    return random.choice(food_items)

# 🍜 Emotion-Based Meal Recommendation App

This project is a smart web application that detects user emotions using facial recognition and suggests personalized meal recommendations. It provides recipes for suggested dishes and includes a vast recipe database, enhancing the user experience with mood-based food choices.


## ✨ Features

- Emotion-Based Meal Suggestions: Detects user emotions (happy, nostalgic, angry, etc.) and recommends suitable meals.
- Recipe Database: Offers a wide collection of recipes along with preparation instructions.
- Facial Emotion Recognition (FER): Uses deep learning models to analyze emotions from facial expressions.
- Email Features: Sends recommended recipes via email.
- Data Visualization: Provides insights into food preferences based on emotional trends.


## 🛠 Tech Stack

#### Frontend: 
- HTML, CSS, JavaScript
#### Backend:
- Flask (Python)
#### Machine Learning & Data Processing:
- TensorFlow, OpenCV, FaceNet-PyTorch (for emotion recognition)
- Pandas, NumPy, Matplotlib (for data processing & visualization)
#### Additional Libraries:
- Flask-Mail (for email-based features)
- MoviePy, ImageIO (for media handling)




## 🚀 How it works

- Emotion Detection: Captures the user's facial expression and analyzes the emotion.
- Meal Recommendation: Suggests food options based on the detected mood.
- Recipe Retrieval: Fetches and displays a detailed recipe for the suggested meal.
- User Engagement: Allows users to explore a large recipe database and receive recommendations via email.


## 📌 Installation & Setup

Clone the project:

```bash
git clone https://github.com/yourusername/Emotion-Based-Meal-Recommendations-App.git

```

Go to the project directory:

```bash
cd Emotion-Based-Meal-Recommendations-App

```

Install dependencies:

```bash
pip install -r requirements.txt

```

Start the server:

```bash
python app.py
```


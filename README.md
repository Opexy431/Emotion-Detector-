# Emotion Detector Web Application

An AI-powered emotion detection web application built with Python and Flask. The system evaluates text for five key emotions: **anger**, **disgust**, **fear**, **joy**, and **sadness**, and identifies the **dominant emotion**.

---

## 📁 Project Structure

```text
Emotion-Detector-/
├── EmotionDetection/
│   ├── __init__.py               # Package initialization exposing emotion_detector
│   └── emotion_detection.py      # Core emotion detection logic with fallback
├── static/
│   └── mywebscript.js            # Asynchronous frontend client logic
├── templates/
│   └── index.html                # Responsive web interface (Bootstrap 5)
├── server.py                     # Main Flask web application server
├── app.py                        # Entrypoint alias
├── test_emotion_detection.py     # Automated unittest test suite
├── requirements.txt              # Project dependencies
└── README.md                     # Documentation
```

---

## 🚀 Getting Started

### 1. Install Dependencies
Ensure you have Python 3.8+ installed, then install the required packages:

```bash
pip install -r requirements.txt
```

### 2. Run the Application
Start the Flask development server:

```bash
python server.py
```

Then navigate to `http://127.0.0.1:5000/` in your web browser.

---

## 🧪 Testing

Run the automated test suite:

```bash
python -m unittest test_emotion_detection.py
```

### Test Coverage
- **Joy**: `"I am glad this happened"` → `joy`
- **Anger**: `"I am really mad about this"` → `anger`
- **Disgust**: `"I feel disgusted just hearing about this"` → `disgust`
- **Sadness**: `"I am so sad about this"` → `sadness`
- **Fear**: `"I am really afraid that this will happen"` → `fear`
- **Invalid / Blank Input**: `""` → `None`

---

## 🔍 Code Quality & Linting

Verify code quality with Pylint (rated 10/10):

```bash
pylint server.py EmotionDetection/emotion_detection.py EmotionDetection/__init__.py
```

---

## 🌐 API Endpoint

### `GET /emotionDetector?textToAnalyze=<text>`

#### Successful Response:
```text
For the given statement, the system response is 'anger': 0.012, 'disgust': 0.005, 'fear': 0.008, 'joy': 0.965 and 'sadness': 0.010. The dominant emotion is joy.
```

#### Blank / Invalid Input Response:
```text
Invalid text! Please try again!
```

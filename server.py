"""
Emotion Detector Flask Web Server.

This server provides web endpoints to analyze emotions from user-submitted text
and renders an interactive web interface.
"""

from flask import Flask, render_template, request, jsonify
from EmotionDetection import emotion_detector

app = Flask("Emotion Detector")


@app.route("/emotionDetector")
def detect_emotion():
    """
    Analyzes the emotion of the input text provided via query parameter.

    Returns:
        str: Formatted emotion report string or error message.
    """
    text_to_analyze = request.args.get('textToAnalyze', '')
    response = emotion_detector(text_to_analyze)

    if response['dominant_emotion'] is None:
        if request.args.get('format') == 'json':
            return jsonify({'error': 'Invalid text! Please try again!'}), 400
        return "Invalid text! Please try again!"

    # Support JSON format for enhanced frontend visualizations
    if request.args.get('format') == 'json':
        return jsonify(response)

    return (
        f"For the given statement, the system response is 'anger': {response['anger']}, "
        f"'disgust': {response['disgust']}, 'fear': {response['fear']}, "
        f"'joy': {response['joy']} and 'sadness': {response['sadness']}. "
        f"The dominant emotion is {response['dominant_emotion']}."
    )


@app.route("/")
def render_index_page():
    """
    Renders the main index HTML page.
    """
    return render_template('index.html')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

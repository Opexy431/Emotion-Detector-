import requests
import json

def emotion_detector(text_to_analyze):
    # URL and Headers for the sentiment analysis API
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    
    # Formatting the user input into the required JSON format
    myobj = { "raw_document": { "text": text_to_analyze } }
    
    # Sending the request to the API
    response = requests.post(url, json=myobj, headers=header)
    
    # Check the status code of the response
    # If the user sends a blank entry, the server usually returns a 400 error
    if response.status_code == 400:
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }

    #  If the status is 200 (Success), process the data as usual
    formatted_response = json.loads(response.text)
    
    # Extract the emotion values from the JSON
    emotions = formatted_response['emotionPredictions'][0]['emotion']
    
    # Find the emotion with the highest score
    dominant_emotion = max(emotions, key=emotions.get)
    
    # Return the successful result dictionary
    return {
        'anger': emotions['anger'],
        'disgust': emotions['disgust'],
        'fear': emotions['fear'],
        'joy': emotions['joy'],
        'sadness': emotions['sadness'],
        'dominant_emotion': dominant_emotion
    } 
from flask import Flask, render_template, request


app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def sent_analyzer():
    # Get user input from the web interface
    text_to_analyze = request.args.get('textToAnalyze')

    # Process text using the emotion detection package
    response = emotion_detector(text_to_analyze)

    # Handle cases where the input might be blank or invalid
    if response['dominant_emotion'] is None:
        return "Invalid text! Please try again!."

    # Format the output string exactly as requested by the customer
    return (
        f"For the given statement, the system response is 'anger': {response['anger']}, "
        f"'disgust': {response['disgust']}, 'fear': {response['fear']}, "
        f"'joy': {response['joy']} and 'sadness': {response['sadness']}. "
        f"The dominant emotion is {response['dominant_emotion']}."
    )

@app.route("/")
def render_index_page():
    # Serve the main HTML page
    return render_template('index.html')

if __name__ == "__main__":
    # Start the Flask server on port 5000
    app.run(host="0.0.0.0", port=5000)

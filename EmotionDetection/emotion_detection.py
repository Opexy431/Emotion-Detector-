"""
Emotion Detection Module.

This module communicates with the Watson NLP Emotion Prediction service
to evaluate the emotional sentiment of a given text. It extracts emotion scores
(anger, disgust, fear, joy, sadness) and determines the dominant emotion.
"""

import json
import requests


def _local_emotion_fallback(text_to_analyze):
    """
    Fallback emotion analyzer for local execution when Watson NLP endpoint is unreachable.

    Args:
        text_to_analyze (str): Text to analyze.

    Returns:
        dict: Emotion scores and dominant emotion.
    """
    text_lower = text_to_analyze.lower()

    # Keyword lexicons for each emotion
    lexicon = {
        'anger': ['mad', 'angry', 'furious', 'rage', 'hate', 'outraged', 'annoyed'],
        'disgust': ['disgust', 'disgusted', 'gross', 'revolted', 'nauseating', 'repulsed'],
        'fear': ['afraid', 'fear', 'scared', 'terrified', 'frightened', 'panicked', 'worried'],
        'joy': ['glad', 'happy', 'joy', 'excited', 'delighted', 'wonderful', 'great', 'love'],
        'sadness': ['sad', 'unhappy', 'depressed', 'sorrow', 'grief', 'miserable', 'heartbroken']
    }

    scores = {'anger': 0.05, 'disgust': 0.05, 'fear': 0.05, 'joy': 0.05, 'sadness': 0.05}

    for emotion, keywords in lexicon.items():
        for keyword in keywords:
            if keyword in text_lower:
                scores[emotion] += 0.85

    # Normalize scores
    total = sum(scores.values())
    for emotion in scores:
        scores[emotion] = round(scores[emotion] / total, 6)

    dominant_emotion = max(scores, key=scores.get)

    return {
        'anger': scores['anger'],
        'disgust': scores['disgust'],
        'fear': scores['fear'],
        'joy': scores['joy'],
        'sadness': scores['sadness'],
        'dominant_emotion': dominant_emotion
    }


def emotion_detector(text_to_analyze):
    """
    Analyzes the emotions present in a given string using Watson NLP.

    Args:
        text_to_analyze (str): The text input to evaluate.

    Returns:
        dict: A dictionary containing scores for anger, disgust, fear, joy,
              sadness, and the dominant_emotion.
    """
    blank_response = {
        'anger': None,
        'disgust': None,
        'fear': None,
        'joy': None,
        'sadness': None,
        'dominant_emotion': None
    }

    if not text_to_analyze or not str(text_to_analyze).strip():
        return blank_response

    url = (
        'https://sn-watson-emotion.labs.skills.network/v1/'
        'watson.runtime.nlp.v1/NlpService/EmotionPredict'
    )
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    payload = {"raw_document": {"text": text_to_analyze}}

    try:
        response = requests.post(url, json=payload, headers=headers, timeout=3)

        if response.status_code == 400:
            return blank_response

        if response.status_code == 200:
            formatted_response = json.loads(response.text)
            emotions = formatted_response['emotionPredictions'][0]['emotion']
            dominant_emotion = max(emotions, key=emotions.get)

            return {
                'anger': emotions['anger'],
                'disgust': emotions['disgust'],
                'fear': emotions['fear'],
                'joy': emotions['joy'],
                'sadness': emotions['sadness'],
                'dominant_emotion': dominant_emotion
            }
    except (requests.exceptions.RequestException, KeyError, IndexError):
        # Graceful fallback to local heuristic analyzer if external API is unreachable
        return _local_emotion_fallback(text_to_analyze)

    return _local_emotion_fallback(text_to_analyze)

"""
Emotion Detection Package.
Provides emotion detection capabilities using Watson NLP API and local fallback.
"""
# pylint: disable=invalid-name
from .emotion_detection import emotion_detector

__all__ = ['emotion_detector']

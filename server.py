"""
Flask server for Emotion Detection application.

This module handles user input, calls the emotion detection
function, and returns a formatted response.
"""

from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

@app.route("/ping")
def ping():
    return "Server is alive!"


@app.route("/emotionDetector")
def detect_emotion() -> str:
    """
    Handle emotion detection requests from the frontend.

    Returns:
        str: Formatted emotion analysis result or error message.
    """
    text_to_analyze = request.args.get("textToAnalyze")

    # Validate input
    if not text_to_analyze or not text_to_analyze.strip():
        return "Invalid text! Please try again!"

    response = emotion_detector(text_to_analyze)

    # Handle invalid API response
    if response.get("dominant_emotion") is None:
        return "Invalid text! Please try again!"

    formatted_response = (
        "For the given statement, the system response is "
        f"'anger': {response.get('anger')}, "
        f"'disgust': {response.get('disgust')}, "
        f"'fear': {response.get('fear')}, "
        f"'joy': {response.get('joy')}, "
        f"'sadness': {response.get('sadness')}. "
        f"The dominant emotion is "
        f"<b>{response.get('dominant_emotion')}</b>."
    )

    return formatted_response


@app.route("/")
def render_index_page() -> str:
    """
    Render the main application page.

    Returns:
        str: HTML content of index page
    """
    return render_template("index.html")


if __name__ == "__main__":
   # Run the Flask development server.
    app.run(host="0.0.0.0", port=8000, debug=True)

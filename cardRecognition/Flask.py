from flask import Flask, jsonify, request
import base64
import os
from image_detection import cards_from_image
from cardRecognitionAlgorithm import cardRecognitionAlgorithm

app = Flask(__name__)

@app.route('/process', methods=['POST'])
def process():
    encoded_photo = request.form['image']
    decoded_photo = base64.b64decode(encoded_photo)
    with open("images/test.png","wb") as fh:
        fh.write(decoded_photo)
    cards_from_image("images/test.png")
    cardRecognitionAlgorithm()
    # for fileName in os.listdir("detected_cards/"):
    #     os.remove("detected_cards/" + fileName)

    # Create a response
    response = {
        'message': 'Card processed successfully',
    }

    return jsonify(response)


def create_directory(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)


def save_result(result, file_path):
    with open(file_path, "wb") as file:
        file.write(result)


if __name__ == '__main__':
    app.run(host="0.0.0.0")

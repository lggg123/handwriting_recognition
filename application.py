import numpy as np

from flask import (
    Flask, render_template, request,
    redirect, url_for, session
)
from random import choice
from bidict import bidict
from tensorflow import keras

ENCODER = bidict({
    'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6,
    'G': 7, 'H': 8, 'I': 9, 'J': 10, 'K': 11, 'L': 12, 
    'M': 13, 'N': 14, 'O': 15, 'P': 16, 'Q': 17, 'R': 18,
    'S': 19, 'T': 20, 'U': 21, 'V': 22, 'W': 23, 'X': 24,
    'Y': 25, 'Z': 26
})

application = Flask(__name__)
application.secret_key = 'alphabet_quiz'

@application.route('/')
def index():
    # we want to clear the session if not it will show the last letter updated
    # and not the new leter updated
    session.clear()
    return render_template("index.html")

@application.route('/add-data', methods=['GET'])
def add_data_get():
    # send a prompt to the page 
    # draw a 'b'
    # B [0, 0, 0...]
    # labels, images
    message = session.get('message', '')

    # labels = np.load('data/labels.npy', allow_pickle=True)
    count = {k: 0 for k in ENCODER.keys()}
    # for label in labels:
    #     count[label] += 1
    count = sorted(count.items(), key=lambda x: x[1])
    letter = count[0][0]

    # letter = choice(list(ENCODER.keys()))
    return render_template("addData.html", letter=letter, message=message)

@application.route('/add-data', methods=['POST'])
def add_data_post():

    label = request.form['letter']
    labels = np.load('data/labels.npy')
    labels = np.append(labels, label)
    np.save("data/labels.npy", labels)

    pixels = request.form['pixels']
    pixels = pixels.split(',')
    # pixels we must change into an array and a type of float
    img = np.array(pixels).astype(float).reshape(1, 50, 50)
    imgs = np.load('data/images.npy')
    imgs = np.vstack([imgs, img])
    np.save("data/images.npy", imgs)

    session['message'] = f'"{label}" added to the training dataset'

    return redirect(url_for('add_data_get'))

    

@application.route('/practice', methods=['GET'])
def practice_get():

    letter = choice(list(ENCODER.keys()))

    return render_template("practice.html", letter=letter, correct='')

@application.route('/practice', methods=['POST'])
def practie_post():

    letter = request.form['letter']

    pixels = request.form['pixels']
    pixels = pixels.split(',')
    img = np.array(pixels).astype(float).reshape(1, 50, 50, 1)

    # this loads the model from the model.
    model = keras.models.load_model('letter.model')

    # this is the letter prediction from the model and adding the training data.
    pred_letter = np.argmax(model.predict(img), axis=-1)
    pred_letter = ENCODER.inverse[pred_letter[0]]

    # if the letter you wrote == predicted letter 
    correct = 'yes' if pred_letter == letter else 'no'

    letter = choice(list(ENCODER.keys()))

    return render_template("practice.html", letter=letter, correct=correct)

if __name__ == '__main__':
    application.run(debug=True)

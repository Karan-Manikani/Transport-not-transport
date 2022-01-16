import tensorflow as tf
import numpy as np


def get_prediction_and_confidence(image, model):
    img_array = np.array(image)
    img = tf.image.resize(img_array, [224, 224])
    img = tf.expand_dims(img, axis=0)

    prediction = model.predict(img)[0][0]

    if prediction > 0.5:
        class_name = 'Transport'
        confidence = prediction
    else:
        class_name = 'Not Transport'
        confidence = 1 - prediction

    return (class_name, confidence)
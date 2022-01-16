import SessionState
import numpy as np
from PIL import Image
import streamlit as st
from keras.models import load_model
from predict_class import get_prediction_and_confidence



st.title('Transport Prediction App')
st.write('This app will tell you whether the image you uploaded is of a mode of transport or not.')

file = st.file_uploader('Choose a file.', accept_multiple_files = False, type = ['jpg', 'jpeg', 'png'])

session_state = SessionState.get(pred_button = False)

if not file:
	st.warning('Please upload an image')
	st.stop()

else:
    image = Image.open(file)
    st.image(image, use_column_width = True)
    _, _, _, center, _, _, _ = st.columns(7)
    pred_button = center.button('Predict')

if pred_button:
    session_state.pred_button = True

if session_state.pred_button:
    model = load_model('../model/efficientnet_transport.h5')

    class_name, confidence = get_prediction_and_confidence(image, model)

    st.metric('Class Prediction', f'{class_name}')
    st.metric('Class Confidence', '{:.2f} %'.format(confidence * 100))

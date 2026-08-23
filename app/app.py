import streamlit as st
import pickle

model = pickle.load(open('model/model.pkl', 'rb'))

st.title("🩺 Vitamin Deficiency Detection")

fatigue = st.selectbox("Fatigue", [0,1,2,3,4,5])
pale_skin = st.selectbox("Pale Skin", [0,1,2,3,4,5])
hair_loss = st.selectbox("Hair Loss", [0,1,2,3,4,5])
bone_pain = st.selectbox("Bone Pain", [0,1,2,3,4,5])
vision_problem = st.selectbox("Vision Problem", [0,1,2,3,4,5])

if st.button("Predict"):
    prediction = model.predict([[fatigue, pale_skin, hair_loss, bone_pain, vision_problem]])
    st.success(f"Possible Deficiency: {prediction[0]}")
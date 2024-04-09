import streamlit as st
import pickle

clf = pickle.load(open('model.pkl', 'rb'))

def input_function():
    st.title("Placement Prediction Model")

    cgpa = st.text_input("Enter CGPA:")
    iq = st.text_input("Enter IQ:")

    output_box = st.empty()
    result = None

    if cgpa != '' and iq != '':
        try:
            features = [[float(cgpa), float(iq)]]
            result = clf.predict(features)
            if result[0] == 1:
                result = "Yes, you will be placed"
                color = 'green'
            elif result[0] == 0:
                result = "No, you will not be placed"
                color = 'red'
        except ValueError:
            result = "Invalid input"
            color = 'white'

    output_box.text_area("Result", value=result, height=10)


if __name__ == "__main__":
    input_function()

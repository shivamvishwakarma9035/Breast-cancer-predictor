import numpy as np
import pickle
import streamlit as st

# Load the trained model
loaded_model = pickle.load(open('C:/Users/awadh/OneDrive/Desktop/BREAST_CANCER/trained_model.sav', 'rb'))

def breast_pred(input_data):
    # Convert input data to numpy array
    input_data_as_numpy_array = np.asarray(input_data)

    # Reshape the data for prediction (for a single instance)
    input_data_reshaped = input_data_as_numpy_array.reshape(1, -1)

    # Make prediction using the model
    prediction = loaded_model.predict(input_data_reshaped)

    if prediction[0] == 0:
        return 'The Woman has no Breast Cancer...'
    else:
        return 'The Woman has Breast Cancer...'

def get_int_input(label, default_value=0):
    """ Helper function to get integer input from user with default handling """
    user_input = st.text_input(label)
    if user_input == '':
        return default_value
    try:
        return int(user_input)
    except ValueError:
        st.error(f"Invalid input for {label}. Please enter a valid number.")
        return default_value

def get_float_input(label, default_value=0.0):
    """ Helper function to get float input from user with default handling """
    user_input = st.text_input(label)
    if user_input == '':
        return default_value
    try:
        return float(user_input)
    except ValueError:
        st.error(f"Invalid input for {label}. Please enter a valid number.")
        return default_value

def main():
    st.title('Breast Cancer Prediction by God Shivam')
   
    # Input fields for the required columns
    Age = get_int_input('Age')
    Race = get_int_input('Race')
    Marital_Status = get_int_input('Marital Status')
    T_Stage = get_int_input('T Stage')
    N_Stage = get_int_input('N Stage')
    Stage_6 = get_int_input('6th Stage')
    Differentiate = get_int_input('Differentiate')
    Grade = get_int_input('Grade')
    A_Stage = get_int_input('A Stage')
    Tumor_Size = get_float_input('Tumor Size')
    Estrogen_Status = get_int_input('Estrogen Status')
    Progesterone_Status = get_int_input('Progesterone Status')
    Regional_Node_Examined = get_int_input('Regional Node Examined')
    Regional_Node_Positive = get_int_input('Regional Node Positive')
    Survival_Months = get_int_input('Survival Months')
   
    
    # Prediction result placeholder
    Status = ''
    
    if st.button('Breast Test Result'):
        # Passing the inputs into the prediction function
        Status = breast_pred([Age, Race, Marital_Status, T_Stage, N_Stage, Stage_6, Differentiate, 
                                 Grade, A_Stage, Tumor_Size, Estrogen_Status, Progesterone_Status, 
                                 Regional_Node_Examined, Regional_Node_Positive, Survival_Months])
        
    # Display the result of prediction
    st.success(Status)

if __name__ == '__main__':
    main()

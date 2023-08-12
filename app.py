import streamlit as st
import joblib
import numpy as np
# import pickle
import sys
import warnings


# Index(['Sex_female', 'Sex_male', 'Embarked_C', 'Embarked_Q', 'Embarked_S',
#        'Pclass', 'Age', 'SibSp', 'Parch', 'Fare'],

# arr = [[0, 1, 0, 0, 1, 2, 34, 0, 0, 200],]
st.title('will i survive the titanic🛳️?')
st.divider()
st.markdown(
'''
##### - this website uses a ai model trained on the titanic dataset to predict if someone would survive the titanic or not.\n
##### - 👈you can play with these controls to improve the predictions.\n
##### - 👇results are shown below
'''
)
st.divider()

# Sideabar Inputs
gender = st.sidebar.selectbox('gender', ['male', 'female'])
got_on = st.sidebar.selectbox('port', ['cherbourg', 'queenstown', 'southampton'])

married = st.sidebar.selectbox('married', ['yes', 'no'])
siblings = st.sidebar.number_input('siblings', 0, 10)

children = st.sidebar.number_input('children', 0, 10)
parent_on_board = st.sidebar.number_input('parents on board', 0, 2)

pclass = st.sidebar.radio('class', ['first', 'second', 'third'])
age = st.sidebar.slider('age', 0, 100)
fare = st.sidebar.slider('fare', 0, 300)

# Sidebar Decoding

if gender == 'male':
    sex_male, sex_female = 1, 0
elif gender == 'female':
    sex_male, sex_female = 0, 1
else:
    sex_male, sex_female = 0, 0

if got_on == 'cherbourg':
    embarked_c, embarked_q, embarked_s = 1, 0, 0
elif got_on == 'queenstown':
    embarked_c, embarked_q, embarked_s = 0, 1, 0
elif got_on == 'southampton':
    embarked_c, embarked_q, embarked_s = 0, 0, 1
else:
    embarked_c, embarked_q, embarked_s = 0, 0, 0

if pclass == 'first':
    passclass = 1
elif pclass == 'second':
    passclass = 2
elif pclass == 'third':
    passclass = 3
else:
    passclass = 0

if married == 'yes':
    spouse = 1
else:
    spouse = 0

sibsp = spouse+siblings
parch = parent_on_board+children

arr = [[sex_female, sex_male, embarked_c, embarked_q, embarked_s, passclass, age, sibsp, parch, fare]]

def prediction_on_click(arr):
    arr = np.array(arr).reshape(1, -1)
    # print(arr)
    mod = joblib.load('model.sav')
    pred = mod.predict(arr)[0]
    # st.title(f'{pred}')
    # print(pred)
    return pred


if st.sidebar.button('predict'):
    prediction = '🟢yes' if prediction_on_click(arr) else '🏮no'
    st.markdown(f'# {prediction}')
else:
    st.header('*press predict to find out*')

# print(button)
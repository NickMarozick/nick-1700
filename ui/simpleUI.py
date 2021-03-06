import streamlit as st
import requests
import json

st.title("Simple UI to Showcase Named Entity Recognition")

userInput= st.text_input('Input the Text to be Analyzed Here:')

runService = st.button('Run Service!')

#port="8080"

if runService:

# ---- The following requests only run if text is entered  -------------------

  if userInput is not None:
      st.write("User Inputted Text: ", userInput)

# ---- creating a JSON object to send over the user input via an HTTP Post request

      dataInput={}
      dataInput['text']= userInput

      jsonDataInput= json.dumps(dataInput)
      jsonDataInput= eval(jsonDataInput)

      #url= 'http://0.0.0.0:8080/userInput'
      url= 'http://bottleserver:8080/userInput'

      postRequest = requests.post(url, json=jsonDataInput)

#-------- Call to a Get Service that runs the Named Entity Recognition ------------

      #res2= requests.get('http://0.0.0.0:8080/analysis')
      namedEntityResponse=requests.get('http://bottleserver:8080/analysis')

      st.write(namedEntityResponse.text)

#---------- Get Request to Get All User Input ------------------

#res= requests.get('http://localhost:8080/userInput')

#st.write(res.text)

#---------------About Section -----------------------------

expander = st.beta_expander("About")
expander.write("Simple UI built via streamlit to run a service and showcase Named Entity Recognition. Please add text to be analyzed in the box and click the 'Run Service' button to analyze and output the results")

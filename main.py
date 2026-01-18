#pip install --upgrade langchain langchain-google-genai streamlit

#from langchain import LLMChain
from langchain_core.prompts import PromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI


import os

# Set up API keys for OpenAI and Google
os.environ['GOOGLE_API_KEY']  = "AIzaSyBlp6aIvGVTuUp6filB8xP0nDL8f2DEty8"

# Initialize Google's Gemini model
gemini_model = ChatGoogleGenerativeAI(model = "gemini-2.5-flash")

# Create prompt template for generating tweets

tweet_template = "Give me {number} tweets on {topic}"
tweet_prompt = PromptTemplate(template = tweet_template, input_variables = ['number', 'topic'])

# Create LLM chain using the prompt template and model
#tweet_chain = tweet_prompt | gpt4o_mini_model
tweet_chain = tweet_prompt | gemini_model


import streamlit as st

st.header("Tweet Generator")
st.subheader("Generate tweets based on a given topic using Google GenAI and LangChain")

topic = st.text_input("Enter a topic for the tweet:")
number = st.number_input("Enter the number of tweets to generate:", min_value=1, max_value=10, value=1, step=1)

#st.button("Generate Tweets", key="generate_button")

if st.button("Generate Tweets"):
    tweets = tweet_chain.invoke({"number" : number, "topic" : topic})
    st.write(tweets.content)
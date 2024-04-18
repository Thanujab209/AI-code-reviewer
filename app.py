from openai import OpenAI
import streamlit as st

#f = open("D:\Innomatics\OpenAI_handson\.openai_api_key.txt")
key = "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"

client = OpenAI(api_key = key)

st.title("🤖GenAI App - AI Code Reviewer")
st.subheader("🧑An AI Code Reviewer")

prompt = st.text_area("Enter your Python code here...😊")

if st.button("Generate")==True:
    response = client.chat.completions.create(
    model="gpt-3.5-turbo", messages=[
        {"role": "system", "content": """Consider yourself as a code reviewer. Users will submit their Python code for review, give feedback on potential bugs along with suggestions for fixes. You should be user-friendly, efficient, and provide accurate bug reports and fixed code snippets.
""" },{"role": "user", "content" : prompt}
    ]
)
    st.write(response.choices[0].message.content)
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import streamlit as st 
from langchain_core.prompts import PromptTemplate,load_prompt

load_dotenv()

model = ChatOpenAI(model='gpt-4o-mini')

st.header("Research Tool")

paper_input = st.selectbox("Select Research Paper Name",["Attention is all you need","BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding","GPT-3: Language Models are Few-Shot Learners","Diffusion Models Beat GANs on Image Synthesis"])

style_input = st.selectbox("Select Explanation Style",["Bigginer friendly","Technical","Code-oriented","Methematical"])

length_input = st.selectbox("Sselct Explanation Length",["Short(1-2 Paragraphs)","Medium(3-5 Paragraphs)","Long(detailed explanation)"])

template= load_prompt('template.json')

prompt = template.invoke({
    "paper_input":paper_input,
    "style_input":style_input,
    "length_input":length_input
})

if st.button("Send"):
    result = model.invoke(prompt)
    st.write(result.content)
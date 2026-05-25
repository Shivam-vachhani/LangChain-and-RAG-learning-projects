from langchain_huggingface import ChatHuggingFace,HuggingFacePipeline
import os


os.environ['HF_HOME'] = 'C:/LLM models/huggingface_cache'

llm = HuggingFacePipeline.from_model_id(
    model_id="TinyLlama/TinyLlama-1.1B-Chat-v1.0",
    task="text-generation",
    model_kWargs={
        "temperature": 0.3,"max_new_tokens":100}
)

model=ChatHuggingFace(llm = llm)

result = model.invoke("What is the capital of India? and why?")

print(result.content)

# need complex pytorch and gpu setup to run locally 
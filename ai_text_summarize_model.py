# text summarization function using Hugging Face Model 

from huggingface_hub import InferenceClient
from dotenv import load_dotenv

import os

# load dotenv
load_dotenv()

api_key = os.getenv("HUGGINGFACEHUB_API_TOKEN")




def ai_model(raw_data: str):
    client = InferenceClient(
    provider="hf-inference",
    api_key= api_key 
    )
    
    response  = client.summarization(raw_data,model = "facebook/bart-large-cnn")
    
    return response

    


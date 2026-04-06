import os
from pulsar import Client
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from langchain.llms import OpenAI

# Environment configuration setup
ENV = os.getenv('ENV', 'development')

# Pulsar client configuration
PULSAR_BROKER = os.getenv('PULSAR_BROKER', 'localhost:6650')

# LangChain and LLM configuration
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY', 'your-openai-api-key')

# Microservice endpoints
MICROSERVICE_API = os.getenv('MICROSERVICE_API', 'http://localhost:8000/api')

# Prompt template for LangChain
prompt = PromptTemplate(
    input_variables=['question'],
    template='Answer the question: {question}.
'
)

llm = OpenAI(openai_api_key=OPENAI_API_KEY)
chain = LLMChain(llm=llm, prompt=prompt)

# Function to get Pulsar client
def get_pulsar_client():
    return Client(PULSAR_BROKER)

# Function to query LangChain model
def query_model(question):
    return chain.run(question=question)

# Function to call microservice API
def call_microservice(endpoint, data):
    import requests
    response = requests.post(endpoint, json=data)
    return response.json()

if __name__ == '__main__':
    print(f'Environment: {ENV}')
    print(f'Pulsar Broker: {PULSAR_BROKER}')
    print(f'LangChain API Key: {OPENAI_API_KEY}')
    print(f'Microservice API: {MICROSERVICE_API}')
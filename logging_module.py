import logging
from pulsar import Client
from langchain.callbacks import LangChainTracer

# Initialize logging configuration
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    filename='app.log'
)

# Pulsar client for message logging
class PulsarLogger:
    def __init__(self, topic):
        self.client = Client('pulsar://localhost:6650')
        self.producer = self.client.createProducer(topic=topic)

    def log(self, message):
        self.producer.send(b'Log message: ' + message.encode('utf-8'))
        logging.info(f'Logged via Pulsar: {message}')

# LangChain logging integration
class LangChainLogger:
    def __init__(self):
        self.tracer = LangChainTracer()
        self.tracer._set_project('quick-scripts')

    def log(self, message):
        self.tracer.log(message)
        logging.info(f'Logged via LangChain: {message}')

# Example usage
def main():
    pulsar_logger = PulsarLogger('persistent-logs')
    langchain_logger = LangChainLogger()

    pulsar_logger.log('This is a test log message via Pulsar.')
    langchain_logger.log('This is a test log message via LangChain.')

if __name__ == '__main__':
    main()
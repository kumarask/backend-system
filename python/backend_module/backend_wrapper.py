from backend_cpp import Queue, Producer, Consumer

class BackendWrapper:
    def __init__(self):
        self.queue = Queue()
        self.producer = Producer(self.queue)
        self.consumer = Consumer(self.queue)

    def start(self):
        self.producer.start()
        self.consumer.start()

    def stop(self):
        self.producer.stop()
        self.consumer.stop()

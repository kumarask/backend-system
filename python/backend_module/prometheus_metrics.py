from prometheus_client import Counter, Gauge, start_http_server

queue_size_gauge = Gauge("queue_current_size", "Current size of the queue")
messages_produced = Counter("messages_produced", "Messages produced")
messages_consumed = Counter("messages_consumed", "Messages consumed")

def start_metrics_server(port=8001):
    start_http_server(port)

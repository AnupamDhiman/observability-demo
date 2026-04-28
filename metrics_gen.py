import time
import random
from prometheus_client import start_http_server, Counter, Histogram

# Metrics definition
REQUEST_COUNT = Counter('http_requests_total', 'Total HTTP Requests', ['method', 'endpoint', 'status'])
REQUEST_LATENCY = Histogram('http_request_duration_seconds', 'HTTP Request Latency', ['endpoint'])

def process_request():
    # Simulate different endpoints
    endpoint = random.choice(['/api/v1/users', '/api/v1/orders', '/health'])
    
    # Simulate status codes (errors for /api/v1/orders)
    if endpoint == '/api/v1/orders' and random.random() < 0.2:
        status = '500'
    else:
        status = '200'
        
    # Observe latency
    latency = random.uniform(0.1, 0.5)
    if endpoint == '/api/v1/users':
        latency += random.uniform(0.1, 1.0) # Users is slower
    
    REQUEST_LATENCY.labels(endpoint=endpoint).observe(latency)
    REQUEST_COUNT.labels(method='GET', endpoint=endpoint, status=status).inc()

if __name__ == '__main__':
    # Start Prometheus metrics server
    start_http_server(8000)
    print("Mock App metrics server started on port 8000")
    
    while True:
        process_request()
        time.sleep(random.uniform(0.5, 2.0))

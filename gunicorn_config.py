# Gunicorn configuration file
bind = "0.0.0.0:5000"
workers = 4
threads = 2
timeout = 120
keepalive = 5
errorlog = "error.log"
accesslog = "access.log"
loglevel = "info"
worker_class = "sync"
max_requests = 1000
max_requests_jitter = 50 
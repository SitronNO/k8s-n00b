from flask import Flask, render_template, url_for
from redis import Redis, RedisError
import os
import socket
import datetime

# Connect to Redis
redis = Redis(host=os.getenv("REDIS_SERVER", "localhost"), db=0, decode_responses=True, socket_connect_timeout=2, socket_timeout=2)

app = Flask(__name__)

def genTable(redis, hostname):
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    if redis.exists(hostname):
        redis.hset(hostname, "last_seen", now)
        redis.hincrby(hostname, "counter", 1)
    else:
        redis.hset(hostname, "first_seen", now)
        redis.hset(hostname, "last_seen", now)
        redis.hset(hostname, "counter", 1)

    servers = []
    for key in redis.scan_iter():
        temp_dict = redis.hgetall(key)
        temp_dict['hostname'] = key
        servers.append(temp_dict)

    return servers

@app.route("/")
def hello():

    try:
        visits = redis.ping()
        server_data = genTable(redis, socket.gethostname())
    except RedisError:
        redis_html = "Cannot connect to Redis"
        return render_template('error.html', hostname=socket.gethostname(), redis_html=redis_html)

    return render_template('redis.html', hostname=socket.gethostname(), server_list=server_data)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)

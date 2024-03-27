from server.server import *
import random


def generate_servers(servers_num, tickets_file):
    servers = []
    for _ in range(servers_num):
        max_requests_per_time = random.randint(1, 10)
        max_concurrent_requests = random.randint(1, 10)
        requests_threshold_delay = random.randint(1, 2)
        servers.append(Server(tickets_file, max_requests_per_time, requests_threshold_delay, max_concurrent_requests))
    return servers

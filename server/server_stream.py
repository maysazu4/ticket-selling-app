from server.server import *
import random


def generate_servers(servers_num, tickets_file):
    """
    Generate a list of servers with random configurations.

    Args:
        servers_num (int): The number of servers to generate.
        tickets_file (str): The file path of the tickets file.

    Returns:
        list: A list of Server objects with random configurations.
    """
    servers = []
    for _ in range(servers_num):
        max_requests_per_time = random.randint(1, 10)
        max_concurrent_requests = random.randint(1, 10)
        requests_threshold_delay = random.randint(1, 2)
        servers.append(Server(tickets_file, max_requests_per_time, requests_threshold_delay, max_concurrent_requests))
    return servers

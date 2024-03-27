from Load_balancer.load_balancer import LoadBalancer
from request_stream.request_stream import RequestGenerator
from server.server_stream import generate_servers


def main():
    request_generator = RequestGenerator()
    servers = generate_servers(5,"database/tickets.json")
    load_balancer = LoadBalancer(request_generator, servers)
    load_balancer.process_events()


if __name__ == "__main__":
    main()

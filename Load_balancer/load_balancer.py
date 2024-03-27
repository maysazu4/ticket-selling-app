from request_stream.request_stream import RequestGenerator
from server.server_stream import generate_servers

class LoadBalancer:
    def __init__(self, event_generator,servers):
        self.event_generator = event_generator
        self.servers = servers

    def get_Least_Connections_server(self):
        min_curr_req = self.servers[0].requests_count
        result = self.servers[0]
        for server in self.servers:
            if server.requests_count < min_curr_req:
                min_curr_req = server.requests_count
                result = server
        return result

    def process_events(self):
        for event in self.event_generator.generate_events():
            self.handle_event(event)

    def handle_event(self, event):
        # Here you can implement any logic to process the event
        print("Received event:", event)
        for _ in range(event['tickets']):
            server = self.get_Least_Connections_server()
            server.sell_ticket(event['event'])
            server.process_request(event['event'])

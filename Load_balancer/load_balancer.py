from request_stream.request_stream import RequestGenerator

class LoadBalancer:
    """Load balancer class responsible for distributing incoming events to servers.
    """

    def __init__(self, event_generator, servers):
        """Initialize the LoadBalancer.
        Args:
            event_generator (RequestGenerator): An instance of the RequestGenerator class responsible for generating events.
            servers (list): A list of server instances to which events will be distributed.
        """
        self.event_generator = event_generator
        self.servers = servers

    def get_Least_Connections_server(self):
        """Get the server with the least number of current requests based on the least connections algo
        Returns:
            Server: The server instance with the least number of current requests.
        """
        min_curr_req = self.servers[0].requests_count
        result = self.servers[0]
        for server in self.servers:
            if server.requests_count < min_curr_req:
                min_curr_req = server.requests_count
                result = server
        return result

    def process_events(self):
        """Process events generated by the event generator and distribute them to servers."""
        for event in self.event_generator.generate_events():
            self.handle_event(event)

    def handle_event(self, event):
        """Handle a single event by distributing it to a server with the least number of current requests.

        param:
            event (dict): The event to be handled, containing information about the event and the number of tickets.
        """
        print("Received event:", event)
        for _ in range(event['tickets']):
            server = self.get_Least_Connections_server()
            server.sell_ticket(event['event'])
            server.process_request(event['event'])

from request_stream import RequestGenerator

class LoadBalancer:
    def __init__(self, event_generator):
        self.event_generator = event_generator

    def process_events(self):
        for event in self.event_generator.generate_events():
            self.handle_event(event)

    def handle_event(self, event):
        # Here you can implement any logic to process the event
        print("Received event:", event)

# Example usage:
if __name__ == "__main__":
    request_generator = RequestGenerator()
    load_balancer = LoadBalancer(request_generator)

    load_balancer.process_events()

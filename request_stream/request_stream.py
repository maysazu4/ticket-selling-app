import random
import time

class RequestGenerator:
    """Class for generating events with random timestamps, events, and ticket counts.
    Attributes:
        events_range (tuple): A tuple representing the range of events to generate.
        time_range (tuple): A tuple representing the range of time intervals between event generation (in seconds).
        event_list (list): A list of event types to choose from when generating events.

    """

    def __init__(self):
        """Initialize the RequestGenerator.
        The RequestGenerator is initialized with default ranges for the number of events to generate
        and the time intervals between event generation, as well as a list of event types.
        """
        self.events_range = (1, 5)  # Range of events to generate
        self.time_range = (0.5, 2)  # Range of time intervals between event generation (in seconds)
        self.event_list = ["Concert", "Sports Game", "Theater Show", "Movie Premiere"]

    def generate_events(self):
        """Generate events with random timestamps, events, and ticket counts indefinitely.
        Yields:
            dict: A dictionary representing an event, including its timestamp, event type, and number of tickets.
        """
        while True:
            num_events = random.randint(*self.events_range)
            for _ in range(num_events):
                timestamp = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
                event = random.choice(self.event_list)
                tickets = random.randint(1, 10)  # Assuming a ticket range from 1 to 10
                yield {"timestamp": timestamp, "tickets": tickets, "event": event}
            time.sleep(random.uniform(*self.time_range))

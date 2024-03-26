import json
import time

class Server:
    def __init__(self, tickets_file, max_requests_per_time=5, requests_threshold_delay=2, max_concurrent_requests=3):
        with open(tickets_file, 'r') as f:
            self.tickets_db = json.load(f)
        self.requests_count = 0
        self.requests_time = time.time()
        self.max_requests_per_time = max_requests_per_time
        self.requests_threshold_delay = requests_threshold_delay
        self.max_concurrent_requests = max_concurrent_requests
        self.current_concurrent_requests = 0

    def sell_ticket(self, event):
        if event not in self.tickets_db or self.tickets_db[event] <= 0:
            print(f"No tickets available for {event}.")
            return False
        if self.current_concurrent_requests >= self.max_concurrent_requests:
            raise Exception("Server overloaded. Please try again later.")
        self.current_concurrent_requests += 1
        self.tickets_db[event] -= 1
        print(f"Sold 1 ticket for {event}. Remaining: {self.tickets_db[event]}")
        self.current_concurrent_requests -= 1
        return True

    def show_unsold_tickets(self):
        print("Unsold tickets:")
        for event, tickets in self.tickets_db.items():
            if tickets > 0:
                print(f"{event}: {tickets} tickets available.")

    def process_request(self, event):
        # Check if the number of requests exceeds the threshold
        self.requests_count += 1
        if self.requests_count > self.max_requests_per_time:
            current_time = time.time()
            elapsed_time = current_time - self.requests_time
            if elapsed_time < 10:  # Y time unit (adjust as needed)
                print("Too many requests. Delaying response.")
                time.sleep(self.requests_threshold_delay)
            else:
                self.requests_time = current_time
                self.requests_count = 1
        # Simulate processing time
        time.sleep(0.5)
        self.current_concurrent_requests -= 1

# Example usage:
if __name__ == "__main__":
    server = Server("tickets.json", max_requests_per_time=10, requests_threshold_delay=3, max_concurrent_requests=5)

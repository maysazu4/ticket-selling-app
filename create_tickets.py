import json
import random
import uuid
# Create a dictionary to store tickets by event type
organized_tickets = {
    "Concert": [],
    "Sports Game": [],
    "Theater Show": [],
    "Movie Premiere": []
}


# Generate tickets and add them to the appropriate event type
for _ in range(500):
    event_type = random.choice(list(organized_tickets.keys()))
    
    ticket = {
        "id": str(uuid.uuid4()),
        "price": round(random.uniform(20, 200), 2),
        "event": event_type,
        "is_sold": False
    }
    organized_tickets[event_type].append(ticket)

# Write organized tickets to a JSON file
with open("tickets.json", "w") as file:
    json.dump(organized_tickets, file, indent=4)

print("Tickets have been created and saved to 'organized_tickets.json'.")
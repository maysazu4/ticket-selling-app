import json
import random

def delete_one_ticket(event_type, file_path):
    # Load tickets from the JSON file
    with open(file_path, 'r') as file:
        tickets_db = json.load(file)

    # Get the list of tickets for the specified event type
    event_tickets = tickets_db[event_type]

    # Delete a ticket
    deleted_ticket = event_tickets.pop()

    # Update the tickets database
    with open(file_path, 'w') as file:
        json.dump(tickets_db, file, indent=4)



def load_tickets(file_path):
    # Load tickets from the JSON file
    with open(file_path, 'r') as file:
        tickets_db = json.load(file)
    return tickets_db

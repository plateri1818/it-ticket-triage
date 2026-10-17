import json
import os

def load_tickets(filepath):
    if not os.path.exists(filepath):
        print(f"Error: {filepath} not found.")
        return []
    with open(filepath, 'r') as f:
        return json.load(f)

def triage_ticket(ticket):
    description = ticket.get("description", "").lower()

    if "network" in description or "wifi" in description or "internet" in description:
        category = "Network"
        priority = "High"
    elif "password" in description or "login" in description or "access" in description:
        category = "Access Control"
        priority = "Medium"
    else:
        category = "Hardware/General"
        priority = "Low"

    ticket["category"] = category
    ticket["priority"] = priority
    return ticket

if __name__ == "__main__":
    tickets = load_tickets("data/sample_tickets.json")
    triaged = [triage_ticket(t) for t in tickets]
    print(json.dumps(triaged, indent=4))
    
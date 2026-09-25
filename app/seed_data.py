"""
Run this script to wipe and reseed the database with sample data:
    python app/seed_data.py
"""
from datetime import datetime
from uuid import uuid4

from app.database import db

NOW = datetime.utcnow()


def make_id():
    return str(uuid4())


# ---- Users (customers + support agents) ----
users = [
    {"id": make_id(), "name": "Aisha Khan", "email": "aisha@example.com", "role": "customer", "created_at": NOW},
    {"id": make_id(), "name": "Ravi Verma", "email": "ravi@example.com", "role": "customer", "created_at": NOW},
    {"id": make_id(), "name": "Meera Nair", "email": "meera@example.com", "role": "customer", "created_at": NOW},
    {"id": make_id(), "name": "Support Agent - Priya", "email": "priya.support@example.com", "role": "support_agent", "created_at": NOW},
    {"id": make_id(), "name": "Support Agent - Arjun", "email": "arjun.support@example.com", "role": "support_agent", "created_at": NOW},
    {"id": make_id(), "name": "Admin User", "email": "admin@example.com", "role": "admin", "created_at": NOW},
]

# ---- Categories ----
categories = [
    {"id": make_id(), "name": "Order Issue", "description": "Problems with placing or tracking an order", "created_at": NOW},
    {"id": make_id(), "name": "Payment Problem", "description": "Failed, duplicate, or incorrect payments", "created_at": NOW},
    {"id": make_id(), "name": "Shipping Delay", "description": "Order shipped late or stuck in transit", "created_at": NOW},
    {"id": make_id(), "name": "Product Defect", "description": "Item received damaged or not as described", "created_at": NOW},
    {"id": make_id(), "name": "Refund Request", "description": "Customer requesting a refund or return", "created_at": NOW},
    {"id": make_id(), "name": "Account Issue", "description": "Login, password, or account access problems", "created_at": NOW},
]

customers = [u for u in users if u["role"] == "customer"]
agents = [u for u in users if u["role"] == "support_agent"]

# ---- Tickets ----
tickets = [
    {
        "id": make_id(),
        "title": "Order not delivered after 10 days",
        "description": "My order #ORD-1042 shows 'shipped' but tracking hasn't updated in a week.",
        "category_id": categories[2]["id"],
        "order_id": "ORD-1042",
        "status": "in_progress",
        "created_by": customers[0]["id"],
        "assigned_to": agents[0]["id"],
        "created_at": NOW,
        "updated_at": NOW,
    },
    {
        "id": make_id(),
        "title": "Charged twice for the same order",
        "description": "I see two charges of $49.99 on my card for order #ORD-1050.",
        "category_id": categories[1]["id"],
        "order_id": "ORD-1050",
        "status": "new",
        "created_by": customers[1]["id"],
        "assigned_to": None,
        "created_at": NOW,
        "updated_at": NOW,
    },
    {
        "id": make_id(),
        "title": "Received a broken headphone set",
        "description": "The left earcup arrived cracked. Requesting a replacement.",
        "category_id": categories[3]["id"],
        "order_id": "ORD-1061",
        "status": "assigned",
        "created_by": customers[2]["id"],
        "assigned_to": agents[1]["id"],
        "created_at": NOW,
        "updated_at": NOW,
    },
    {
        "id": make_id(),
        "title": "Refund not processed after return",
        "description": "Returned item 12 days ago, refund still not showing in my account.",
        "category_id": categories[4]["id"],
        "order_id": "ORD-1039",
        "status": "on_hold",
        "created_by": customers[0]["id"],
        "assigned_to": agents[0]["id"],
        "created_at": NOW,
        "updated_at": NOW,
    },
    {
        "id": make_id(),
        "title": "Cannot log into my account",
        "description": "Password reset email never arrives.",
        "category_id": categories[5]["id"],
        "order_id": None,
        "status": "resolved",
        "created_by": customers[1]["id"],
        "assigned_to": agents[1]["id"],
        "created_at": NOW,
        "updated_at": NOW,
    },
    {
        "id": make_id(),
        "title": "Wrong item shipped",
        "description": "Ordered a blue jacket, received a red one instead.",
        "category_id": categories[0]["id"],
        "order_id": "ORD-1077",
        "status": "closed",
        "created_by": customers[2]["id"],
        "assigned_to": agents[0]["id"],
        "created_at": NOW,
        "updated_at": NOW,
    },
    {
        "id": make_id(),
        "title": "Payment declined but amount deducted",
        "description": "Checkout said payment failed, but my bank shows the amount was deducted.",
        "category_id": categories[1]["id"],
        "order_id": "ORD-1083",
        "status": "new",
        "created_by": customers[0]["id"],
        "assigned_to": None,
        "created_at": NOW,
        "updated_at": NOW,
    },
    {
        "id": make_id(),
        "title": "Package stuck in customs",
        "description": "Tracking shows the package has been in customs for 5 days.",
        "category_id": categories[2]["id"],
        "order_id": "ORD-1090",
        "status": "in_progress",
        "created_by": customers[1]["id"],
        "assigned_to": agents[1]["id"],
        "created_at": NOW,
        "updated_at": NOW,
    },
]

# ---- Comments ----
comments = [
    {"id": make_id(), "ticket_id": tickets[0]["id"], "author_id": agents[0]["id"], "message": "We've contacted the courier for an update.", "created_at": NOW},
    {"id": make_id(), "ticket_id": tickets[2]["id"], "author_id": agents[1]["id"], "message": "Replacement has been dispatched.", "created_at": NOW},
    {"id": make_id(), "ticket_id": tickets[4]["id"], "author_id": agents[1]["id"], "message": "Password reset link resent manually. Issue resolved.", "created_at": NOW},
    {"id": make_id(), "ticket_id": tickets[3]["id"], "author_id": customers[0]["id"], "message": "Still no refund showing after a week.", "created_at": NOW},
    {"id": make_id(), "ticket_id": tickets[0]["id"], "author_id": customers[0]["id"], "message": "Any update on this?", "created_at": NOW},
    {"id": make_id(), "ticket_id": tickets[5]["id"], "author_id": agents[0]["id"], "message": "Correct jacket has been reshipped, tracking sent via email.", "created_at": NOW},
    {"id": make_id(), "ticket_id": tickets[7]["id"], "author_id": agents[1]["id"], "message": "Reached out to the shipping partner for clearance status.", "created_at": NOW},
    {"id": make_id(), "ticket_id": tickets[1]["id"], "author_id": customers[1]["id"], "message": "Please refund the duplicate charge as soon as possible.", "created_at": NOW},
]

# ---- Attachments ----
attachments = [
    {"id": make_id(), "ticket_id": tickets[2]["id"], "filename": "broken_headphones.jpg", "uploaded_by": customers[2]["id"], "uploaded_at": NOW},
    {"id": make_id(), "ticket_id": tickets[5]["id"], "filename": "wrong_item_received.jpg", "uploaded_by": customers[2]["id"], "uploaded_at": NOW},
    {"id": make_id(), "ticket_id": tickets[1]["id"], "filename": "bank_statement.pdf", "uploaded_by": customers[1]["id"], "uploaded_at": NOW},
    {"id": make_id(), "ticket_id": tickets[3]["id"], "filename": "return_receipt.pdf", "uploaded_by": customers[0]["id"], "uploaded_at": NOW},
    {"id": make_id(), "ticket_id": tickets[6]["id"], "filename": "payment_error_screenshot.png", "uploaded_by": customers[0]["id"], "uploaded_at": NOW},
    {"id": make_id(), "ticket_id": tickets[0]["id"], "filename": "tracking_screenshot.png", "uploaded_by": customers[0]["id"], "uploaded_at": NOW},
    {"id": make_id(), "ticket_id": tickets[7]["id"], "filename": "customs_notice.pdf", "uploaded_by": customers[1]["id"], "uploaded_at": NOW},
    {"id": make_id(), "ticket_id": tickets[4]["id"], "filename": "login_error.png", "uploaded_by": customers[1]["id"], "uploaded_at": NOW},
]

# ---- Audit logs ----
audit_logs = [
    {"id": make_id(), "action": "ticket_created", "entity_type": "ticket", "entity_id": t["id"], "performed_by": t["created_by"], "timestamp": NOW}
    for t in tickets
]


def seed_collection(name, records):
    collection = db[name]
    result = collection.delete_many({})
    if records:
        collection.insert_many(records)
    print(f"{name}: cleared {result.deleted_count} old record(s), inserted {len(records)} new record(s)")


if __name__ == "__main__":
    seed_collection("users", users)
    seed_collection("categories", categories)
    seed_collection("tickets", tickets)
    seed_collection("comments", comments)
    seed_collection("attachments", attachments)
    seed_collection("audit_logs", audit_logs)
    print("\nSeeding complete.")

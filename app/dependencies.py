from app.database import db


def get_users_collection():
    return db["users"]


def get_categories_collection():
    return db["categories"]


def get_tickets_collection():
    return db["tickets"]


def get_comments_collection():
    return db["comments"]


def get_attachments_collection():
    return db["attachments"]


def get_audit_logs_collection():
    return db["audit_logs"]

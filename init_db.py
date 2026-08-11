from database import create_tables, seed_rooms

if __name__ == "__main__":
    create_tables()
    seed_rooms()
    print("Database initialized successfully.")
    print("Created: users and rooms tables.")

import sqlite3
from datetime import datetime

class FitnessCenter:
    def __init__(self, db_name='fitness_center.db'):
        self.db_name = db_name
        self.setup_database()
    
    def setup_database(self):
        """Initialize the database with required tables"""
        with sqlite3.connect(self.db_name) as conn:
            # Create tables
            conn.executescript('''
                DROP TABLE IF EXISTS WorkoutSessions;
                DROP TABLE IF EXISTS Members;
                
                CREATE TABLE Members (
                    id INTEGER PRIMARY KEY,
                    name VARCHAR(255) NOT NULL,
                    age INTEGER
                );
                
                CREATE TABLE WorkoutSessions (
                    session_id INTEGER PRIMARY KEY,
                    member_id INTEGER,
                    session_date DATE,
                    session_time VARCHAR(50),
                    activity VARCHAR(255),
                    FOREIGN KEY (member_id) REFERENCES Members(id)
                );
            ''')
            conn.commit()
    
    def add_member(self, name, age):
        """Add a new member to the database"""
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute('INSERT INTO Members (name, age) VALUES (?, ?)', (name, age))
            conn.commit()
            return cursor.lastrowid
    
    def schedule_workout(self, member_id, date, time, activity):
        """Schedule a new workout session"""
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute('''
                INSERT INTO WorkoutSessions (member_id, session_date, session_time, activity)
                VALUES (?, ?, ?, ?)
            ''', (member_id, date, time, activity))
            conn.commit()
            return cursor.lastrowid
    
    def view_member_workouts(self, member_id):
        """View all workouts for a specific member"""
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute('''
                SELECT m.name, ws.session_date, ws.session_time, ws.activity
                FROM WorkoutSessions ws
                JOIN Members m ON ws.member_id = m.id
                WHERE m.id = ?
                ORDER BY ws.session_date
            ''', (member_id,))
            return cursor.fetchall()
    
    def list_all_members(self):
        """List all members in the database"""
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM Members')
            return cursor.fetchall()

# Example usage
if __name__ == "__main__":
    # Create fitness center instance
    fc = FitnessCenter()
    
    # Add sample members
    jane_id = fc.add_member("Jane Doe", 29)
    john_id = fc.add_member("John Smith", 35)
    alice_id = fc.add_member("Alice Brown", 42)
    
    # Schedule workouts
    fc.schedule_workout(jane_id, "2024-11-20", "Morning", "Yoga")
    fc.schedule_workout(john_id, "2024-11-21", "Afternoon", "Weight Training")
    fc.schedule_workout(alice_id, "2024-11-22", "Evening", "Cardio")
    
    # Print all members
    print("\nAll Members:")
    for member in fc.list_all_members():
        print(f"ID: {member[0]}, Name: {member[1]}, Age: {member[2]}")
    
    # Print Jane's workouts
    print(f"\nJane's Workouts:")
    for workout in fc.view_member_workouts(jane_id):
        print(f"Name: {workout[0]}, Date: {workout[1]}, Time: {workout[2]}, Activity: {workout[3]}")

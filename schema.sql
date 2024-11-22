-- Fitness Center Database Schema

-- Drop tables if they exist (in correct order due to foreign key constraints)
DROP TABLE IF EXISTS WorkoutSessions;
DROP TABLE IF EXISTS Members;

-- Create Members table
CREATE TABLE Members (
    id INT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    age INT
);

-- Create WorkoutSessions table
CREATE TABLE WorkoutSessions (
    session_id INT PRIMARY KEY,
    member_id INT,
    session_date DATE,
    session_time VARCHAR(50),
    activity VARCHAR(255),
    FOREIGN KEY (member_id) REFERENCES Members(id)
);

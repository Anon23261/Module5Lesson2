-- Fitness Center Database Operations

-- Task 1: SQL Data Insertion
-- Insert records into the Members table
INSERT INTO Members (id, name, age) VALUES
(1, 'Jane Doe', 29),
(2, 'John Smith', 35),
(3, 'Alice Brown', 42);

-- Insert records into the WorkoutSessions table
INSERT INTO WorkoutSessions (session_id, member_id, session_date, session_time, activity) VALUES
(101, 1, '2024-11-20', 'Morning', 'Yoga'),
(102, 2, '2024-11-21', 'Afternoon', 'Weight Training'),
(103, 3, '2024-11-22', 'Evening', 'Cardio');

-- Task 2: SQL Data Update
-- Update workout session time for Jane Doe (change from 'Morning' to 'Evening')
UPDATE WorkoutSessions
SET session_time = 'Evening'
WHERE member_id = (SELECT id FROM Members WHERE name = 'Jane Doe');

-- Task 3: SQL Data Deletion
-- Step 1: Delete workout sessions related to John Smith
DELETE FROM WorkoutSessions 
WHERE member_id = (SELECT id FROM Members WHERE name = 'John Smith');

-- Step 2: Delete John Smith's record from the Members table
DELETE FROM Members 
WHERE name = 'John Smith';

# Fitness Center Database Management System

A robust SQL-based database management system for fitness centers, implementing core DML (Data Manipulation Language) operations.

## Overview

This project demonstrates the implementation of a fitness center database system with functionality for managing member records and workout sessions. It includes SQL scripts for creating tables, inserting data, updating records, and handling membership cancellations.

## Features

- Member management (addition, modification, deletion)
- Workout session tracking
- Data integrity maintenance through foreign key relationships
- Comprehensive DML operations demonstration

## Database Structure

### Members Table
```sql
CREATE TABLE Members (
    id INT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    age INT
);
```

### WorkoutSessions Table
```sql
CREATE TABLE WorkoutSessions (
    session_id INT PRIMARY KEY,
    member_id INT,
    session_date DATE,
    session_time VARCHAR(50),
    activity VARCHAR(255),
    FOREIGN KEY (member_id) REFERENCES Members(id)
);
```

## Usage

1. Execute the table creation scripts
2. Run the data insertion scripts to populate initial data
3. Use the update and delete scripts as needed for maintenance

## Scripts Included

- `schema.sql`: Database schema creation
- `operations.sql`: DML operations (INSERT, UPDATE, DELETE)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

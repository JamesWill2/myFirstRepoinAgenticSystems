# Understanding Relational Databases in AI Systems

## Q1. Explain Why databases are important in real-world AI systems?

Databases are essential in AI systems because they store and manage large amounts of structured data that AI models rely on for training, prediction, and analysis.Real-world AI systems continuously collect and process data from different sources, and databases provide an organized way to store this information.

For example:
- User data in recommendation systems
- Medical records in healthcare AI systems
- Transaction data in fraud detection
- Sensor data in IoT and robotics

Structured storage is important because it ensures that data is organized in tables with defined relationships. 
This allows fast querying, efficient analysis, and consistent data management, which are critical for training AI models and making accurate predictions.

## Q2. Describe the relational database mental model

In a relational database, data is organized into tables, which consist of rows and columns.

- Table: Represents a collection of related data (e.g., Users table).
- Row: Represents a single record or entry in the table.
- Column: Represents a specific attribute or property of the record.

Example:

| User_ID | Name  | Email            |
|--------|------|------------------|
| 1      | rahul | rahule@email.com |
| 2      | john   | johnb@email.com   |

Each table should represent one entity. 
For example:
- Users table : stores user information.
- Orders table : stores order information.

This separation helps avoid duplication and keeps the database organized.

## Q3. Explain the concept of a primary key

A primary key is a column (or combination of columns) that uniquely identifies each record in a table.

Properties of a primary key:
- Must be unique
- Cannot contain NULL values

Example:

| User_ID (Primary Key)| Name |
|----------------------|------|
| 1                    |Rahul |
| 2                    |John  |

Here, User_ID is the primary key because each user has a unique identifier.

Primary keys are important because they ensure that every record can be uniquely identified and referenced from other tables.

## Q4. What is a database schema?

A database schema is the structure or blueprint of a database. It defines how data is organized and how tables relate to each other.

A schema typically includes:
- Table names
- Column names and data types
- Primary keys
- Foreign keys
- Constraints

Example schema for a Users table:

Users
User_ID (INT, Primary Key)
Name (VARCHAR)
Email (VARCHAR)


Schemas are important because they maintain consistency and integrity of data in the database and ensure that data follows a predefined structure.

## Q5. Explain how relationships between tables work in relational databases?

In relational databases, tables are connected using foreign keys.

A foreign key is a column in one table that references the primary key of another table.

Example:

### Users Table

| User_ID | Name |
|--------|------ |
| 1      |Kavita |
| 2      |Mahima|

### Orders Table

| Order_ID| User_ID | Product |
|---------|-------- |-------- |
| 101     | 1       |  Laptop |
| 102     | 2       |  Phone  |

Here:
- `User_ID` in the "Orders table" is a "foreign key"
- It references `User_ID` in the "Users table"

This relationship allows us to connect users with their orders.

For example, we can query:
- Which user placed an order
- How many orders a user has made

These relationships help maintain data integrity and allow complex queries across multiple tables.
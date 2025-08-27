# Student Management System

## Overview

This project is a simple FastAPI application that provides a student management system. It allows users to create, read, update, and delete student records. The application uses SQLModel for database operations and includes authentication and authorization features.

## Features

- Create, read, update, and delete student records
- Authentication and authorization using HTTP Basic
- Database operations using SQLModel
- Logging of requests to a log file

## Requirements

- Python 3.7+
- FastAPI
- Uvicorn (for running the API)
- SQLModel (for database operations)

## Installation

1. Install the required packages: pip install -r requirements.txt
2. Run the application: uvicorn app.main:app 

## Usage

1. Create a new student record: POST /students/ with name, age, email, and grades in the request body
2. Get all student records: GET /students/
3. Get a specific student record: GET /students/{student_id}
4. Update a student record: PUT /students/{student_id} with name, age, email, and grades in the request body
5. Delete a student record: DELETE /students/{student_id}

## Authentication

The application uses HTTP Basic authentication. To access the endpoints, you need to provide a valid username and password in the Authorization header.

## Logging

The application logs all requests to a log file named log_file.log in the logs directory.

## API Documentation

The API documentation is available at http://localhost:8000/docs. You can use the documentation to test the API endpoints.
# Contact Manager API

## Overview
This project is a simple contact management API built using FastAPI and SQLModel. It provides endpoints for creating, reading, updating, and deleting contacts, and includes JWT-based authentication and middleware for logging IP addresses.

## Features
*   Contact management: create, read, update, delete contacts
*   Authentication: JWT-based authentication
*   Middleware: logs IP addresses of every request
*   CORS: enabled for all origins

## Requirements
*   Python 3.7+
*   FastAPI
*   Uvicorn (for running the API)
*   SQLModel (for database operations)
*   python-jose (for JWT authentication)

## Installation
1.  Install the required packages: `pip install -r requirements.txt`
2.  Run the application: `uvicorn app.main:app --reload`

## Usage
1.  Create a new contact: `POST /contacts/` with `name`, `email`, and `phone` in the request body
2.  Get all contacts: `GET /contacts/`
3.  Update a contact: `PUT /contacts/{id}` with `name`, `email`, and `phone` in the request body
4.  Delete a contact: `DELETE /contacts/{id}`
5.  Login: `POST /auth/login` with `username` and `password` in the request body

## API Documentation

The API documentation is available at http://localhost:8000/docs. You can use the documentation to test the API endpoints.
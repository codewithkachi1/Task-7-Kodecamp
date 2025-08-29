# Job Application Tracker

## Overview
This project is a simple job application tracker built using FastAPI. It provides endpoints for managing job applications and includes authentication and error handling features.

## Features
*   Job application management: create, read, search applications
*   Authentication: JWT token authentication
*   Error handling: invalid queries are handled and return error messages
*   Middleware: rejects requests if User-Agent header is missing

## Requirements
*   Python 3.7+
*   FastAPI
*   Uvicorn (for running the API)
*   SQLModel (for database operations)
*   python-jose (for JWT authentication)

## Installation
1.  Install the required packages: `pip install -r requirements.txt`
2.  Run the application: `uvicorn app.main:app`

## Usage
1.  Create a new job application: `POST /applications/` with `company`, `position`, `status`, and `date_applied` in the request body
2.  Get all job applications: `GET /applications/`
3.  Search job applications by status: `GET /applications/search?status=pending`

## API Documentation
The API documentation is available at http://localhost:8000/docs. You can use the documentation to test the API endpoints.
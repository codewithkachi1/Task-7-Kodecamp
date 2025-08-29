# Notes API

## Overview
This project is a simple notes management API built using FastAPI. It provides endpoints for creating, reading, and deleting notes, and includes middleware for counting and logging requests.

## Features
*   Note management: create, read, delete notes
*   Middleware: counts total requests made and logs them
*   File storage: saves notes to notes.json
*   CORS: allows multiple origins

## Requirements
*   Python 3.7+
*   FastAPI
*   Uvicorn (for running the API)
*   SQLModel (for database operations)

## Installation
1.  Install the required packages: `pip install -r requirements.txt`
2.  Run the application: `uvicorn app.main:app`

## Usage
1.  Create a new note: `POST /notes/` with `title` and `content` in the request body
2.  Get all notes: `GET /notes/`
3.  Get a single note: `GET /notes/{id}`
4.  Delete a note: `DELETE /notes/{id}`

## API Documentation
The API documentation is available at http://localhost:8000/docs. You can use the documentation to test the API endpoints.
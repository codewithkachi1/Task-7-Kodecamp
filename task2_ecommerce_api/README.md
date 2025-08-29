# E-Commerce API

## Overview

This project is a simple e-commerce API built using FastAPI. It provides endpoints for managing products, cart, and users. The API uses SQLModel for database operations and includes JWT authentication for users.

## Features

- Product management: create, read products
- Cart management: add products to cart, checkout
- User authentication: login, generate JWT token
- Middleware: measure response time and add it to headers
- Orders are saved to orders.json for backup

## Requirements

- Python 3.7+
- FastAPI
- Uvicorn (for running the API)
- SQLModel (for database operations)
- python-jose (for JWT authentication)

## Installation

1. Install the required packages: pip install -r requirements.txt
2. Run the application: uvicorn app.main:app 

## Usage

1. Create a new product: POST /admin/products/ with name, price, and stock in the request body
2. Get all products: GET /products/
3. Add product to cart: POST /cart/add/ with product_id and quantity in the request body
4. Checkout: POST /cart/checkout/
5. Login: POST /users/login/ with username and password in the request body

## API Documentation

The API documentation is available at http://localhost:8000/docs. You can use the documentation to test the API endpoints.
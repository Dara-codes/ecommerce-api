# E-commerce Product API

## Project Overview

This project is an E-commerce Product API built using Django and Django REST Framework (DRF). The API supports product management, user authentication, and search functionality for an e-commerce platform.

## Features

- **Product Management (CRUD):**
  - Create, Read, Update, and Delete products.
  - Attributes: Name, Description, Price, Category, Stock Quantity, Image URL, Created Date.
- **User Management:**
  - Register, Login, Logout endpoints.
  - Token-based authentication using Django REST Framework's JWT.
- **Product Search and Filters:**
  - Search products by Name or Category.
  - Filter products by Category, Price Range, and Stock Availability.
  - Pagination for search results.
- **Error Handling:**
  - Proper HTTP status codes for errors (e.g., 404, 400).

## Installation

### Prerequisites

- Python 3.8+
- Django 4.0+
- Django REST Framework

## API Endpoints

### Authentication

- **Register**: `POST /api/register/`
- **Login**: `POST /api/token/` (returns access and refresh tokens)
- **Refresh Token**: `POST /api/token/refresh/`
- **Logout**: Custom endpoint (if implemented)

### Products

- **List Products**: `GET /api/products/`
- **Create Product**: `POST /api/products/`
- **Retrieve Product**: `GET /api/products/<id>/`
- **Update Product**: `PUT /api/products/<id>/`
- **Delete Product**: `DELETE /api/products/<id>/`

### Search and Filter

- **Search by Name/Category**: `GET /api/products/?search=<query>`
- **Filter by Category/Price/Stock**: `GET /api/products/?category=<category>&min_price=<min>&max_price=<max>&in_stock=True`

## Deployment

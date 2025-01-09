# E-commerce Platform API

## Overview

This project is an e-commerce platform developed using Django for the backend. The project includes a custom user model, product and category management, and features like searching, filtering, and pagination.

## Key Features

- **Custom User Model**: A user model based on `AbstractUser` with an email field that is unique.
- **Product Management**: Create, retrieve, update, and delete products.
- **Category Management**: Organize products into categories.
- **Authentication**: JWT-based authentication for secure user management.
- **Searching, Filtering, and Pagination**: Advanced options to query products by name, category, stock, and price range.
- **All Products View**: A public endpoint to view products with pagination.

## Current Focus

### What Has Been Implemented

1. **Custom User Model**:

   - A `CustomUser` model extending `AbstractUser` with unique email.
   - Fully integrated into the project as the user model.

2. **Product and Category Models**:

   - Models for managing products and categories with appropriate fields and relationships.

3. **Product ViewSet**:

   - Provides CRUD operations for products.
   - Includes filtering by category, stock, and price range.
   - Includes search functionality for product names and categories.
   - Pagination to limit the number of products per page.

4. **Authentication**:

   - JWT-based authentication using `djangorestframework-simplejwt`.
   - Access and refresh tokens are implemented and tested.

5. **Public Product View**:

   - A separate viewset to list all products for unauthenticated users.

### Current Work

- Debugging errors related to token authentication and 500/401 responses when creating products.
- Ensuring the `CustomUser` model is consistently used across the project to avoid conflicts with the built-in `User` model.
- Updating the `README` to align with project progress and maintain accuracy.

## API Endpoints

### Authentication Endpoints

1. **Register**: `POST /api/register/`
2. **Login**: `POST /api/token/`
3. **Token Refresh**: `POST /api/token/refresh/`

### Product Endpoints

1. **Create Product**: `POST /api/products/` (Authenticated)
2. **List Products**: `GET /api/products/`
3. **Search Products**: `GET /api/products/?search=<query>`
4. **Filter Products**: `GET /api/products/?min_price=<value>&max_price=<value>`
5. **Pagination**: `GET /api/products/?page=<number>`
6. **Public Product View**: `GET /api/allproducts/` (Unauthenticated)

### Category Endpoints

1. **List Categories**: `GET /api/categories/`
2. **Create Category**: `POST /api/categories/` (Authenticated)

## How to Set Up and Run the Project

### Prerequisites

- Python 3.10+
- Django 4.x
- Postman or any API testing tool
- Virtual environment (optional but recommended)

### Authentication Testing

1. **Register**:

   - Endpoint: `POST /api/register/`
   - Body:
     ```json
     {
       "username": "testuser",
       "email": "testuser@example.com",
       "password": "password123"
     }
     ```

2. **Login**:

   - Endpoint: `POST /api/token/`
   - Body:
     ```json
     {
       "username": "testuser",
       "password": "password123"
     }
     ```
   - Response includes `access` and `refresh` tokens.

3. **Use Access Token**:

   - Include the token in headers for authenticated endpoints:
     ```
     Authorization: Bearer <access_token>
     ```

### Product Management Testing

1. **Create Product**:

   - Endpoint: `POST /api/products/`
   - Requires authentication.
   - Body:
     ```json
     {
       "name": "Example Product",
       "description": "A sample product description.",
       "price": 19.99,
       "category": 1,
       "stock_quantity": 100,
       "image_url": "http://example.com/image.jpg"
     }
     ```

2. **List Products**:

   - Endpoint: `GET /api/products/`

3. **Search and Filter**:

   - Search by name or category:
     ```
     /api/products/?search=example
     ```
   - Filter by price range:
     ```
     /api/products/?min_price=10&max_price=50
     ```

4. **Pagination**:

   - Default page size is 10.
   - Query with:
     ```
     /api/products/?page=2
     ```

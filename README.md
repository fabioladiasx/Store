# Product and Category Management API

A REST API built with **FastAPI** and **SQLite** to manage products and categories.

## Features

- Create, read, update, and delete products (CRUD).
- Create, read, update, and delete categories.
- Store data using an SQLite database.
- Validate request data using Pydantic schemas.
- Enable CORS for frontend integration.

## Technologies

- Python
- FastAPI
- SQLite
- Uvicorn
- Pydantic

## Project Structure

```text
project-folder/
├── main.py
├── database.py
├── schemas.py
├── store.db
└── README.md
```

*Note: `store.db` is an example filename; check `database.py` for the actual database location and name.*

## Installation and Setup

### 1. Open the project

Open your project folder in Visual Studio Code and open a new terminal.

### 2. Create a virtual environment

**macOS/Linux:**

```bash
python3 -m venv .venv
source .venv/bin/activate
```

**Windows:**

```powershell
py -m venv .venv
.venv\Scripts\Activate.ps1
```

### 3. Install dependencies

```bash
python -m pip install fastapi uvicorn
```

### 4. Start the API

If your application file is named `main.py`, run:

```bash
uvicorn main:app --reload
```

Replace `main` with your Python filename if it is different.

### 5. Open the API documentation

- API root: http://127.0.0.1:8000/
- Interactive documentation: http://127.0.0.1:8000/docs
- Alternative documentation: http://127.0.0.1:8000/redoc

## API Endpoints

### Products

| Method | Endpoint | Description |
|---|---|---|
| POST | `/products` | Create a product |
| GET | `/products` | Get all products |
| GET | `/products/{product_id}` | Get a product by ID |
| PUT | `/products/{product_id}` | Update a product |
| DELETE | `/products/{product_id}` | Delete a product |

### Categories

| Method | Endpoint | Description |
|---|---|---|
| POST | `/categories` | Create a category |
| GET | `/categories` | Get all categories |
| GET | `/categories/{category_id}` | Get a category by ID |
| PUT | `/categories/{category_id}` | Update a category |
| DELETE | `/categories/{category_id}` | Delete a category |

## Example Requests

### Create a category

**POST `/categories`**

```json
{
  "name": "Produce"
}
```

### Create a product

**POST `/products`**

Create the category first, then use its actual ID for `category_id`.

```json
{
  "name": "Apples",
  "description": "Fresh red apples",
  "price": 3.99,
  "stock": 20,
  "category_id": 1
}
```

### Update a product

**PUT `/products/1`**

```json
{
  "name": "Green Apples",
  "description": "Fresh green apples",
  "price": 4.49,
  "stock": 15,
  "category_id": 1
}
```

The product update endpoint requires the fields defined by `ProductCreate` in your current code.

### Update a category

**PUT `/categories/1`**

```json
{
  "name": "Fresh Produce"
}
```

### Delete a product

**DELETE `/products/1`**

Replace `1` with the ID of the product to delete.

## Database

The application uses SQLite through the `get_connection()` and `create_tables()` functions in `database.py`.

The expected tables are:

**Categories**
- `id`
- `name`

**Products**
- `id`
- `name`
- `description`
- `price`
- `stock`
- `category_id`

The `category_id` field associates each product with a category.

## Troubleshooting

- Make sure the FastAPI server is running.
- Check that the database tables exist.
- Create a category before creating a product that references it.
- Ensure request bodies match the Pydantic schemas in `schemas.py`.
- Use `/docs` to test endpoints.

**Important:** Fix the category update endpoint in your Python code. The SQL should use `UPDATE categories SET name = ? WHERE id = ?`, without a trailing comma. Also change the route parameter to `/categories/{category_id}` to match the function argument.

## Future Improvements

- Add consistent HTTP error responses.
- Improve database connection handling.
- Add automated tests.
- Build a frontend for managing products and categories.
- Restrict CORS origins before deploying publicly.

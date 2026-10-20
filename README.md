# Inventory Dashboard — Burgundy Edition

A simple inventory management project with a **FastAPI backend** and a responsive HTML frontend. The dashboard lets you manage products and categories from one interface, with a clean, minimalist design in burgundy, warm ivory, white, and soft blush.

## Features

### Frontend

- Minimalist, responsive dashboard layout
- Burgundy accent palette:
  - Burgundy: `#762C46`
  - Deep wine / hover: `#552033`
  - Soft blush: `#F3E7EC`
  - Warm ivory background: `#FBFAF7`
- Product management form for creating and editing products
- Product table with name search and category filtering
- Category management form and category table
- Product and category edit and delete actions
- Stock indicators that remain green when inventory is available and red when stock is zero
- Refresh button to reload data from the API
- Tailwind CSS loaded from its CDN

### Backend

- FastAPI API
- SQLite database integration through `database.py`
- Request schemas imported from `schemas.py`
- Product and category CRUD operations
- CORS middleware for frontend-to-backend requests

> **Note:** The frontend expects the API to be running at `http://127.0.0.1:8000`. The backend must implement the endpoints listed below for the dashboard features to work.

## Requirements

- Python 3.9 or newer
- FastAPI
- Uvicorn
- SQLite (included with standard Python installations)
- A modern web browser
- Internet access when using the Tailwind CSS CDN

## Project Structure

Your project may be organized like this:

```text
inventory-dashboard/
├── main.py          # FastAPI application
├── database.py      # SQLite connection and table setup
├── schemas.py       # Pydantic request models
├── index.html       # Burgundy dashboard frontend
├── store.db         # SQLite database (created by the app, if configured)
└── README.md
```

Use the filenames in your own project if they differ from this example.

## Run the Backend

1. Open the project folder in Visual Studio Code or a terminal.
2. (Recommended) Create a virtual environment:

   ```bash
   python -m venv .venv
   ```

3. Activate it.

   **macOS/Linux:**

   ```bash
   source .venv/bin/activate
   ```

   **Windows:**

   ```bash
   .venv\Scripts\activate
   ```

4. Install the dependencies:

   ```bash
   pip install fastapi uvicorn
   ```

5. Start the server. If your FastAPI file is named `main.py`, run:

   ```bash
   uvicorn main:app --reload
   ```

6. Open the API documentation:

   - Swagger UI: <http://127.0.0.1:8000/docs>
   - ReDoc: <http://127.0.0.1:8000/redoc>

If your Python file has a different name, replace `main` with that filename without `.py`.

## Open the Frontend

1. Save the latest burgundy HTML as `index.html` in your frontend/project folder.
2. Make sure the backend is running at `http://127.0.0.1:8000`.
3. Open `index.html` in your browser.
4. Use **Refresh All Data** to load products and categories.

The HTML frontend uses this API base URL:

```javascript
const API_BASE = "http://127.0.0.1:8000";
```

If you change the backend address or port, update `API_BASE` in the HTML file as well.

## API Endpoints Used by the Frontend

The frontend sends requests to these routes:

| Method | Endpoint | Purpose |
|---|---|---|
| `GET` | `/categories` | Load all categories |
| `POST` | `/categories` | Create a category |
| `PUT` | `/categories/{category_id}` | Update a category |
| `DELETE` | `/categories/{category_id}` | Delete a category |
| `GET` | `/products` | Load all products |
| `POST` | `/products` | Create a product |
| `PUT` | `/products/{product_id}` | Update a product |
| `DELETE` | `/products/{product_id}` | Delete a product |

The frontend expects category objects to include `id` and `name`. Product objects are expected to include `id`, `name`, `description`, `price`, `stock`, and `category_id`.

### Example product request body

```json
{
  "name": "Wireless Mouse",
  "description": "Wireless ergonomic mouse",
  "price": 29.99,
  "stock": 100,
  "category_id": 1
}
```

### Example category request body

```json
{
  "name": "Electronics"
}
```

The selected `category_id` must correspond to a category that exists in the database.

## How to Use the Dashboard

### Products

1. Open the **Products Management** tab.
2. Enter the product name and description.
3. Enter its price and stock quantity.
4. Choose a category.
5. Select **Save Product**.
6. Use the search field or category filter to find products.
7. Select **Edit** to load a product into the form, or **Delete** to remove it after confirming.

### Categories

1. Open the **Category Management** tab.
2. Enter a category name.
3. Select **Save Category**.
4. Use **Edit** to rename a category or **Delete** to remove it.

### Troubleshooting

- **Products or categories do not load:** Check that FastAPI is running and that the API URL is `http://127.0.0.1:8000`.
- **Browser reports a CORS error:** Check the backend's CORS middleware configuration and ensure it allows the frontend origin during development.
- **Product cannot be saved:** Confirm all required fields are filled in and the selected category exists.
- **Styles do not appear:** The frontend loads Tailwind CSS from a CDN, so check your internet connection.
- **A route returns 404 or 405:** Compare your FastAPI route paths and HTTP methods with the endpoint table above.

## Development Notes

- The burgundy styling is contained in the HTML `<style>` block and uses CSS custom properties for its color palette.
- Product and category data are retrieved from the backend; the HTML file does not replace the database.
- For production, restrict CORS to trusted frontend origins instead of allowing every origin.
- Confirm that database tables are created by your backend's table-initialization code before using the dashboard.

## License

This project is for learning and practice. Add a license if you plan to distribute it publicly.

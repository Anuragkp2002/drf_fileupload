# User Data Processing API

## Overview
This Django REST Framework (DRF) API allows users to upload a CSV file containing user data. The API validates and processes the CSV file, storing valid user records in the database and providing a detailed response about the processing results.

## Features
- Upload CSV files containing user details.
- Validate required fields (`name`, `email`, `age`).
- Ensure uniqueness of `email` before saving.
- Return a summary of processed records, including success and failure counts.
- Provide error details for rejected records.

## Technologies Used
- Python
- Django
- Django REST Framework
- Pandas
- SQLite 

## Installation

1. Clone the repository:
   ```sh
   git clone https://github.com/Anuragkp2002/drf_fileupload.git
   cd drf_fileupload
   ```
2. Create a virtual environment and activate it:
   ```sh
   python -m venv venv
   venv\Scripts\activate  # On Linux use: source venv/bin/activate
   ```
3. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```
4. Apply migrations:
   ```sh
   python manage.py migrate
   ```
5. Run the development server:
   ```sh
   python manage.py runserver
   ```

## API Endpoints

### Upload User Data (CSV)
**Endpoint:** `POST /usercreation_api/`

**Request:**
- Upload a CSV file with the following columns: `name`, `email`, `age`.

**Example Request:**
```sh
curl -X POST http://127.0.0.1:8000/usercreation_api/ \n    -H "Content-Type: multipart/form-data" \n    -F "file=@users.csv"
```

**Response:**
```json
{
    "totalrecords": 100,
    "successfullrecords": 80,
    "rejectedrecords": 20,
    "errors": [
        {
            "data": {"name": "John Doe", "email": "invalid_email", "age": 30},
            "errors": {"email": ["Enter a valid email address."]}
        }
    ]
}
```



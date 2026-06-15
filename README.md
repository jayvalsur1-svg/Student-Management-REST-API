# Student Management REST API

A RESTful API built with FastAPI for managing student records. The system supports CRUD operations, academic performance analysis, automatic percentage calculation, CGPA generation, grade classification, and subject-wise performance tracking.

## Features

✅ Add Student Records

✅ View All Students

✅ Retrieve Student by ID

✅ Update Student Information

✅ Delete Student Records

✅ Automatic Percentage Calculation

✅ CGPA Calculation

✅ Grade Classification

✅ Top Subject Identification

✅ Data Validation with Pydantic

✅ Interactive API Documentation

---

## Technologies Used

* Python
* FastAPI
* Pydantic V2
* JSON Storage
* REST APIs

---

## Student Model

```json
{
  "id": "S001",
  "name": "Luffy",
  "grade_level": 6,
  "subjects": {
    "Maths": 90,
    "Science": 85,
    "English": 88
  }
}
```

---

## Computed Fields

The API automatically calculates:

### Percentage

```text
Percentage = (Obtained Marks / Total Marks) × 100
```

### CGPA

```text
CGPA = Percentage / 10
```

### Grade Status

| Percentage | Grade |
| ---------- | ----- |
| 0 - 43     | Pass  |
| 44 - 55    | D     |
| 56 - 65    | C     |
| 66 - 75    | B     |
| 76 - 85    | A     |
| 86 - 99    | S     |

### Top Subject

The highest-scoring subject is automatically identified.

---

## API Endpoints

### Home

```http
GET /
```

### View All Students

```http
GET /view
```

### Get Student By ID

```http
GET /student/{id}
```

### Add Student

```http
POST /add
```

### Update Student

```http
PUT /update/{id}
```

### Delete Student

```http
DELETE /delete/{id}
```

---

## Validation Rules

### Student ID

Must start with:

```text
S00
```

Example:

```text
S001
S002
S003
```

### Subject Marks

Valid range:

```text
0 - 100
```

Any value outside this range will be rejected.

---

## Installation

Clone the repository:

```bash
git clone <repository-url>
cd student-management-api
```

Install dependencies:

```bash
pip install fastapi uvicorn pydantic
```

Run the application:

```bash
uvicorn main:App --reload
```

---

## API Documentation

Swagger UI:

```text
http://127.0.0.1:8000/docs
```

ReDoc:

```text
http://127.0.0.1:8000/redoc
```

---

## Concepts Demonstrated

* REST API Development
* CRUD Operations
* FastAPI Framework
* Pydantic Validation
* Computed Fields
* Data Modeling
* JSON Data Persistence
* Backend Development
* Error Handling

---

## Future Improvements

* SQLite/PostgreSQL Integration
* Authentication & Authorization
* Student Ranking System
* Search and Filtering
* Pagination
* Docker Support
* Unit Testing
* Cloud Deployment

---

## Author

Jay Valsur

Python Developer | FastAPI Enthusiast | Backend Development Learner

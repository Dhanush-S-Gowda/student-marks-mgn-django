# Student Marks Management System

## Overview

Student Marks Management System is a Django web application that allows CRUD (Create, Read, Update, Delete) operations on student records. It provides functionalities to manage student information including names, IDs, marks for five subjects, and calculates their percentage automatically.

## Features

- **Create:** Add new students with their name, ID, and marks for five subjects.
- **Read:** View a list of all students along with their details and calculated percentage.
- **Update:** Modify existing student information including name, ID, and subject marks.
- **Delete:** Remove students from the database.

## Technologies Used

- **Python:** Django web framework
- **Database:** SQLite (default for Django)
- **Frontend:** HTML, Bootstrap 5

## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/Dhanush-S-Gowda/student-marks-mgn-django.git
   cd your_repository```
   
2. **Setup Virtual Environment:**

   ```bash
   # Create virtual environment
    python -m venv venv
    # Activate virtual environment
    # On Windows
    venv\Scripts\activate
    # On macOS/Linux
    source venv/bin/activate```
   
3. Install Dependencies:

  ```bash
  pip install -r requirements.txt
```

4. Run Migrations:

  ```bash
  python manage.py migrate
```

5. Start the Development Server:

  ```bash
python manage.py runserver
```
The application will be accessible at http://localhost:8000/.


## Usage

- Navigate to http://localhost:8000/ in your web browser to access the application.
- Use the provided form to add, update, or delete student records.
- The list of students and their details are displayed in a tabular format.

## License

This project is licensed under the MIT License - see the [LICENSE.md] file for details.



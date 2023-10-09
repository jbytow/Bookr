# Bookr
Bookr is a web application developed as a part of the "Web Development with Django" book. It serves an online book repository with reviews and reading tracker for each user.

## Features

* Display Books: Browse through a wide range of books and view their details
* Search for Books: Search for books based on title/author
* Reviews: Write, edit and view latest book reviews.
* Publishers: Display and edit publishers
* REST Api: Added to the app
* User Accounts: Register, login and tracks your book read on your profile and download reading history in excel file

## Built With
* Python
* Django
* Django REST Framework
* HTML
* Bootstrap
* Javascript

## Installation
1. Clone the Repository
```bash
git clone https://github.com/jbytow/bookr.git
```

2. Setup Virtual Environment
```bash
python -m venv venv
source venv/bin/activate  # For Linux/macOS
venv\Scripts\activate  # For Windows
```

3. Install Dependencies
```bash
pip install -r requirements.txt
```

4. Run Migrations
```bash
python manage.py migrate
```

5. Start the Development Server
```bash
python manage.py runserver
```

Open your browser and navigate to http://127.0.0.1:8000/ to see the application in action.
    
## License

[MIT](https://choosealicense.com/licenses/mit/)

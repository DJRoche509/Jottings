# Jottings -- Where Jotting Remains Simply Easy 
<h6> Your new favorite Note app 📝</h6>
<br/> 

Jottings is a simple web application built with Flask, allowing users to jot down notes and manage their tasks efficiently. This minimalistic app provides an intuitive interface to add, edit, and delete notes effortlessly.
<br/><br/>

## Table of Contents
* Features
* Screenshots
* Installation
* Usage
* Technologies Used
* Future Enhancements
* Contributing
* License
  
<br/>
  
## Features
* **User-Friendly Interface:** Clean and intuitive design for smooth user experience.
* **Add Notes:** Add new notes with a title and timestamp.
* **DateTime Stamps Notes:** Create all note records with dates and UTC time (CST)
* **Edit Notes:** Modify existing notes easily.
* **Delete Notes:** Remove unwanted notes from your list.
* **Flash Messages:** Receive confirmation messages for successful operations.
<br/>

## Screenshots
- App folder structure

```
  Jottings/
  │
  ├── __pycache__/                    # Compiled Python files (ignored by version control)
  ├── .gitignore                      # Configuration file to specify files/folders to be ignored by Git
  ├── .vscode/                        # Visual Studio Code configuration folder
  ├── app/                            # Main application package
  │   ├── __pycache__/                # Compiled Python files specific to the app package
  │   ├── static/                     # Folder for static assets (CSS, JavaScript)
  │   │   ├── handleFlashMessage.js   # JavaScript file for handling flash messages
  │   │   └── styles.css              # Custom CSS styles for the application
  │   ├── templates/                  # HTML templates for rendering views
  │   │   ├── addNote.html            # Template for adding a new note
  │   │   ├── base.html               # Base template containing common structure (header, flash messages, etc.)
  │   │   ├── deleteNote.html         # Template for deleting a note
  │   │   ├── editNote.html           #     "     "  editing  "   " 
  │   │   └── index.html              #     "     " displaying the list of notes
  │   ├── __init__.py                 # Initialization file for the Flask application
  │   ├── forms.py                    # Flask-WTF forms definitions (form classes)
  │   ├── models.py                   # Database models (Task class definition)
  │   └── routes.py                   # Flask routes and view functions
  ├── instance/                       # Instance folder (contains sensitive or environment-specific data)
  │    └── data.db                    # SQLite database file (ignored by version control)
  ├── .env                            # Environment variables file (contains sensitive data, not in version control)
  ├── launch.json                     # Configuration file for launching the app in a specific way (IDE-specific)
  ├── .venv/                          # Virtual environment folder (contains Python dependencies, not in version control)
  ├── config.py                       # Configuration settings for the app
  ├── requirements.txt                # List of Python dependencies (generated via pip freeze)
  └── run.py                          # Entry point to run the Flask app
```
<br>
  
  - App Home page after adding a few notes
    <br/> <br/>
    <img alt="Pic showing AddNote button triggered " src="https://github.com/DJRoche509/Jottings/assets/100164051/aca3a21f-dc25-443f-90cb-f9d1a4a25e1e"  height="650" width="500">
  <br/><br/>
  
  - Showing preview for a delete Confirmation request operation
    <br/> <br/>
    <img alt="Pic showing AddNote button triggered " src="https://github.com/DJRoche509/Jottings/assets/100164051/0453a5b8-581a-45c3-be5c-e2396592ad45"   height="400" width="500">
  
<br/><br/>

## Installation
1. Clone the Repository:
  ```
    git clone https://github.com/DJRoche509/Jottings.git
  ```
2. Create a Virtual Environment (for Windows users):
  ```
    cd jottings
    python -m venv venv
  ```
3. Activate the Virtual Environment:
  * Windows:
    ```
      venv\Scripts\activate
    ```
  * Linux/macOS:
    ```
      source venv/bin/activate
    ```
4. Install Dependencies:
  ```
    pip install -r requirements.txt
  ```
5. Set Up the Database:
   Run the Flask shell:
  ```
    flask shell
  ```
   Inside the shell, create the database tables:
  ```
    from app.models import db, Task
    from datetime import datetime, timezone, timedelta
    from app import app 
    with app.app_context():
        db.create_all()
 
    exit()
  ```
6. Run the Application:
  ```
    flask run
  ```
The app will be accessible at `http://localhost:5000` by default.
<br/><br/>

## Usage
1. <span style="font-size:bold"> Homepage:</span>
    * View all your notes on the homepage.
    * Each note displays its title and the date it was created.
2. Adding a Note:
    * Click on "Add a Note" to create a new note.
    * Enter the title of your note and click "Submit."
    * A confirmation message will appear at the top.
3. Editing a Note:

    * Click "Edit" next to the note you want to modify.
    * Update the title and click "Submit."
    * The note will be updated, and a confirmation message will appear.
4. Deleting a Note:
    * Click "Delete" next to the note you want to remove.
    * A confirmation dialog will appear. Click "Delete" to confirm.
    * The note will be deleted, and a confirmation message will appear.
<br/><br/>

## Technologies Used
  * **Flask:** Lightweight web framework for Python.
  * **Flask-SQLAlchemy:** Flask extension for working with SQL databases.
  * **Flask-WTF:** Flask extension for handling web forms.
  * **Jinja2:** Template engine for Python.
  * **SQLite:** Embedded relational database management system.
  * **jQuery:** JavaScript library for DOM manipulation.
<br/><br/>

## Future Enhancements
* **Authentication and Authorization:** I plan to implement user authentication and authorization features, allowing users to securely log in, manage their own notes, and ensure data privacy.

<br/>

## Contributing
Contributions are welcome! Please follow these steps to contribute:

1. Fork the repository.
2. Create a new branch: `git checkout -b feature/your-feature-name`.
3. Make your changes and commit them: `git commit -m 'Add a new feature'`.
4. Push to the branch: `git push origin feature/your-feature-name`.
5. Submit a pull request.
<br/><br/>

## License
This project is licensed under the MIT License.

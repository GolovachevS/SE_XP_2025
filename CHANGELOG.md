# Changelog

## [v0.1.0] — 2025-10-22
### 🎉 Initial Release — MVP

This is the first public release of the **Homework Submission Web App** — a minimal working prototype (MVP).

#### ✨ Features
- **User roles:** Student and Teacher.
- **Authentication:** registration, login, and logout.
- **Homework uploads:** students can send homework files to a selected teacher.
- **Teacher dashboard:** teachers can view all submitted works, download files, and provide feedback.
- **Grading:** teachers can assign grades and leave comments.
- **Student dashboard:** students can view grades, feedback, and submission status.
- **Basic UI:** responsive interface built with Bootstrap 5.
- **SQLite database + migrations:** for lightweight data persistence.

#### 🧩 Tech stack
- Python 3.12 + Flask
- SQLAlchemy + Flask-Migrate
- WTForms
- Bootstrap 5
- SQLite (local)
  
#### 🚀 Notes
This release is intended for demonstration and educational purposes (XP pair project).  
Files are stored locally in the `uploads/` folder.  
Future releases will add:
- Automated CI/CD workflow via GitHub Actions  
- Cloud storage integration  
- Deployment to Render or Fly.io  
- Automatic testing and grading logic

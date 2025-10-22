# Homework Submission Web App

A lightweight web platform for collecting and reviewing homework assignments.  
Built with **Flask**, following XP principles in a pair-programming setup.
## Demo video
![Demo](assets/demo.gif)

## 🚀 Features

### Students
- Register, log in, and upload homework files.
- Choose a teacher to send work to.
- View all submitted works, grades, and teacher feedback.

### Teachers
- View all submissions from assigned students.
- Download uploaded files.
- Assign grades and leave comments.
- See grading status (checked / pending).

---

## Tech Stack

| Component | Technology |
|------------|-------------|
| Backend | Python 3.12, Flask |
| ORM / DB | SQLAlchemy + Flask-Migrate (SQLite) |
| Frontend | HTML, Jinja2, Bootstrap 5 |
| Auth | Flask-Login, WTForms |
| CI/CD | GitHub Actions  |
| Deployment | Render / Fly.io *(planned)* |

---

## Installation

### Clone the repo
```bash
git clone https://github.com/<your-org>/SE_XP_2025.git
cd SE_XP_2025
```

### Create and activate virtual environment
```bash
python3 -m venv se_venv
source se_venv/bin/activate
pip install -r requirements.txt
```

### Run locally
```bash
python app.py
```
App will be available at: [http://127.0.0.1:5000](http://127.0.0.1:5000)

### Run test
Without coverage:
```bash
pytest -q
```
With coverage:
```bash
pytest --cov=.
```
Example run:
```
---------- coverage: platform linux, python 3.10.12-final-0 ----------
Name             Stmts   Miss Branch BrPart  Cover   Missing
------------------------------------------------------------
app.py              44      4      6      1    90%   29-30, 60-61
auth.py             37      3      8      2    89%   23, 32-33
decorators.py       14      5      4      0    50%   10-14
submissions.py      60     31      4      0    45%   20-42, 49-55, 62-73, 80-81, 88-94
------------------------------------------------------------
TOTAL              212     43     22      3    77%

2 files skipped due to complete coverage.
```

##  Testing

- `pytest` test suite  
- GitHub Actions CI  

---

##  Project Structure

```
xp/
├── app.py                 # Application entry point
├── auth.py                # Authentication routes
├── submissions.py         # File upload & review logic
├── models.py              # SQLAlchemy models
├── forms.py               # WTForms classes
├── decorators.py          # Role-based access control
├── templates/             # Jinja2 HTML templates
├── uploads/               # Uploaded homework files
├── migrations/            # Auto-generated DB migrations
└── requirements.txt
```

---

## Development Guidelines

- Follow **Extreme Programming (XP)** principles: communication, simplicity, feedback, courage.  
- Work in **pairs**, alternating *driver* / *navigator* roles.  
- Keep commits **small, clear, and frequent**.  
- Every feature → separate Pull Request with English description.  
- Maintain code style (`black`, `flake8`).

---

### Planned Feature: Cloud Storage for Homework Files

Currently, all uploaded homework files are stored locally on the server.
In future iterations, we plan to integrate **cloud storage (AWS S3, Google Cloud Storage, or Yandex Object Storage)**
to securely store uploaded files and images, improve scalability, and simplify deployment.


---

##  Contributing

1. Fork the repository  
2. Create a feature branch  
   ```bash
   git checkout -b feature/my-feature
   ```
3. Commit your changes  
   ```bash
   git commit -m "add: new feature"
   ```
4. Push and open a Pull Request  

---

## License

This project is licensed under the **MIT License** — see [LICENSE](LICENSE).

---

## Authors

Developed by  
**Anna Artamonova** & **Sergey Golovachev**  
for *Software Engineering XP 2025* coursework.

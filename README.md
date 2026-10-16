# Django Online Course Assessment & Evaluation System

A full-stack Django web application featuring an interactive online course catalog, lesson viewer, administrative backend, and an automated assessment examination engine with real-time grading, result analytics, and Bootstrap-styled interfaces.

---

## 📌 Project Overview

This project extends an e-learning platform by designing and implementing an **Assessment and Evaluation System** for online courses. Learners can enroll in courses, browse structured curriculum lessons, attempt comprehensive multiple-choice assessment exams, and receive instant score calculations with detailed question-by-question feedback. Instructors and administrators can manage courses, lessons, questions, and choices directly through the Django Admin dashboard.

---

## 🚀 Key Features

- **Course & Lesson Management:** Hierarchical course catalog with detailed syllabi, descriptions, instructors, and sequenced lesson modules.
- **Assessment Examination Engine:** Dynamically renders multiple-choice questions with customized point values per question using responsive Bootstrap collapsibles.
- **Automated Grading & Evaluation:** Real-time evaluation evaluating student submissions against correct choices, calculating percentage scores and pass/fail thresholds.
- **Interactive Results Interface:** Rich result breakdown highlighting correct choices (green badge), incorrect selections (red alert), and unselected answers.
- **Django Admin Customization:** Integrated admin dashboard with `QuestionInline` and `ChoiceInline` for streamlined course and question authoring.
- **User Authentication:** Full user registration, login, logout, and session-based enrollment management.

---

## 📊 Data Models Architecture

- **`Course`:** Represents online courses with title, description, publication date, instructors, and enrollments.
- **`Lesson`:** Sequenced curriculum modules associated with a course (`order`, `title`, `content`).
- **`Instructor` & `Learner`:** User profiles extending Django's auth model for instructors and students.
- **`Enrollment`:** Tracks user course registrations, modes (Honor/Audit/BETA), and ratings.
- **`Question`:** Assessment questions linked to courses and lessons with `question_text`, `grade` points, and `is_get_score()` evaluation logic.
- **`Choice`:** Multiple-choice options linked to questions with `choice_text` and `is_correct` boolean indicator.
- **`Submission`:** Records student exam submissions linked to enrollments and selected choices.

---

## 🛠️ Tech Stack

- **Backend:** Python 3.11, Django 5.x / 3.x
- **Database:** SQLite3 / Relational Database (ORM)
- **Frontend:** HTML5, Django Template Language (DTL), Bootstrap 4, jQuery, Popper.js
- **Testing & Tooling:** Playwright, Python unittest

---

## 📁 Repository Structure

```text
django-onlinecourse-assessment-system/
├── manage.py
├── populate_db.py
├── take_screenshots.py
├── course_details_bootstrap.html
├── 03-admin-site.png
├── 07-final.png
├── myproject/
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
├── onlinecourse/
│   ├── models.py
│   ├── admin.py
│   ├── views.py
│   ├── urls.py
│   ├── apps.py
│   ├── migrations/
│   │   └── 0001_initial.py
│   └── templates/
│       └── onlinecourse/
│           ├── course_detail_bootstrap.html
│           ├── course_details_bootstrap.html
│           ├── course_list_bootstrap.html
│           ├── exam_result_bootstrap.html
│           ├── user_login_bootstrap.html
│           └── user_registration_bootstrap.html
└── static/
    └── media/
        └── course_images/
```

---

## ⚙️ Local Setup Instructions

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/myaz3d/django-onlinecourse-assessment-system.git
   cd django-onlinecourse-assessment-system
   ```

2. **Install Dependencies:**
   ```bash
   pip install django
   ```

3. **Apply Database Migrations:**
   ```bash
   python manage.py makemigrations onlinecourse
   python manage.py migrate
   ```

4. **Populate Sample Course & Exam Data:**
   ```bash
   python populate_db.py
   ```

5. **Start Development Server:**
   ```bash
   python manage.py runserver
   ```
   Open `http://127.0.0.1:8000/` in your browser.

---

## 📝 Submission Checklist & Reference Links

- **Task 1 (models.py):** [onlinecourse/models.py](onlinecourse/models.py)
- **Task 2 (admin.py):** [onlinecourse/admin.py](onlinecourse/admin.py)
- **Task 3 (Admin Screenshot):** [03-admin-site.png](03-admin-site.png)
- **Task 4 (course_details_bootstrap.html):** [onlinecourse/templates/onlinecourse/course_details_bootstrap.html](onlinecourse/templates/onlinecourse/course_details_bootstrap.html)
- **Task 5 (views.py):** [onlinecourse/views.py](onlinecourse/views.py)
- **Task 6 (urls.py):** [onlinecourse/urls.py](onlinecourse/urls.py)
- **Task 7 (Mock Exam Result Screenshot):** [07-final.png](07-final.png)

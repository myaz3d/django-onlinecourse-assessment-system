import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings')
django.setup()

from django.contrib.auth.models import User
from onlinecourse.models import Course, Lesson, Question, Choice, Instructor, Learner, Enrollment, Submission
from datetime import date

def setup_data():
    # 1. Superuser
    if not User.objects.filter(username='admin').exists():
        admin_user = User.objects.create_superuser('admin', 'admin@example.com', 'admin12345')
        admin_user.first_name = 'Administrator'
        admin_user.save()
        print('Superuser admin created')
    else:
        admin_user = User.objects.get(username='admin')

    # 2. Student user
    if not User.objects.filter(username='student').exists():
        student_user = User.objects.create_user('student', 'student@example.com', 'password123', first_name='Mohd', last_name='Yazid')
        print('Student user created')
    else:
        student_user = User.objects.get(username='student')

    # 3. Instructor
    inst, _ = Instructor.objects.get_or_create(user=admin_user, defaults={'full_time': True, 'total_learners': 250})

    # 4. Course
    course, _ = Course.objects.get_or_create(
        name='Cloud Application Development with Django',
        defaults={
            'description': 'Master full-stack Django web development, database modeling, and exam assessment evaluation.',
            'pub_date': date.today(),
            'total_enrollment': 1
        }
    )
    course.instructors.add(inst)

    # 5. Lessons
    l1, _ = Lesson.objects.get_or_create(
        title='Introduction to Django MVT Architecture',
        course=course,
        defaults={'order': 0, 'content': 'Django follows the Model-View-Template pattern to structure dynamic, secure web applications.'}
    )
    l2, _ = Lesson.objects.get_or_create(
        title='Database Models, Migrations, and Admin',
        course=course,
        defaults={'order': 1, 'content': 'Django ORM translates Python classes into SQL tables and provides a powerful admin dashboard.'}
    )
    l3, _ = Lesson.objects.get_or_create(
        title='Views, Forms, and Assessment Features',
        course=course,
        defaults={'order': 2, 'content': 'Learn how to capture student quiz submissions, compute grades, and display detailed results.'}
    )

    # 6. Questions & Choices
    q1, _ = Question.objects.get_or_create(
        course=course,
        question_text='Which file is used to define database models in a Django application?',
        defaults={'grade': 10, 'lesson': l2}
    )
    Choice.objects.get_or_create(question=q1, choice_text='models.py', defaults={'is_correct': True})
    Choice.objects.get_or_create(question=q1, choice_text='views.py', defaults={'is_correct': False})
    Choice.objects.get_or_create(question=q1, choice_text='admin.py', defaults={'is_correct': False})
    Choice.objects.get_or_create(question=q1, choice_text='urls.py', defaults={'is_correct': False})

    q2, _ = Question.objects.get_or_create(
        course=course,
        question_text='What is the primary function of Django Admin inline classes?',
        defaults={'grade': 10, 'lesson': l2}
    )
    Choice.objects.get_or_create(question=q2, choice_text="To edit related child models directly within a parent model's change page", defaults={'is_correct': True})
    Choice.objects.get_or_create(question=q2, choice_text='To write inline CSS styles for Bootstrap templates', defaults={'is_correct': False})
    Choice.objects.get_or_create(question=q2, choice_text='To execute raw SQL queries inside Python functions', defaults={'is_correct': False})
    Choice.objects.get_or_create(question=q2, choice_text='To configure web server routing', defaults={'is_correct': False})

    q3, _ = Question.objects.get_or_create(
        course=course,
        question_text='Which HTTP request method is typically used to submit exam answers in a web form?',
        defaults={'grade': 10, 'lesson': l3}
    )
    Choice.objects.get_or_create(question=q3, choice_text='POST', defaults={'is_correct': True})
    Choice.objects.get_or_create(question=q3, choice_text='GET', defaults={'is_correct': False})
    Choice.objects.get_or_create(question=q3, choice_text='DELETE', defaults={'is_correct': False})
    Choice.objects.get_or_create(question=q3, choice_text='PUT', defaults={'is_correct': False})

    # 7. Enrollment & successful mock submission
    enrollment, _ = Enrollment.objects.get_or_create(user=student_user, course=course, defaults={'mode': 'honor'})
    correct_choices = list(Choice.objects.filter(is_correct=True))
    sub, _ = Submission.objects.get_or_create(enrollment=enrollment)
    sub.choices.set(correct_choices)
    sub.save()

    print('Database successfully populated with course, lessons, questions, choices, and mock submission!')

if __name__ == '__main__':
    setup_data()

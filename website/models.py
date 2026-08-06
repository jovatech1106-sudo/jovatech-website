from django.db import models
class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    date_sent = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name

class Student(models.Model):
    COURSE_CHOICES = [
        ("Laptop Engineering", "Laptop Engineering"),
        ("Smartphone Engineering", "Smartphone Engineering"),
        ("Python Programming", "Python Programming"),
        ("JavaScript & Web Development", "JavaScript & Web Development"),
        ("IT System Administration", "IT System Administration"),
    ]
    GENDER_CHOICES = [
        ("Male", "Male"),
        ("Female", "Female"),
    ]
    TRAINING_MODE = [
        ("Physical", "Physical"),
        ("Online", "Online"),
        ("Hybrid", "Hybrid"),
    ]
    full_name = models.CharField(max_length=150)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    date_of_birth = models.DateField()
    phone = models.CharField(max_length=20)
    whatsapp = models.CharField(max_length=20)
    email = models.EmailField()
    address = models.TextField()
    state = models.CharField(max_length=100)
    lga = models.CharField(max_length=100)
    nationality = models.CharField(max_length=100)
    qualification = models.CharField(max_length=100)
    occupation = models.CharField(max_length=100)
    course = models.CharField(max_length=100, choices=COURSE_CHOICES)
    training_mode = models.CharField(max_length=20, choices=TRAINING_MODE)
    passport = models.ImageField(upload_to="students/")
    registration_date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.full_name
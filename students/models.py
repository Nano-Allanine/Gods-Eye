from django.db import models


class Faculty(models.Model):
    class Meta:
        verbose_name = "Faculty"
        verbose_name_plural = "Faculties"

    FACULTY_CHOICES = [
        ("SCI", "Science and Technology"),
        ("BUS", "Business Studies"),
        ("HUM", "Human Science"),
        ("AGR", "Agriculture"),
    ]

    faculty_name = models.CharField(max_length=250, choices=FACULTY_CHOICES, blank=True, null=True)
    department = models.CharField(max_length=250, blank=False)
    faculty_head = models.CharField(max_length=250)

    def __str__(self):
        return f'{self.faculty_name}'


class Student(models.Model):
    COURSE_CHOICES = [
       ("BIT", "Bachelor of information Technology"), 
       ("BCS", "Bachelor of Computer Technology"),
       ("BBC", "Bachelor of Bussiness Technology")
    ]

    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    age = models.IntegerField()
    grade = models.CharField(max_length=50)
    course = models.CharField(max_length=100, choices=COURSE_CHOICES, null=True)
    faculty = models.ForeignKey(Faculty, on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return self.first_name

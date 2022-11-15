from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.base_user import BaseUserManager

class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError('Users require an email field')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        extra_fields.setdefault('username', email)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('username', email)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, password, **extra_fields)

class CustomUser(AbstractUser):
    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False, unique=True)


    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []  # removes email from REQUIRED_FIELDS

    email = models.EmailField(max_length=254, unique=True, null=True)

    objects = UserManager()

    phone_number = models.CharField(max_length=20, unique=True, null=True, blank=True)
    about = models.TextField(max_length=9000, null=True, blank=True)
    resume = models.FileField(upload_to='resumes', max_length=100, null=True, blank=True)
    education = models.CharField(max_length=255, null=True, blank=True)

    birth_date = models.DateField(auto_now=False, auto_now_add=False, null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True, auto_now=False)
    modified_at = models.DateTimeField(auto_now_add=False, auto_now=True)

    twentyTwentyone = "2020/2021"
    twentyoneTwentytwo = "2021/2022"
    twentytwoTwentythree = "2022/2023"
    twentythreeTwentyfour = "2023/2024"
    twentyfourTwentyfive = "2024/2025"
    twentyfiveTwentysix = "2025/2026"
    twentysixTwentyseven = "2026/2027"
    UNKOWN = "UNKOWN"
    NA = "NA"
    GRADUATION_YEAR_CHOICES = [
        (NA, 'Not Applicable'),
        (twentyTwentyone, '2020/2021'),
        (twentyoneTwentytwo, '2021/2022'),
        (twentytwoTwentythree, '2022/2023'),
        (twentythreeTwentyfour, "2023/2024"),
        (twentyfourTwentyfive, "2024/2025"),
        (twentyfiveTwentysix, "2025/2026"),
        (twentysixTwentyseven, "2026/2027"),
    ]
    graduation_year = models.CharField(
        max_length=10,
        choices=GRADUATION_YEAR_CHOICES,
        default=NA,
        null=True
    )

    first_year = "1st"
    second_year = "2nd"
    third_year = "3rd"
    fourth_year = "4th"

    STUDY_YEAR_CHOICES = [
        (NA, 'Not Applicable'),
        (first_year, '1st Year'),
        (second_year, "2nd Year"),
        (third_year, "3rd Year"),
        (fourth_year, "4th Year")
    ]

    study_year = models.CharField(
        max_length=10,
        choices=STUDY_YEAR_CHOICES,
        default=NA,
        null=True
    )

    admin = "ADM"
    student = "STU"
    recruiter = "REC"

    USER_TYPE_CHOICES = [
        (admin, "Admin"),
        (recruiter, "Recruiter"),
        (student, "Student")
    ]

    user_type = models.CharField(
        max_length=10,
        choices=USER_TYPE_CHOICES,
        default=student,
        null=True
    )



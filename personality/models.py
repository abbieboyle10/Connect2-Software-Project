from django.db import models

# Create your models here.
from django.conf import settings
from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.template.defaultfilters import slugify
from account.models import *


class Personality(models.Model):
    types = (
        ('entp', 'entp'),
        ('intp', 'intp'),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_letter = models.CharField(max_length=70)
    second_letter = models.CharField(max_length=70)
    third_letter = models.CharField(max_length=70)
    fourth_letter = models.CharField(max_length=70)
    type_personality = models.CharField(
        max_length=200, blank=True, choices=types)

    def __str__(self):
        return self.user


class Quiz(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=70)
    image = models.ImageField()
    slug = models.SlugField(blank=True)
    roll_out = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Question(models.Model):
    types = (
        ('extraverted', 'extraverted'),
        ('introverted', 'introverted'),
        ('intuitive', 'intuitive'),
        ('sensing', 'sensing'),
        ('thinking', 'thinking'),
        ('feeling', 'feeling'),
        ('judging', 'judging'),
        ('perceiving', 'perceiving'),



    )
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    label = models.CharField(max_length=100)
    category = models.CharField(max_length=200, blank=True, choices=types)

    def __str__(self):
        return self.label


class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    label = models.CharField(max_length=100)
    scoring = models.DecimalField(default=0, max_digits=5, decimal_places=2)

    def __str__(self):
        return self.label


class QuizTaker(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    extraverted_score = models.DecimalField(
        default=0, max_digits=5, decimal_places=2)
    introverted_score = models.DecimalField(
        default=0, max_digits=5, decimal_places=2)
    extraverted_score = models.DecimalField(
        default=0, max_digits=5, decimal_places=2)
    intuitive_score = models.DecimalField(
        default=0, max_digits=5, decimal_places=2)
    sensing_score = models.DecimalField(
        default=0, max_digits=5, decimal_places=2)
    thinking_score = models.DecimalField(
        default=0, max_digits=5, decimal_places=2)
    feeling_score = models.DecimalField(
        default=0, max_digits=5, decimal_places=2)
    judging_score = models.DecimalField(
        default=0, max_digits=5, decimal_places=2)
    perceiving_score = models.DecimalField(
        default=0, max_digits=5, decimal_places=2)

    completed = models.BooleanField(default=False)
    date_finished = models.DateTimeField(null=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.email


class UsersAnswer(models.Model):
    quiz_taker = models.ForeignKey(QuizTaker, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer = models.ForeignKey(Answer, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.question.label


@receiver(pre_save, sender=Quiz)
def slugify_name(sender, instance, *args, **kwargs):
    instance.slug = slugify(instance.name)

from django.db import models


# Create your models here.
class Question(models.Model):
    question_text = models.CharField(max_length=200, unique=True)
    pub_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.question_text

from django.contrib import admin

# Register your models here.
from polls.models import Question


class QuestionAdmin(admin.ModelAdmin):
    list_display = ['question_text', 'pub_date']


admin.site.register(Question, QuestionAdmin)

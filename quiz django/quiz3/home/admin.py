from django.contrib import admin

# Register your models here.
from .models import *


admin.site.register(Category)

class AnswerAdmin(admin.StackedInline):
    model = Answer

class QuestionsAdmin(admin.ModelAdmin):
    inlines = [AnswerAdmin]

admin.site.register(Question , QuestionsAdmin)
admin.site.register(Answer)
from django.contrib import admin
from .models import *
# Register your models here.


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']


@admin.register(Quizzes)
class QuizAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'date_created']


class OptionInlineModel(admin.TabularInline):
    model = Options
    fields = ['option', 'is_right']


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    fields = ('title', 'quiz', 'difficulty')
    list_display = ['title', 'quiz', 'difficulty', 'date_updated']
    inlines = [OptionInlineModel]


@admin.register(Options)
class OptionsAdmin(admin.ModelAdmin):
    model = Options
    list_display = ['question', 'option', 'is_right']
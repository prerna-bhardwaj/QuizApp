from os import name
from django.urls import path
from .views import *

app_name='myApp'

urlpatterns = [
    # Get list of all Quizzes
    path('', Quiz.as_view(), name='quiz'),
    # Get a random question from selected quiz
    path('random/<str:quiz_name>/', RandomQuestion.as_view(), name='question'),
    # Get a list of all questions from the selected quiz
    path('all/<str:quiz_name>/', AllQuestions.as_view(), name='all_questions'),
    # Get data of all Categories
    path('category', CategoriesData.as_view(), name='categories'),
    # Get all the data for a particular Category
    path('category/<str:category_name>/', CategoryData.as_view(), name='category'),
]

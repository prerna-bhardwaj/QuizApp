from os import name
from django.urls import path
from .views import *

app_name='myApp'

urlpatterns = [
    # Get list of all Quizzes
    path('quiz/', QuizList.as_view(), name='quiz'),

    # Get details of a particular Quiz
    path('quiz/<int:id>', QuizDetails.as_view(), name='quiz_details'),

    # Get a random question from selected quiz
    path('random/<str:quiz_name>/', RandomQuestion.as_view(), name='question'),

    # Get a list of all questions from the selected quiz
    path('all/<str:quiz_name>/', AllQuestions.as_view(), name='all_questions'),

    # Get data of all Categories
    path('category', CategoryList.as_view(), name='category'),

    # Get all the data for a particular Category
    path('category/<int:pk>/', CategoryDetails.as_view(), name='category_detail'),

    # Register a User
    path('user/', UserDetails.as_view(), name='user'),
]

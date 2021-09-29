from rest_framework import status
from rest_framework.response import Response
from rest_framework.status import HTTP_404_NOT_FOUND
from rest_framework.views import APIView
from .serializers import *
from .models import *
from rest_framework.response import Response
from rest_framework import generics, serializers
from rest_framework.views import APIView


# All quizzes
class Quiz(generics.ListAPIView):
    serializer_class = QuizSerializer
    queryset = Quizzes.objects.all()


# Create / View a Random Question
class RandomQuestion(APIView):
    def get(self, request, format=None, **kwargs):
        print(kwargs)
        question = Question.objects.filter(quiz__title=kwargs['quiz_name']).order_by('?')[:1]
        serializer = QuestionSerializer(question, many=True)
        return Response(serializer.data)


# Questions with all answers - for a specific quiz
class AllQuestions(APIView):
    def get(self,request, format=None, **kwargs):
        questions = Question.objects.filter(quiz__title=kwargs['quiz_name'])
        serializer = AllQuestionsSerializer(questions, many=True)
        return Response(serializer.data)


# Specific Category data - All quizzes
class CategoryData(APIView):
    def get(self, request, format=None, **kwargs):
        category = Category.objects.filter(name=kwargs['category_name'])
        serializer = CategorySerializer(category, many=True)
        if serializer is None:
            return Response(self.response_obj, status=status.HTTP_404_NOT_FOUND)
        return Response(serializer.data)


# All Categories
class CategoriesData(APIView):
    def get(self, request, format=None, **kwargs):
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data)


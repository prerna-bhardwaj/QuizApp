import re
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import *
from .models import *
from rest_framework.response import Response
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework import mixins
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from django.contrib.auth.models import User


class UserDetails(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get(self, request):
        return self.list(request)

    def post(self, request):
        return self.create(request)
    

# All quizzes
class QuizList(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin):
    serializer_class = QuizSerializer
    queryset = Quizzes.objects.all()
    permission_classes = [IsAuthenticated, ]
    authentication_classes = (TokenAuthentication, )


    def get(self, request):
        return self.list(request)

    def post(self, request):
        return self.create(request)


class QuizDetails(generics.GenericAPIView, mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin):
    queryset = Quizzes.objects.all()
    serializer_class = QuizSerializer

    lookup_field = 'id'

    def get(self, request, id):
        return self.retrieve(request, id=id)

    def put(self, request, id):
        return self.update(request, id=id)

    def delete(self, request, id):
        return self.destroy(request, id=id)


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
class CategoryDetails(APIView):

    def get_object(self, id):
        try:
            return Category.objects.get(pk=id) 
        except:
            return None
    
    def get(self, request, format=None, **kwargs):
        category = self.get_object(kwargs['pk'])
        # If 0 or >1 objects with given pk are found then return error.
        if category is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = CategorySerializer(category)
        return Response(serializer.data)
    

    def put(self, request, **kwargs):
        category = self.get_object(kwargs['pk'])
        serializer = CategorySerializer(category, request.data)
        # If the serializer is valid, then save it and returned updated object.
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        # Else return error message
        return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)

    
    def delete(self, request, **kwargs):
        category = self.get_object(kwargs['pk'])
        if category is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        # Delete the category if found
        category.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# All Categories
class CategoryList(APIView):
    def get(self, request, format=None, **kwargs):
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


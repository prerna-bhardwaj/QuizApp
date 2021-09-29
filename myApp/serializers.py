from rest_framework import serializers
from rest_framework.relations import StringRelatedField
from .models import *


class QuizSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quizzes
        fields = ['title', 'category']


class QuestionSerializer(serializers.ModelSerializer):
    # StringRelatedField - used to represent the option model using its __str__() method.
    options = StringRelatedField(many=True)
    class Meta:
        model = Question
        fields = ['title', 'difficulty', 'options']


class OptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Options
        fields = ['id', 'option', 'is_right']


class AllQuestionsSerializer(serializers.ModelSerializer):
    options = OptionSerializer(many=True, read_only=True)
    quiz = QuizSerializer(read_only=True)
    class Meta:
        model = Question
        fields = ['quiz', 'title', 'difficulty', 'options']


class QuizDetailsSerializer(serializers.ModelSerializer):
    questions = AllQuestionsSerializer(many=True)
    class Meta:
        model = Quizzes
        fields = ['title', 'questions']


class CategorySerializer(serializers.ModelSerializer):
    quizzes_set = QuizDetailsSerializer(many=True)

    class Meta:
        model = Category
        fields = ['name','quizzes_set']

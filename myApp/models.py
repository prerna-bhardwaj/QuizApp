from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.

class Category(models.Model):
    class Meta:
        verbose_name = _('Category')
        verbose_name_plural = _('Categories')

    name = models.CharField(max_length=255, verbose_name=_('Category Name'))
    
    def __str__(self) -> str:
        return self.name

class Quizzes(models.Model):
    class Meta:
        verbose_name = _('Quiz')
        verbose_name_plural = _('Quizzes')
        ordering = ['id']

    title = models.CharField(max_length=255, default='New Quiz', verbose_name=_('Quiz Title'))
    category = models.ForeignKey(Category, default=1, on_delete=models.DO_NOTHING)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.title

class UpdatedOn(models.Model):
    date_updated = models.DateTimeField(verbose_name=_('Last Updated'), auto_now=True)

    class Meta:
        abstract = True

class Question(UpdatedOn):
    class Meta:
        verbose_name = _('Question')
        verbose_name_plural = _('Questions')
        ordering = ['id']

    SCALE = (
        (0, _('Fundamental')),
        (1, _('Basic')),
        (2, _('Intermediate')),
        (3, _('Advanced')),
        (4, _('Expert')),
    )

    title = models.CharField(max_length=255, verbose_name=_('Question Text'))
    quiz = models.ForeignKey(Quizzes, related_name='questions', on_delete=models.DO_NOTHING)
    difficulty = models.IntegerField(choices=SCALE, verbose_name=_('Difficulty Level'))
    date_created = models.DateTimeField(auto_now_add=True, verbose_name=_('Date Created'))
    is_active = models.BooleanField(default=False, verbose_name=_('Active Status'))

    def __str__(self) -> str:
        return self.title

class Options(UpdatedOn):
    class Meta :
        verbose_name = _('Option')
        verbose_name_plural = _('Options')
        ordering = ['id']

    question = models.ForeignKey(Question, related_name='options', on_delete=models.DO_NOTHING)
    option = models.CharField(max_length=300, verbose_name=_('Option Text'))
    is_right = models.BooleanField(default=False)

    def __str__(self) -> str:
        return f'{str(self.question.id)}. {self.option} - {str(self.is_right)}'
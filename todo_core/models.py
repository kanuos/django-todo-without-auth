from django.forms import ModelForm
from django.db import models


class Note(models.Model):
    title = models.CharField(max_length=200, name='title',
                             error_messages={
                                "blank": "Title cannot be empty"
                             })
    is_complete = models.BooleanField(name='complete', default=False)
    detail = models.TextField(max_length=500, name='detail', blank=True)
    priority = models.IntegerField(default=1, choices=[
            (2, 'High Priority'),
            (1, 'Medium Priority'),
            (0, 'Low Priority'),
            ])
    date_created = models.DateTimeField(auto_now=True)


class NoteForm(ModelForm):
    class Meta:
        model = Note
        exclude = ['date_created', 'complete']


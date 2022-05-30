from django import forms


class CommentsForm(forms.Form):
    text = forms.CharField(label='Добавить комментарий', max_length=255)
    author = forms.CharField(label='Автор комментария',max_length=150)

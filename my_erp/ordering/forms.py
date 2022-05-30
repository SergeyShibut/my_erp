from django import forms


class CommentsForm(forms.Form):
    text = forms.CharField(label='Текст комментария', max_length=255, widget=forms.Textarea())
    author = forms.CharField(label='Автор комментария', max_length=150, widget=forms.TextInput())

class SendmailForm(forms.Form):
    content = forms.CharField(label='Текст сообщения', max_length=255, widget=forms.Textarea())
    subject = forms.CharField(label='Тема', max_length=150, widget=forms.TextInput())
    your_address = forms.EmailField(label='E-mail отправителя')
    address = forms.EmailField(label='E-mail получателя')
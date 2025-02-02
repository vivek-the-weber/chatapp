from django import forms

class ChatForm(forms.Form):
    all_chats = forms.CharField(max_length=500)
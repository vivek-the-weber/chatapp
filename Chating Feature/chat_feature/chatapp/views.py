from django.shortcuts import render
from django import views
from django.http import HttpResponseRedirect

from .forms import ChatForm
from .models import ChatModel
# Create your views here.

class ChatView(views.View):
    chats = ChatModel()
    def get(self,request):
        chat_form = ChatForm()
        chat_list = self.chats.all_chats.split(',')
        return render(request,"chatapp/chat.html",{
            "chat_form":chat_form,
            "all_chats" :chat_list
        })
    
    def post(self,request):
        chat_form = ChatForm(request.POST)
        chat_list = self.chats.all_chats.split(',')
        chat_list.append(chat_form.data['all_chats'])
        self.chats.all_chats = ','.join(chat_list)
        print(chat_list)
        self.chats.save()
        return HttpResponseRedirect("/")

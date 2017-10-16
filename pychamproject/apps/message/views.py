from django.shortcuts import render
import MySQLdb

from .models import  UserMessage
# Create your views here.

def getform(request):
    # all_messages = UserMessage.objects.filter(name="mayu")
    # for message in all_messages:
    #     print message.name



    if request.method == "POST":
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        address = request.POST.get('address', '')
        message = request.POST.get('message', '')
        user_message = UserMessage()
        user_message.name = name
        user_message.email = email
        user_message.address = address
        user_message.message = message
        user_message.save()



    return render(request,'message_index.html')

# def book_list(request):
#
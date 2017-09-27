from django.shortcuts import render
import MySQLdb

from .models import  UserMessage
# Create your views here.

def getform(request):
    # all_messages = UserMessage.objects.filter(name="mayu")
    # for message in all_messages:
    #     print message.name

    # user_message = UserMessage()
    # user_message.name = "atuko"
    # user_message.email = "atuko@a.com"
    # user_message.address = "akb48"
    # user_message.message = "ajiang"
    # user_message.save()



    return render(request,'message_index.html')

# def book_list(request):
#
from django.shortcuts import render
import MySQLdb

# Create your views here.

def getform(request):
    return render(request,'message_index.html')

# def book_list(request):
#
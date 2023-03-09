from django.shortcuts import render
from django.http import HttpResponse

def feedback(request):
    return render(request,'feedback.html')

def reverse(request):
    reversed_text=request.GET['usertext']
    reversed_text=reversed_text[::-1]
    return render(request,'reverse.html',{'reverse_text':reversed_text})




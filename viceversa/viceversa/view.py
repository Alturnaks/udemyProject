from django.shortcuts import render
from django.http import HttpResponse

def feedback(request):
    return render(request,'feedback.html')

def reverse(request):
    reversed_text=request.GET['usertext']
    reversed_text=reversed_text[::-1]
    len_text=len(reversed_text)
    
    data= {'reverse_text':reversed_text ,'len_text':len_text}

    return render(request, 'reverse.html', data)




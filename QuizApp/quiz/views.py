from django.shortcuts import render,redirect
from quiz.models import Quiz 
# Create your views here.
class QuizData:
    Qdata=Quiz.objects.all().values()
    

def quiz(request):
    return redirect("/quiz")

def quizHome(request):
    return render(request,"quizhome.html",{"Qdata":QuizData.Qdata})

def quizpage(request,qname,qno):
    quiz=Quiz.objects.filter(qname=qname).values()
    # print(quiz)
    no=int(qno)
    return render(request,"quizpage.html",{"quiz":quiz,"i":no})
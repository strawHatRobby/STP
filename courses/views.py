from django.shortcuts import render
from courses.models import Course,Assignment

# Create your views here.
def courses(request):
    course = Course.objects.all()
    # output = ', '.join(course)
    return render(request, 'courses.html',{'courses':course})
    
def assignments(request):
    assignment = Assignment.objects.all()
    return render(request,'assignment.html',{'assignments':assignment})
    
def assignment_details(request,pk):
    assignment = Assignment.objects.get(pk=pk)
    return render(request,'assignment_details.html',{'assignment':assignment})
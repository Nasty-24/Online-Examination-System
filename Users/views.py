from django.shortcuts import render

# Create your views here.
def Admin(request):
    return render(request, 'Admin.html')
def Contact(request):
    return render(request, 'Contact.html')
def Teacher(request):
    return render(request, 'Teacher.html')
def Student(request):
    return render(request, 'Student.html')
def Index(request):
    return render(request, 'Index.html')

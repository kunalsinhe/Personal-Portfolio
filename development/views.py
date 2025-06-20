from django.shortcuts import render

# Create your views here.
def development(request):
    return render(request, 'development/development.html')
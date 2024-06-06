from django.shortcuts import render

def all_notes(request):
    return render(request, 'all_notes.html')

# Create your views here.

from django.shortcuts import render


def dod(request):
    return render(request, 'documents/bed.html')
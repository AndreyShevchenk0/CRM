from django.shortcuts import render

def red(request):
    return render(request, 'dashboard/base.html')

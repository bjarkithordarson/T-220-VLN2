from django.shortcuts import render, redirect

def http404(request, exception=None):
    return render(request, 'errors/404.html', status=404)

def http500(request, exception=None):
    return render(request, 'errors/500.html', status=500)

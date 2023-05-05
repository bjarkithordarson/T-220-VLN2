from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect

# Create your views here.
def register(request):
    if request.user.is_authenticated:
        return redirect('profile')

    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('signin')

    print(repr(form))
    return render(request, 'register.html', {
        'form': form
    })



def profile(request):
    if not request.user.is_authenticated:
        return redirect('signin')

    return render(request, 'profile.html')

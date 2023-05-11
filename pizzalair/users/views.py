from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import UpdateUserForm, UpdateProfileForm
from django.contrib.auth.views import LoginView


# Create your views here.
def register(request):
    if request.user.is_authenticated:
        return redirect('profile')

    form = UserCreationForm()

    if request.method == 'POST':
        form = SignUpForm(data=request.POST)

        if form.is_valid():
            form.save()
            return redirect('signin')
        return redirect('signup')


    print(repr(form))
    return render(request, 'register.html', {
        'form': form
    })




def profile(request):
    return render(request, 'profile.html')



def updateUser(request):
    if request.method == 'POST':
        user_form = UpdateUserForm(request.POST, instance=request.user)
        profile_form = UpdateProfileForm(request.POST or None, request.FILES or None, instance=request.user)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Your profile is updated successfully')
            return redirect(to='profile')
    else:
        user_form = UpdateUserForm(instance=request.user)
        profile_form = UpdateProfileForm(instance=request.user)

    return render(request, 'profile.html', {'user_form': user_form, 'profile_form': profile_form})


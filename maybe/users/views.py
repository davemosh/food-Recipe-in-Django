from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .form import RegistrationForm
# Create your views here.


#here we are passing in the default django user registration form also checking if everthing enetered is valid
def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request,f'Welcome {username} your account has been created')
            return redirect('login')
    else:
        form = RegistrationForm()
    return render(request, 'users/register.html', {'form':form})


#here we are creating profile for the users which login is required
@login_required
def profilepage(request):
    return render(request, 'users/profile.html')










































































































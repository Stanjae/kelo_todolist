from email import message
from django.shortcuts import render, redirect
from myusers.forms import usersform
from django.contrib import messages


# Create your views here.
def register(request):
    form = usersform()
    if request.method == "POST":
        form = usersform(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Welcome {username}, account was sucessfully created')
            return redirect('login')
    else:
        form = usersform()
    context = {'form':form}
    return render(request, 'myusers/register.html', context)

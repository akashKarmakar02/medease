from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import SignUpForm, SignInForm


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            return redirect('/')
    else:
        form = SignUpForm()
    print(form.as_p())
    return render(request, 'auth/sign-up.html', {
        'form': form
    })


def signin(request):
    if request.method == 'POST':
        form = SignInForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            print(username)
            print(password)
            user = authenticate(request, username=username, password=password)
            print(user)
            if user is not None:
                login(request, user)
                return redirect('/')
            else:
                # Invalid login
                return render(request, 'auth/sign-in.html', {
                    'form': form,
                    'error_message': 'Invalid username or password'
                })
    else:
        form = SignInForm()
    return render(request, 'auth/sign-in.html', {'form': form})


def signout(request):
    logout(request)
    return redirect('/')

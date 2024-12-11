from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import UserLoginForm, RegistrationForm


# Create your views here.
def login_request(request):
    title = "Login"
    form = UserLoginForm(request.POST or None)
    context = {
        'form': form,
        'title': title,
    }
    if form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(request, username=username, password=password)

        login(request, user)
        return redirect('index')
    else:
        print(form.errors)
    return render(request, 'authentication/login.html', context=context)


def signup_request(request):
    title = "Create Account"
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password1")
            user = authenticate(
                request,
                username=username,
                password=password,
            )
            login(request, user)
            return redirect("index")
    else:
        form = RegistrationForm()

    context = {
        "form": form,
        "title": title,
    }
    return render(
        request,
        "authentication/signup.html",
        context=context,
    )


def logout_request(request):
    logout(request)
    # messages.info(request, "Logged out successfully!")
    return redirect('index')

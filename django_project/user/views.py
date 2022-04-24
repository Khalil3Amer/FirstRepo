from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect, render


def register(req):
    if req.method == "POST":
        form = UserCreationForm(req.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            messages.success(req, f"Account created for: {username}")
            return redirect("/")
        else:
            messages.warning(req, "invalid inputs!")
    else:
        form = UserCreationForm()
    return render(req, "user/register.html", {"form": form})

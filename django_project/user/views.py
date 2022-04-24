from django.contrib import messages
from django.shortcuts import redirect, render

from .forms import NewUserForm


def register(req):
    if req.method == "POST":
        form = NewUserForm(req.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            messages.success(req, f"Account created for: {username}")
            return redirect("/")
        else:
            messages.warning(req, "invalid inputs!")
    else:
        form = NewUserForm()
    return render(req, "user/register.html", {"form": form})

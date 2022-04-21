from django.shortcuts import render

from .models import Car


def home(req):
    return render(req, "blog/home.html", {"cars": Car.objects.all()})


def about(req):
    return render(
        req, template_name="blog/about.html", context={"title": "About Us"}
    )

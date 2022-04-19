from django.shortcuts import render

# Create your views here.
dummy_data = [
    {"first_name": "Khalil", "last_name": "Abdallah"},
    {"first_name": "Ahmad", "last_name": "Mahmoud"},
]


def home(req):
    return render(req, "blog/home.html", {"data": dummy_data})


def about(req):
    return render(req, "blog/about.html")

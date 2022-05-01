from django.shortcuts import render


def about_html(request):
    car = {
        "brand": "Ford",
        "model": "Mustang",
        "year": 1964
    }
    return render(request, 'pages/about.html', car)


def contactus_html(request):
    return render(request, 'pages/contactus.html')


def home_html(request):
    return render(request, '../templates/home.html')

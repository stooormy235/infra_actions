from django.shortcuts import render

def index(request):
    return render(request, 'index.html', context={'title': 'У меня получилось!'})

def second_page(request):
    return render(request, 'second_page.html', context={'title': 'А это вторая страница'})

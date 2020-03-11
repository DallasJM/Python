from django.shortcuts import render
from time import gmtime, strftime
from django.shortcuts import render, HttpResponse


# def index(request):
# return HttpResponse("Hey there")


def hello(request):
    return HttpResponse("hey again")


def hello_with_name(request, name):
    return HttpResponse(f"Hey there {name}")


def returnHTML(request):
    return render(request, "index.html")


def time_display(request):
    context = {
        "time": strftime("%Y-%m-%d %H:%M %p", gmtime())
    }
    return render(request, 'index.html', context)


def index(request):
    context = {
        "time": strftime("%Y-%m-%d %H:%M %p", gmtime())
    }
    return render(request, 'index.html', context)

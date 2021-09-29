from django.shortcuts import render
from django.http import HttpResponse
from .resultpy import model_load
from django.core.files.storage import FileSystemStorage


def index(request):
    return render(request, 'main/index.html')


def index(request):
    pred_y = model_load()
    return render(request, 'main/index.html', {'pred_y': pred_y})

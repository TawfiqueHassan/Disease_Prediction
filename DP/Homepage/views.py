from django.http import HttpResponse
from django.shortcuts import render
import pickle as pk

def index(request):
    with open('Model','rb') as file:
        model = pk.load(file)
    print(model.predict([[3,4,4,7,4,3,6,5,7,5,4,0,0,0,0,0,0]]))
    return render(request, "index.html")
from django.shortcuts import render
from django.http import HttpResponse


# simple api endpoint
def students(request):
    khalifas = [
        { 'id': "1", 'name': "Abu Bakar RA"},
        { 'id': "2", 'name': "Umar e Farroq RA" },
        { 'id': "3", 'name': "Osman RA" },
        { 'id': "4", 'name': "Hazrath Ali RA" },
    ]
    return HttpResponse(khalifas)
    # return HttpResponse("<center><h1>Assalamu alaikum</h1></center>")

from django.shortcuts import render
from django.http import HttpResponse
from .etl import run_etl
import os

def upload_view(request):
    if request.method == "POST":
        csv_file = request.FILES['csvfile']
        path = "temp_imdb.csv"
        
        with open(path, "wb+") as f:
            for chunk in csv_file.chunks():
                f.write(chunk)
        
        run_etl(path)
        
        return HttpResponse("ETL Complete! The messy data is now clean in your Database.")

    return render(request, "upload.html")
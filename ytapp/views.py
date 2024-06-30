# from django.shortcuts import render
from pytube import YouTube
from django.shortcuts import render,redirect, reverse
# import datetime
# from . models import 
from django.core.exceptions import ObjectDoesNotExist
# Create your views here.
def index(request):
    if request.method=="POST":
        vlink=request.POST['vlink']
        try:
            YouTube(vlink).streams.get_highest_resolution().download(output_path="your_download_path")
            msg="Downloaded Successfully"
            return render(request,"index.html",{"msg":msg})
        
        except:
            msg="Video Not Found"
            return render(request,"index.html",{"msg":msg})

    return render(request,"index.html")

# Create your views here.

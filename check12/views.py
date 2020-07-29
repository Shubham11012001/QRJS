from django.shortcuts import render
from .forms import DangerForm
from django.http import HttpResponse


# Create your views here.
def indexView(request):
    if request.method == "POST":
        data_received = request.POST['data']
        print(data_received)
        return HttpResponse(data_received)
    else:
        form = DangerForm()
        return render(request,"index.html",{'form':form})
from django.shortcuts import render
from.models import Place
from.models import Team


# Create your views here.
def travels (request):
    object=Place.objects.all()
    obj= Team.objects.all()

    return render(request,"index.html",{'result':object,'change':obj})


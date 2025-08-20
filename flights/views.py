from django.shortcuts import render

from . models import Flight

# Create your views here.
def index(request):
    return render(request, "flights/index.html", {
        "flights": Flight.objects.all()
    })

def flight(request,flight_id):
    flight = Flight.objects.get(pk=  flight_id ) #pk = primary key
    #adicionar verificação
    return render(request, "flights/flight.html",{
        "flight": flight,
        "passengers": flight.passengers.all()
        })
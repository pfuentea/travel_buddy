from django.contrib import messages
from django.shortcuts import redirect, render
import bcrypt
from .decorators import login_required
from .models import Travel, User
from datetime import date

@login_required
def index(request):
    target=User.objects.get(id=request.session['user']['id'])
    #viajes a los que voy
    travels = Travel.objects.filter(fellows=target).all()
    #viajes de los que no soy creador
    #other_travels = Travel.objects.exclude(creator=target).all()
    #viajes de los que no pertenezco
    more_travels=Travel.objects.exclude(fellows=target).all()
    context = {
        'travels': travels,
        "more_travels":more_travels
    }
    return render(request, 'index.html', context)


@login_required
def add(request):
    if request.method=='GET':
        today= date.today().strftime('%Y-%m-%d')
        context = {
            "today":today
        }
        return render(request, 'add.html', context)
    if request.method =='POST':
        errors = Travel.objects.validador_basico(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect('/add')
        else:    
            destination=request.POST['destination']
            description=request.POST['description']
            date_init=request.POST['date_init']
            date_end=request.POST['date_end']
            
            creador=User.objects.get(id=request.session['user']['id'])
            viaje=Travel.objects.create(destination=destination,plan=description,init_date=date_init,end_date=date_end,creator=creador)
            viaje.fellows.add(creador)
            return redirect('/')

#listo!
@login_required
def join(request,travel_id):
    fellow=User.objects.get(id=request.session['user']['id'])
    viaje=Travel.objects.get(id=travel_id)
    viaje.fellows.add(fellow)
    messages.success(request, "Vamos de viaje!")
    return redirect('/')

#LISTO
@login_required
def remove(request,travel_id):
    fellow=User.objects.get(id=request.session['user']['id'])
    viaje=Travel.objects.get(id=travel_id)
    viaje.fellows.remove(fellow)
    messages.warning(request, "Removido del viaje!")
    return redirect('/')

#solo falta el modal
@login_required
def delete(request,travel_id):
    viaje=Travel.objects.get(id=travel_id)
    viaje.delete()
    messages.warning(request, "Viaje eliminado!")
    return redirect('/')

@login_required
def view(request,travel_id):
    viaje=Travel.objects.get(id=travel_id)
    context = {
        "viaje":viaje
    }
    return render(request, 'view.html', context)


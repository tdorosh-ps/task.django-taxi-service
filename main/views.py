from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout

from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin

from django.contrib.auth.decorators import login_required

from main.models import Order, Car
from main.forms import OrderForm

# Create your views here.

class OrderCreateView(CreateView):
    model = Order
    form_class = OrderForm

    def form_valid(self, form):
        available_cars = Car.objects.filter(is_available=True)
        if available_cars:
            order = form.save(commit=False)
            car = available_cars[0]
            car.set_unavailable()
            car.save()
            order.car = car
            order.save()
            return render(self.request, 'main/success_order.html', {'order': order})
        else:
            form = OrderForm(self.request.POST)
            return render(self.request, 'main/order_form.html', {'form': form, 'message': True})


class OrderListView(LoginRequiredMixin, ListView):
    queryset = Order.objects.order_by('-create_datetime')
    context_object_name = 'order_list'
    paginate_by = 2

class OrderDetailView(LoginRequiredMixin, DetailView):
    model = Order
    context_object_name = 'order'

class CarListView(LoginRequiredMixin, ListView):
    queryset = Car.objects.order_by('-is_available')
    context_object_name = 'car_list'
    paginate_by = 2

class CarDetailView(LoginRequiredMixin, DetailView):
    model = Car
    context_object_name = 'car'

@login_required
def car_set_available_view(request, pk):
    car = Car.objects.get(pk=pk)
    car.set_available()
    car.save()
    return redirect('{}?status_message=Car was set available successfully'.format(reverse('car-list')))

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username', '').strip()
        password = request.POST.get('password', '').strip()
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect(reverse('order-list'))
        else:
            return render(request, 'main/login.html', {'error': 'Authentication error'})
    return render(request, 'main/login.html')

def logout_view(request):
    logout(request)
    return redirect(reverse('create-order'))
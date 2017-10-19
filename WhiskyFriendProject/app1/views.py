from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.template.response import TemplateResponse
from django.urls import reverse_lazy, reverse
from django.views import View
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView
from .models import Slainteet, Spirit, Order
from .forms import SignUpForm, CreateSlainteetForm, OrderForm


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})


class StartView(View):
    def get(self, request):
        return render(request, "index.html")


class AllSpiritsView(View):
    def get(self, request):
        return TemplateResponse(request, 'all_spirits.html')


class SpiritDetailsView(View):
    def get(self, request, spirit_id):
        spirit = Spirit.objects.get(id=spirit_id)
        orders = Order.objects.filter(spirit_id=spirit_id)
        return render(request, "spirit_details.html", {"spirit": spirit, "orders": orders})


class NewOrderView(LoginRequiredMixin, View):
    def get(self, request, spirit_id):
        form = OrderForm()
        spirit = Spirit.objects.get(id=spirit_id)
        return render(request, "new_order.html", {"form": form, "spirit": spirit})

    def post(self, request, spirit_id):
        form = OrderForm(request.POST)
        if form.is_valid():
            spirit = spirit_id
            quantity = form.cleaned_data['quantity']
            user = request.user

            Order.objects.create(
                spirit_id=spirit,
                quantity=quantity,
                user=user

            )
            url = reverse("spirit_details", kwargs={"spirit_id": spirit_id})
            return HttpResponseRedirect(url)
        else:
            return render(request, "all_spirits.html", {'form': form})


class AllOrdersView(View):
    def get(self, request):
        return TemplateResponse(request, 'all_orders.html')


class SlainteetList(LoginRequiredMixin, ListView):
    template_name = 'slainteet_wall.html'

    def get_queryset(self):
        return Slainteet.objects.all().order_by("-creation_date")


class NewSlainteet(LoginRequiredMixin, CreateView):
    form_class = CreateSlainteetForm
    template_name = 'form.html'
    success_url = reverse_lazy('wall')

    def get_initial(self):
        initials = super(NewSlainteet, self).get_initial()
        initials['user'] = self.request.user
        return initials

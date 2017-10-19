import datetime
from .models import Spirit, Order


def my_cp(request):
    ctx = {
        "date": datetime.date.today(),
        'version' : "v. 1.0"
    }
    return ctx


def spirits(request):
    ctx = {
        "spirits" : Spirit.objects.all()
    }
    return ctx

def orders(request):
    ctx = {
        "orders" : Order.objects.all()
    }
    return ctx
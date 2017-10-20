"""WhiskyFriendProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""

from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static
from app1 import views as core_views

from app1.views import (StartView, AllSpiritsView, SpiritDetailsView, NewOrderView, AllOrdersView, SlainteetListView,
                        NewSlainteetView, SlainteetDetailView, CreateCommentView)

urlpatterns = [
                  # Linki do Logowania
                  url(r'^admin/', admin.site.urls),

                  url(r'^login/$', auth_views.login, {'template_name': 'login.html'}, name='login'),
                  url(r'^logout/$', auth_views.logout, {"next_page": "home"}, name='logout'),
                  url(r'^signup/$', core_views.signup, name='signup'),
                  # Linki do akcji
                  url(r'^index', StartView.as_view(), name="home"),
                  url(r'^all_spirits/', AllSpiritsView.as_view(), name="all_spirits"),
                  url(r'spirit_details/(?P<spirit_id>(\d)+)', SpiritDetailsView.as_view(), name="spirit_details"),
                  url(r'^new_order/(?P<spirit_id>(\d)+)', NewOrderView.as_view(), name="new_order"),
                  url(r'^all_orders', AllOrdersView.as_view(), name="all_orders"),
                  # Linki do community
                  url(r'^slainteet/', SlainteetListView.as_view(), name="wall"),
                  url(r'^say_slainte/', NewSlainteetView.as_view(), name="say_slainte"),
                  url(r'^add_comment/(?P<slainteet_id>(\d)+)', CreateCommentView.as_view(), name='comment'),
                  url(r'^slainteet_detail/(?P<pk>(\d)+)', SlainteetDetailView.as_view(), name='slainteet')

              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

from django.urls import path

from catalog.views import exp_view

app_name = 'catalog'

urlpatterns = [
    path('', exp_view, name='exp_view'),
]

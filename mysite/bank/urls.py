from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    #path('überweisung', views.make_transaction, name='Überweisung'),
    path('123',views.testview, name='test')
]
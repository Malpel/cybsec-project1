from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('accounts/', views.accounts, name='accounts'),
    path('account/', views.account, name='account'),
    path('signup/', views.sign_up, name='signup'),
    path('login/', views.login, name='login')
]
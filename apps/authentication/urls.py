from django.urls import path
from apps.authentication import views
from django.contrib.auth.views import LoginView



urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('signup/', views.signup, name='signup')

]
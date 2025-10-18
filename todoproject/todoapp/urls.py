from django.urls import path
from todoapp import views
from django.contrib.auth.views import LoginView

urlpatterns=[
    path("",views.home),
    path("SignUp",views.SignUp,name='signup'), #creating a path from home page to signup page
    path("Login",LoginView.as_view(template_name='login.html'),name='login'),
    path("accounts/profile/",views.Dashboard,name='dashboard'),
    path('addTask',views.AddTask,name='Add_Task'),
    path('edit/<int:pk>',views.Edit,name='edit'),
    path('delete/<int:pk>',views.Delete,name='delete'),
    path('forgetpassword',views.Forgpass,name='forgpass'),
    path('today/', views.today_view, name='today'),       # Connects {% url 'today' %}
    path('upcoming/', views.upcoming_view, name='upcoming'), # Connects {% url 'upcoming' %}
    path('completed/', views.completed_view, name='completed'), # Connects {% url 'completed' %}
    path('settings/', views.settings_view, name='settings'), # Connects {% url 'settings' %}
]

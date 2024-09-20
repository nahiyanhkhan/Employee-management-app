from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("add/", views.add_emp, name="add_emp"),
    path("action/", views.action, name="action"),
    path("update/<int:pk>/", views.update_emp, name="update_emp"),
    path("delete/<int:pk>/", views.delete_emp, name="delete_emp"),
    path("employee/<int:pk>/", views.emp_details, name="emp_details"),
    path("login/", views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout"),
]

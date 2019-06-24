from django.urls import path
from skillset import views

# Template urls
app_name = 'skillset'

urlpatterns=[
    path('employee/sign_up/', views.employee_sign_up, name='emp_signup'),
    path('enterprise/sign_up/', views.comp_sign_up, name='comp_signup'),
    path('login/', views.user_login, name='user_login'),
    path('search/', views.search, name='search'),
]

from django.urls  import path
from . import views

urlpatterns = [
    path('logout/',views.log_out, name="logout"),
    path('register/',views.register_user, name="register"),
    path("",views.home,name="home")
]

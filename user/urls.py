from django.urls import path
from . import views
urlpatterns = [
    path('login/',views.user_login,name='user_login'),
    path('signup/',views.user_signup,name='user_signup'),
    path('logout/',views.user_logout,name='user_logout'),
    path('profile/',views.user_profile,name='user_profile'),
    path('profile/change_password',views.pass_change,name='pass_change'),
    path('profile/change_password2',views.pass_change2,name='pass_change2'),
]

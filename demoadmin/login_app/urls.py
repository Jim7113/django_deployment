from django.conf.urls import url
from django.urls import path
from login_app import views
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns,static

app_name = 'login_app'

urlpatterns = [
    path('', views.index , name='index'),
    path('reg/', views.register, name='reg'),
    path('login/', views.login_page, name='login'),
    path('user_login/', views.login_user, name='user_login'),
    path('logout/', views.user_logout, name='logout'),
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


from django.contrib import admin
from django.urls import path
from plantas import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('plantas/', views.listar_plantas, name='listar_plantas'),
    path('plantas/create/', views.create_planta, name='create_planta'),
    path('plantas/edit/<int:id>/', views.edit_planta, name='edit_planta'),
    path('plantas/delete/<int:id>/', views.delete_planta, name='delete_planta'),
]

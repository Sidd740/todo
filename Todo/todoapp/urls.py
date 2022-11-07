from django.urls import path
from todoapp import views


urlpatterns = [
    path('update/<int:tid>',views.update),
    path('show/', views.show),
    path('delete/<int:tid>',views.delete)
]

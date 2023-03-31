from django.urls import path
from . import views

urlpatterns = [
    path('update/<int:id>/', views.UserUpdateView.as_view(), name='update'),
    # path('<int:id>/', views.UserUpdateView.as_view(), name='update'),
    path('delete/<int:id>/', views.UserDeleteView.as_view(), name='delete'),
    # path('<int:id>/', views.UserDeleteView.as_view(), name='delete')
    
]

from django.urls import path
from .views import (PasswordListView, 
                    PasswordDetailView, 
                    PasswordCreateView,
                    PasswordUpdateView,
                    PasswordDeleteView,
                    UserPasswordListView
)
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    # path('index', PasswordListView.as_view(), name='index'),
    path('user/<str:username>', UserPasswordListView.as_view(), name='user-sitepassword'),
    path('sitepassword/<int:pk>/', PasswordDetailView.as_view(), name='sitepassword-detail'),
    path('sitepassword/new/', PasswordCreateView.as_view(), name='sitepassword-create'),
    path('sitepassword/<int:pk>/update/', PasswordUpdateView.as_view(), name='sitepassword-update'),
    path('sitepassword/<int:pk>/delete/', PasswordDeleteView.as_view(), name='sitepassword-delete'),
    path('login/', views.login, name='login'),
]

# <app>/<model>_<viewtype>.html
# core/sitepassword_list.html OR # citadel/sitepassword_list.html
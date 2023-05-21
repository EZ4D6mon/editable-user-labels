from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.registerPage, name="register"),
    path('login/', views.loginPage, name="login"),
    path('logout/', views.logoutUser, name="logout"),

    path('', views.home, name="home"),
    path('about/', views.about, name = 'about'),
    path('user/<str:pk_test>/', views.userPage, name = "user"),
    path('account/', views.accountSettings, name="account_settings"),

    path('create_tag/', views.createTag, name="create_tag"),
    path('rename_tag/<str:pk>/', views.renameTag, name="rename_tag"),
    path('delete_tag/<str:pk>/', views.deleteTag, name="delete_tag"),
]
from django.urls import  path

from . import views

urlpatterns = [
	#Leave as empty string for base url
	path('', views.home, name="home"),
	path('register/', views.register, name="register"),
	path('login/', views.login, name="login"),
	path('demo/', views.demo, name="demo"),
	# path('upload/', views.upload, name="upload"),
	# path('cart/', views.cart, name="cart"),
	# path('checkout/', views.checkout, name="checkout"),

]
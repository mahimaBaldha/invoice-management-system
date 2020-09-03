from django.urls import  path

from . import views

urlpatterns = [
	#Leave as empty string for base url
	path('', views.home, name="home"),
	path('register/', views.register, name="register"),
	path('login/', views.login, name="login"),
	path('logout/', views.logout, name="logout"),
	path('fileupload/', views.uploadFile, name="uploadFile"),
	path('create_invoice/<int:id>/<str:pdf_name>', views.createInvoice, name="upload"),
	# path('addItem/', views.addItems, name="addItems"),
]
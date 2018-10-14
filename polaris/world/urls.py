from django.urls import path

from . import views

app_name = 'world'

urlpatterns = [
	path('',views.index,name='index'),
	path('world_view/',views.world_view,name='world_view')
]

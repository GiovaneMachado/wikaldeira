from django.urls import path
from . import views
from django.conf.urls.static import static
from wikaldeiraproject import settings

urlpatterns = [
	path('', views.lore_list, name='lore_list'),
	path('results/', views.lore_search, name='lore_search'),
	path('lore/<int:pk>/', views.lore_detail, name='lore_detail'),
	path('lore/new/', views.lore_new, name='lore_new'),
	path('lore/<int:pk>/edit/', views.lore_edit, name='lore_edit'),
	path('lore/<int:pk>/delete/', views.lore_delete, name='lore_delete'),
]

urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
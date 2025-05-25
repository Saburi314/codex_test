from django.urls import path

from . import views

urlpatterns = [
    path('', views.PreparedItemListView.as_view(), name='prepareditem_list'),
    path('add/', views.PreparedItemCreateView.as_view(), name='prepareditem_add'),
    path('<int:pk>/', views.PreparedItemDetailView.as_view(), name='prepareditem_detail'),
    path('<int:pk>/edit/', views.PreparedItemUpdateView.as_view(), name='prepareditem_edit'),
    path('<int:pk>/delete/', views.PreparedItemDeleteView.as_view(), name='prepareditem_delete'),
]

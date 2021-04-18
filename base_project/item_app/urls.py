from item_app import views
from django.urls import path
app_name='item_app'
urlpatterns=[
    #url('',views.index,name='index'),
    path('', views.ItemListView.as_view(),name='list'),
    path('<int:pk>/', views.ItemDetailView.as_view(), name='detail'),
    path('create/',views.ItemCreateView.as_view(), name='create'),
    path('update/<int:pk>/', views.ItemUpdateView.as_view(), name='update'),
    path('delete/<int:pk>/', views.ItemDeleteView.as_view(), name='delete'),
    ]
# appname/urls.py
from django.urls import path
from .views import ListHubPropertyListView, AddListHubPropertyView

urlpatterns = [
    path('listhub-properties/', ListHubPropertyListView.as_view(), name='listhub-properties-list'),
    path('listhub-properties/add/', AddListHubPropertyView.as_view(), name='listhub-properties-add'),

]

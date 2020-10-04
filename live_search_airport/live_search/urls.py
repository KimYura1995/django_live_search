from django.urls import path

from live_search.views import AirportListView, AirportLiveSearchView

urlpatterns = [
    path('', AirportListView.as_view(), name='airport_list'),
    path('filter_city/', AirportLiveSearchView.as_view(), name='airport_filter'),
]

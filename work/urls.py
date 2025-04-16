from django.urls import path
from .views import (
    WorkCreateView,
    WorkListView,
    WorkDetailView,
    WorkUpdateView,
    WorkDeleteView,
)

urlpatterns = [
    path('works_list/', WorkListView.as_view(), name='work-list'),
    path('work_create/', WorkCreateView.as_view(), name='work-create'),
    path('work_detail/<uuid:uid>/', WorkDetailView.as_view(), name='work-detail'),
    path('work/<uuid:uid>/update/', WorkUpdateView.as_view(), name='work-update'),
    path('work/<uuid:uid>/delete/', WorkDeleteView.as_view(), name='work-delete'),
]

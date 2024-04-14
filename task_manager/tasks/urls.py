from django.urls import path

from task_manager.tasks.views import (
    IndexView,
    TaskView,
    TaskFormCreateView,
    TaskFormUpdateView,
    TaskFormDeleteView,
)

urlpatterns = [
    path('', IndexView.as_view(), name='tasks_index'),
    path('create/', TaskFormCreateView.as_view(), name='task_create'),
    path('<int:pk>/', TaskView.as_view(), name='task_read'),
    path('<int:pk>/update/', TaskFormUpdateView.as_view(), name='task_update'),
    path('<int:pk>/delete/', TaskFormDeleteView.as_view(), name='task_delete'),
]

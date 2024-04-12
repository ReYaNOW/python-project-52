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
    path('<int:id>/', TaskView.as_view(), name='task_read'),
    path('<int:id>/update/', TaskFormUpdateView.as_view(), name='task_update'),
    path('<int:id>/delete/', TaskFormDeleteView.as_view(), name='task_delete'),
]
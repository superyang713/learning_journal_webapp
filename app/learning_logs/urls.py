from django.urls import path

from learning_logs import views

app_name = 'learning_logs'

urlpatterns = [
    path(r'', views.index, name='index'),
    path('topics', views.topics, name='topics'),
    path('topics/<int:topic_id>', views.topic, name='topic'),
    path('topics/new_topic/', views.new_topic, name='new_topic'),
    path('topics/new_entry/<int:topic_id>', views.new_entry, name='new_entry'),
    path('topics/edit_entry/<int:entry_id>', views.edit_entry, name='edit_entry'),
]

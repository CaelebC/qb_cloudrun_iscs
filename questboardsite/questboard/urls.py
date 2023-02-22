from django.urls import path

from .views import (
    HomeView, QuestboardDetailView,
    edit_questboard, add_quest, edit_quest
)


urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path(
        'questboard/<int:pk>', QuestboardDetailView.as_view(),
        name='questboard_detail'
    ),
    path('edit_questboard/<int:pk>', edit_questboard, name='edit_questboard'),
    path(
        'add_questboard/<int:pk>', add_quest,
        name='add_quest'
    ),
    path('edit_quest/<int:pk>', edit_quest, name='edit_quest')
]

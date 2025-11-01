from django.urls import path
from .views import GamesView, GameView, GameMoveView, GameMovesView

urlpatterns = [
    path('games/', GamesView.as_view(), name='games'),
    path('game/<int:game_id>/', GameView.as_view(), name='game'),
    path('gamemoves/', GameMovesView.as_view(), name='gamemoves'),
    path('gamemove/', GameMoveView.as_view(), name='gamemove'),
]
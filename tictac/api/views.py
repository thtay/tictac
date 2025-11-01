from rest_framework import status
import numpy as np
import random

from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Game, GameMove
from .serializers import GameSerializer, GameMoveSerializer
from django.core import serializers



class GamesView(APIView):
    def get(self, request):
        games = Game.objects.order_by("created")

        player_id = request.GET.get('player_id', None)
        if player_id is not None:
            games = games.filter(player_id__icontains=player_id)

        serializer = GameSerializer(games, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = GameSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
    
class GameView(APIView):
    def get(self, request , game_id):
        games = Game.objects.filter(id=game_id)
        serializer = GameSerializer(games, many=True)
        return Response(serializer.data)
    
    def put(self, request , game_id):
        game = Game.objects.filter(id=game_id)
        if game is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = GameSerializer(game)
        return Response(serializer.data)
    
    def delete(self, request, game_id):
        games = Game.objects.filter(id=game_id)
        games.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
class GameMovesView(APIView):
    def get(self, request):
        game_moves = GameMove.objects.all()
        serializer = GameMoveSerializer(game_moves, many=True)
        return Response(serializer.data)
    
    
class GameMoveView(APIView):
    
    # Game logic for tic tac. We should probably move this to another class.
    def create_empty_board(self,):
        return np.zeros((3, 3), dtype=int)

    def build_board_place(self, board, gameHisotry):
        loc = (gameHisotry.x, gameHisotry.y)
        board[loc] = gameHisotry.player_id
        return board

    def row_win(self, board, player):
        return any(all(cell == player for cell in row) for row in board)
    
    def col_win(self, board, player):
        return any(all(row[i] == player for row in board) for i in range(3))
    
    def diag_win(self,board, player):
        return all(board[i][i] == player for i in range(3)) or \
            all(board[i][2 - i] == player for i in range(3))
    
    def evaluate(self, board):
        for player in [1, 2]:
            if self.row_win(board, player) or self.col_win(board, player) or self.diag_win(board, player):
                return player
        return -1 if np.all(board != 0) else 0

        
    def get(self, request):
        game_id = request.GET.get('game_id', None)
        game_moves = GameMove.objects.filter(game_id=game_id)
        serializer = GameMoveSerializer(game_moves, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        game_id = request.GET.get('game_id', None)
        game = Game.objects.filter(id=game_id)
        
        if game is None:
            return Response(status=status.HTTP_404_NOT_FOUND)

        # Need to check that move is valid
                
        # Make the move
        serializer = GameMoveSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        
        # The AI also need to make a move
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
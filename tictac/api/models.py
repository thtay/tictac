from django.db import models


class Game(models.Model):
    player_id = models.IntegerField(max_length=70, blank=False)
    status = models.CharField(max_length=70, blank=False, default='incomplete')
    board = models.JSONField()
    created = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["created"]


class GameMove(models.Model):
    player_id = models.IntegerField(max_length=70, blank=False)
    x = models.IntegerField(max_length=70, blank=False, default=0)
    y = models.IntegerField(max_length=70, blank=False, default=0)
    game_id = models.IntegerField(max_length=70, blank=False, default='')
    created = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["created"]

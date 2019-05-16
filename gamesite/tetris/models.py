from django.db import models


class Stats(models.Model):
    score = models.IntegerField

    def get_score(self):
        return self.score


class WebGame(models.Model):
    difficulty = models.IntegerField(default=0)

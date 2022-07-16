from operator import index
from uuid import uuid4

from django.db import models


class Draw(models.Model):
    draw_id = models.UUIDField(default=uuid4, primary_key=True)
    draw_name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f"draw_id: {self.draw_id}, draw_name: {self.draw_name}, created_at: {self.created_at}"

    def __repr__(self) -> str:
        return f"Draw(draw_id={self.draw_id}, draw_name={self.draw_name}, created_at={self.created_at})"
    

    class Meta:
        ordering = ['created_at']

class Winner(models.Model):
    winner_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    fk_draw = models.ForeignKey("Draw", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"winner_id: {self.winner_id} - fk_draw: {self.fk_draw} - name: {self.name}"

    def __repr__(self):
        return f"Winner(winner_id={self.winner_id}, name={self.name})"

    class Meta:
        ordering = ['name']
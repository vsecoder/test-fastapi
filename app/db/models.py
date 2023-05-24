from tortoise import fields
from tortoise.models import Model


class Messages(Model):
    id = fields.BigIntField(pk=True, unique=True)
    text = fields.TextField()
    toxic = fields.FloatField(default=0.0)
    neutral = fields.FloatField(default=0.0)

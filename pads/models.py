from django.contrib.auth.models import User
from django.db import models


class Pad(models.Model):
    name = models.CharField(max_length=100)
    user = models.ForeignKey(
        User,     
        on_delete = models.CASCADE,
        limit_choices_to={'is_user': True},
    )

    def __unicode__(self):
        return self.name

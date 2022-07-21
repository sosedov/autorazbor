from datetime import datetime
from enum import auto
from time import timezone
import uuid

from django.db import models


class AbstractModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created = models.DateTimeField(auto_now=True, null=True)
    changed = models.DateTimeField(null=True)

    class Meta:
        abstract = True

    def __str__(self):
        return str(self.pk)

    def save(self, *args, **kwargs):
        self.changed = datetime.now()
        super(AbstractModel, self).save(*args, **kwargs)
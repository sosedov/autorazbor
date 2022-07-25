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

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        self.changed = datetime.now()
        super().save(force_insert, force_update, using, update_fields)
import uuid

from django.db import models


class AbstractModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created = models.DateTimeField(auto_now=True)
    changed = models.DateTimeField(null=True)

    class Meta:
        abstract = True

    def __str__(self):
        return str(self.pk)

from django.db import models
import uuid

class basemodel(models.Model):
    uid=models.UUIDField(primary_key=True,editable=False,default=uuid.uuid4)
    create_at=models.DateField(auto_now=True)
    updated_at=models.DateField(auto_now_add=True)
    
    class Meta:
        abstract=True
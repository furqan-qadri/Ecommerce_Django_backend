from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey

# Create your models here.
#implementing tag and tags here

class Tag(models.Model):
    label=models.CharField(max_length=255)
    
class TaggedItem(models.Model):
    tag=models.ForeignKey(Tag, on_delete=models.CASCADE)
    #generic content type. #these three are needed.
    content_type=models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id=models.PositiveIntegerField()
    content_object=GenericForeignKey()
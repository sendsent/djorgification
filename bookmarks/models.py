from uuid import uuid4
from django.db import models

# Create your models here.
# Take a look at models.Model and Model class from django
class Bookmark (models.Model): 
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    url = models.URLField('URL', unique=True) # unique=true can be translated to a constraint in the SQL that will actually restrict URLs to be unique in the DB
    name = models.CharField(max_length=300)
    notes = models.TextField(blank=True)


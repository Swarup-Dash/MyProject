from django.db import models
from django.utils import timezone

# Create your models here.

class NotesVariety(models.Model):
  CHAI_TYPE_CHOICES = [
    ('PY', 'PYTHON'),
    ('DJ', 'DJANGO'),
    ('MS', 'MySql'),
    ('HM', 'HTML'),
    ('JV', 'JAVA'),
  ]

  name = models.CharField(max_length=100)
  image = models.ImageField(upload_to='myprofile/')
  date_added = models.DateTimeField(default=timezone.now)
  type = models.CharField(max_length=2, choices=CHAI_TYPE_CHOICES, default='PY')

  def __str__(self): 
    return self.name
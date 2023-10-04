from django.db import models

# Create your models here.
class rfidno_esp32no(models.Model):
    rfidno = models.IntegerField()
    esp32no = models.IntegerField()
    
    def __str__(self):
        return self.esp32no
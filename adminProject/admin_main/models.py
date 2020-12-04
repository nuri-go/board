from django.db import models
from django.db.models import Model 


# Create your models here.
class Client_list(models.Model):
    NO = models.AutoField(primary_key=True)
    voc_date = models.TextField()
    voc_method = models.CharField(max_length=50)
    client_number = models.TextField()
    client_name = models.TextField()
    voc_number =  models.TextField()
    voc_title = models.TextField()
    voc_content = models.TextField()
    voc_comment = models.TextField()
    voc_manger = models.CharField(max_length=50)
    report = models.CharField(max_length=50)
    partner = models.CharField(max_length=50)

    def client_save(self):
        self.save()

    class Meta:
        managed = False
        db_table = 'client_list'

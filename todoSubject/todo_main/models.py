from django.db import models

# Create your models here.

class Todo_list(models.Model):
    no = models.AutoField(primary_key=True)
    pcode = models.CharField(max_length=4)
    user_id = models.CharField(max_length=50)
    title = models.CharField(max_length=200)
    content = models.TextField(max_length=1000)
    is_complete = models.BooleanField()
    date= models.DateField()

    class Meta:
        managed = False
        db_table = 'todo_list'

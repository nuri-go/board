from django.db import models

# Create your models here.
class ProjectCode(models.Model):
    pcode = models.CharField(primary_key=True, max_length=4)
    pname = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'project_code'


class TodoList(models.Model):
    no = models.AutoField(db_column='NO', primary_key=True)  # Field name made l                                                                                                                                                             owercase.
    pcode = models.CharField(max_length=4)
    user_id = models.CharField(max_length=50, blank=True, null=True)
    title = models.CharField(max_length=200, blank=True, null=True)
    content = models.CharField(max_length=1000, blank=True, null=True)
    is_complete = models.IntegerField(blank=True, null=True)
    priority = models.IntegerField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)

    def todo_save(self):
        self.save()

    class Meta:
        managed = False
        db_table = 'todo_list'

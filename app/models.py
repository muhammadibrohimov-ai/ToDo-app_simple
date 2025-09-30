from django.db import models

# Create your models here.

class ToDo(models.Model):
    STATUS_CHOICES = [
        ['new', 'NEW'],
        ['in_proccess', 'IN PROCCESS'],
        ['finished', 'FINISHED'],
    ]
    
    title = models.CharField(max_length=150)
    desc = models.TextField(null=True, blank=True)
    time= models.DateTimeField()
    status = models.CharField(max_length=50, choices=STATUS_CHOICES)
    
    class Meta:
        verbose_name = "ToDo"
        verbose_name_plural = "ToDo"
    
    def __str__(self):
        return self.title
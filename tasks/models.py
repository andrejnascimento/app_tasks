from django.db import models

# Create your models here.
class Tasks(models.Model):
    STATUS_CHOICES = [
        ('P', 'Pendente'),
        ('A', 'Em andamento'),
        ('C', 'Concluido'),
    
    ]
    title = models.CharField(max_length=255)
    description = models.TextField()
    status = models.CharField(max_length=1, choices= STATUS_CHOICES, default= 'P')
    created_at = models.DateTimeField(auto_now_add= True)
    due_date = models.DateField()
    
    def __str__(self) -> str:
        return self.title
    
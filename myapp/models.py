from django.db import models

# Create your models here. 
class Projects(models.Model):
    name = models.CharField(max_length=200)

    # Extend this class to django admin.
    def __str__(self) -> str:
        return self.name

class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    project = models.ForeignKey(Projects, on_delete=models.CASCADE)
    done = models.BooleanField(default=False)

    # Extend this class to django admin.
    def __str__(self) -> str:
        return self.title + '-' + self.project.name
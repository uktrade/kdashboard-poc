from django.db import models
from user.models import User
# Create your models here.

class Dashboards(models.Model):
    dashboard_name = models.CharField(max_length=100)
    user = models.ManyToManyField(User)

    def __str__(self):
        return self.dashboard_name


# class AccessToDashboard(models.Model):
#     dashboard_user = models.ForeignKey(User, on_delete=models.CASCADE)
#     dashboard_item = models.ForeignKey(Dashboards, on_delete=models.CASCADE)

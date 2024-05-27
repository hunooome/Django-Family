from django.db import models
from django.core.files.storage import FileSystemStorage





class contact(models.Model):
    id = models.AutoField(primary_key=True)
    logo = models.FileField(upload_to='uploads/%Y/%m/%d/',default="",blank=True,null=True)
    title = models.CharField(max_length=70, blank=False)
    city = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=20)

    Type = "pls choice the type"
    Individual = "Individual"
    Company = "Company"
    
    type_choice = {
        Type: "pls choice the type",
        Individual: "Individual",
        Company: "Company",
    }
    type = models.CharField(max_length=20, choices=type_choice, default=Type,)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

   

    def __str__(self):
        return self.title
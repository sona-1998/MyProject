from django.db import models

# Create your models here.
class User(models.Model):
    first_name =models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    user_name = models.CharField(max_length=100)
    phone_no = models.IntegerField()
    email= models.EmailField()
    password = models.CharField(max_length=50)
    conform_password = models.CharField(max_length=50)


    def __str__(self):
        return self.user_name
    #login
'''class LoginUser(models.Model):
    email = models.EmailField()
    password = models.CharField(max_length=50)

    def __str__(self):
        return self.email'''


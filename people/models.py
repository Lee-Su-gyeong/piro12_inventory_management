from django.db import models

class People(models.Model):
    name=models.CharField(max_length=100,verbose_name='이름')
    phone=models.CharField(max_length=200,verbose_name='전화번호')
    address=models.CharField(max_length=200,verbose_name='주소')

    def __str__(self):
        return self.name

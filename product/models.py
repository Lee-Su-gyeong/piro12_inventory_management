from django.db import models





class Post(models.Model):

    title = models.CharField(max_length=200,verbose_name='제품명')
    content = models.TextField(verbose_name='제품설명')
    image = models.FileField(upload_to="image",verbose_name='제품 사진')
    price = models.IntegerField(verbose_name='제품 가격')
    amount = models.IntegerField(default=0,verbose_name='남은 수량')

    # nationality = models.ForeignKey(People,on_delete=models.CASCADE,verbose_name='거래처',related_name='item')

    def __str__(self):
        return self.title




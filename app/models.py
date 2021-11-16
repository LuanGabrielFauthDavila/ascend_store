from django.db import models

class produto_model(models.Model):
    file = models.FileField(upload_to='app/static/public/product_images/')
    title = models.CharField(max_length=30)
    desc = models.CharField(max_length=55)
    price = models.FloatField()

    def __str__(self):
        return self.title

class pedido_model(models.Model):
    numero = models.IntegerField()
    usuario = models.CharField(max_length=55)

    def __str__(self):
        return self.numero

class shop_car_model(models.Model):
    id_user = models.IntegerField()
    id_produto = models.IntegerField()

    def __str__(self):
        return str(self.id_user)
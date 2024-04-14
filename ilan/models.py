from django.db import models
import os

# Create your models here.

class Ilan(models.Model):
    il_choices = (('Tekirdağ', 'Tekirdağ'),('Bursa', 'Bursa'),('Kocaeli', 'Kocaeli'))
    gender_choices = (('Erkek', 'Erkek'),('Dişi', 'Dişi'))
    age_choices = (('0-3 Aylık', '0-3 Aylık'),('3-6 Aylık', '3-6 Aylık'),('6-12 Aylık', '6-12 Aylık'),('1', '1'),('2', '2'),('3', '3'),('4', '4'),('5', '5'),('6', '6'),('7', '7'),('8', '8'),('9 ve Üstü', '9 ve Üstü'))
    
    advertiser = models.ForeignKey('auth.User',on_delete=models.CASCADE,verbose_name="ilan_sahibi")
    title = models.CharField(max_length=40,verbose_name="baslik")
    content = models.TextField(verbose_name="icerik")
    price = models.IntegerField(verbose_name="fiyat")
    gender = models.CharField(max_length=15, choices=gender_choices)
    age = models.CharField(max_length=20, choices=age_choices)
    created_date = models.DateTimeField(auto_now_add=True,verbose_name="ilan_tarihi")
    address = models.CharField(max_length=15, choices=il_choices)
    phone = models.IntegerField(verbose_name="telefon")
    image = models.ImageField(upload_to='files/covers',verbose_name="fotograf")

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created_date'] 
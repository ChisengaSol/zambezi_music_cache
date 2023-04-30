from django.db import models
from user_accounts.models import User

class Musician(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
    )
    stage_name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='images/',null=True)
    bio = models.TextField(null=True)

    def __str__(self):
        return self.stage_name

class Album(models.Model):
    title = models.CharField(max_length=255)
    musician = models.ForeignKey(
        Musician,
        on_delete=models.CASCADE,
    )
    price = models.DecimalField(max_digits=10,decimal_places=2)
    image = models.ImageField(upload_to='images/')
    description = models.TextField(null=True)
    release_date = models.DateTimeField()


class Track(models.Model):
    musician = models.ForeignKey(
        Musician,
        on_delete=models.CASCADE,
    )
    title = models.CharField(max_length=255)
    description = models.TextField(null=True)
    image = models.ImageField(upload_to='images/',null=True)
    file = models.FileField(upload_to='music/')
    album = models.ForeignKey(Album, on_delete= models.CASCADE,null=True)
    price = models.DecimalField(max_digits=10,decimal_places=2)
    is_available = models.BooleanField(default=False)
    release_date = models.DateTimeField()

class Listener(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
    )

    balance = models.DecimalField(max_digits=10,decimal_places=2,default=0.0)

class Listens(models.Model):
    listener = models.ForeignKey(
        Listener,
        on_delete=models.CASCADE,
    )

    track = models.ForeignKey(Track,on_delete=models.CASCADE)
    listen_date = models.DateTimeField()
    
class Purchase(models.Model):
    listener = models.ForeignKey(
        Listener,
        on_delete=models.CASCADE,
    )

    track = models.ForeignKey(Track,on_delete=models.CASCADE)
    purchase_date = models.DateTimeField()

    amount = models.DecimalField(max_digits=10,decimal_places=2)

class Payments(models.Model):
    purchase = models.ForeignKey(Purchase,on_delete=models.CASCADE)
    listener = models.ForeignKey(
        Listener,
        on_delete=models.CASCADE,
    )
    amount = models.DecimalField(max_digits=10,decimal_places=2)

    payment_date = models.DateTimeField()




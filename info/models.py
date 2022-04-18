from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
class Profile(models.Model):
    username = models.CharField(max_length=100, blank =True )
    bio = models.TextField(max_length=300,blank =True)
    user = models.OneToOneField(User, on_delete = models.CASCADE , related_name='profile')
    email = models.CharField(max_length=100, default = '')
    location = models.CharField(max_length=100,blank =True)
    neighbourhood = models.ForeignKey("Neighbourhood",on_delete=models.CASCADE, default='', null=True, blank=True)
    profile_pic = models.ImageField( upload_to='profile/', blank ='true',default='default.png')

    def __str__(self):
        return f'{self.user.username} Profile'

    def save_profile(self):
        self.save
    
    def delete_user(self):
        self.delete()


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):

    if created:
        Profile.objects.create(user=instance)


class Business(models.Model):
    name = models.CharField(max_length=50)
    user = models.ForeignKey(User,on_delete=models.CASCADE,default = '')
    email = models.CharField(max_length=100, default = '')
    neighbourhood = models.ForeignKey("Neighbourhood",on_delete=models.CASCADE, default='', null=True, blank=True)
    description = models.TextField( default = '')



    def __str__(self):
        return f'{self.name} business'


    def save_business(self):
        self.save()

    def delete_business(self):
        self.delete()

    @classmethod
    def hood_biz(cls, id):
        hoodbiznas = Business.objects.filter(neighbourhood = id)
        return hoodbiznas
  

class Post(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField()
    user = models.ForeignKey(User,on_delete=models.CASCADE,default = '')
    date = models.DateField(auto_now_add=True)
    neighbourhood = models.ForeignKey("Neighbourhood",on_delete=models.CASCADE, default='', null=True, blank=True)
    

    @classmethod
    def hood_post(cls,id):
        hoodpost = Post.objects.filter(neighbourhood = id)
        return hoodpost
    
    def __str__(self):
        return f'{self.title} Post'

    def save_post(self):
        self.save()

    def delete_post(self):
        self.delete()


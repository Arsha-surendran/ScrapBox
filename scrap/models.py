from django.db import models

from django.contrib.auth.models import User

from datetime import datetime

from django.utils import timezone

from django.db.models.signals import post_save

# Create your models here.
class UserProfile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,related_name="profile")
    first_name=models.CharField(max_length=200)
    last_name=models.CharField(max_length=200)
    address=models.CharField(max_length=200,null=True)
    phone=models.CharField(max_length=200,null=True)
    profile_pic=models.ImageField(upload_to="profilepics",null=True,blank=True)

    def __str__(self):
        return self.user.username
    
class Category(models.Model):
    name=models.CharField(max_length=200) 

    def __str__(self):
        return self.name
    
class Scraps(models.Model):
    name=models.CharField(max_length=200) 
    condition=models.CharField(max_length=200)
    price=models.PositiveIntegerField() 
    picture=models.ImageField(upload_to="scrap_pic",null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="scrap_user")
    place=models.CharField(max_length=200)
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    created_date=models.DateTimeField(auto_now_add=True)
    status_option={
        ("sold","sold"),
        ("available","available")

    }
    status=models.CharField(max_length=200,choices=status_option,default="available")


    def __str__(self):
        return self.name



class Wishlist(models.Model):
    scrap=models.ManyToManyField(Scraps,related_name="wished_scrap") 
    user=models.ForeignKey(User,on_delete=models.CASCADE,related_name="user_wish")
    created_date=models.DateTimeField(auto_now_add=True)

class Bids(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,related_name="bids_user")
    scrap=models.ForeignKey(Scraps,on_delete=models.CASCADE) 
    amount=models.PositiveIntegerField() 
    bids_option=(
        ("pending","pending"),
        ("accept","accept"),
        ("reject","reject")
    )
    status=models.CharField(max_length=200,choices=bids_option,default="pending")
    def __str__(self):
        return self.amount

class Reviews(models.Model):
    scrap=models.ForeignKey(Scraps,on_delete=models.CASCADE,related_name="scrap_view") 
    user=models.OneToOneField(User,on_delete=models.CASCADE,related_name="user_bids")
    comment=models.CharField(max_length=200)
    rating=models.PositiveIntegerField()

    def __str__(self):
        return self.comment
    
class pay(models.Model):
    acno=models.PositiveIntegerField()   
    Bankname=models.CharField(max_length=200)
    IFSC=models.CharField(max_length=200) 
    branch=models.CharField(max_length=200)
    payment_option={
        ("UPI","UPI"),
        ("credit/debit card","credit/debit card"),
        
        ("Rupay","Rupay")

    }
    payment=models.CharField(max_length=200,choices=payment_option,default="UPI")

    
    def __str__(self):
        return self.Bankname
        


def create_profile(sender,created,instance,**kwargs):
    if created:
        UserProfile.objects.create(user=instance)
        print("created")

post_save.connect(create_profile,sender=User)



        
   


 


 

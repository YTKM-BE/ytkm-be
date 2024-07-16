from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager

class MyUserManager(BaseUserManager):
   def create_user(self,kakao_sub,nickname,password=None):
       if not kakao_sub:
           raise ValueError("User must have kakao_sub")
       user = self.model(kakao_sub=kakao_sub)
       user.nickname = nickname
       user.set_password(password)
       user.save()
       return user
   
   def super_user(self,kakao_sub,nickname,password=None):
       if not kakao_sub:
           raise ValueError("User must have kakao_sub")
       user = self.model(kakao_sub=kakao_sub)
       user.nickname = nickname
       user.set_password(password)
       user.is_admin = True
       user.save()
       return user
   
class MyUser(AbstractBaseUser):
    nickname = models.CharField(max_length=10)
    kakao_sub = models.IntegerField(unique=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    objects = MyUserManager()

    USERNAME_FIELD = 'kakao_sub'
    REQUIRED_FIELDS = ['nickname']


class Medicine(models.Model):
    item_seq = models.IntegerField()

class Schedule(models.Model):
    member_id = models.ForeignKey(MyUser,on_delete=models.CASCADE)
    medicine_id = models.ForeignKey(Medicine,on_delete=models.CASCADE)
    datetime = models.DateTimeField()


class Tag(models.Model):
    schedule_id = models.ForeignKey(Schedule,on_delete=models.CASCADE)
    content = models.CharField(max_length=10)

class Scrap(models.Model):
    SCRAP_CATEGORY_CHOICES = (
        ("FAVORITE","즐겨찾기"),
        ("LIKE","효과가 좋았던 약"),
        ("DISLIKE","효과가 안좋았던 약")
    )
    member_id = models.ForeignKey(MyUser,on_delete=models.CASCADE)
    medicine_id = models.ForeignKey(Medicine,on_delete=models.CASCADE)
    category = models.CharField(choices=SCRAP_CATEGORY_CHOICES, max_length=15)
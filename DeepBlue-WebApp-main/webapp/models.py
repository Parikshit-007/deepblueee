from django.db import models
from django.contrib.auth.models import User

 # add this line


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, default=None)
    first_name = models.CharField(max_length=50,default='')
    username = models.CharField(max_length=50, default='')
    email = models.EmailField(default='')
    password = models.CharField(max_length=100,default='')
    video_file = models.FileField(upload_to="main/videos",default='default_value')
    
    def register(self):
        self.save()

    # ...

    # ...2

  
    @staticmethod
    def get_user_by_email(email):
        try:
            return UserProfile.objects.get(email=email)
        except:
            return False
  
    def isExists(self):
        if UserProfile.objects.filter(email=self.email):
            return True
  
        return False   

    def __str__(self):
       return self.user.username    
class Video(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, default=None)
    title = models.CharField(max_length=100)
    description = models.TextField()
    upload_date = models.DateTimeField(auto_now_add=True)
    video_file = models.FileField(upload_to="main/videos")
# Create your models here.

class Summary(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    video = models.ForeignKey(Video, on_delete=models.CASCADE)
    summary_text = models.TextField()
    generated_date = models.DateTimeField(auto_now_add=True)

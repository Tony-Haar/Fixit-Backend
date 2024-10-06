from django.db import models
from django.conf import settings
#from django.contrib.auth.models import User  # Assuming we are using Django's built-in User model
from Domains.models import Domain


# Create your models here.
    
class Professional(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete = models.CASCADE, related_name = "professional")
    #domain = models.OneToOneField(Domain, on_delete = models.CASCADE)
    domain = models.ForeignKey(Domain, on_delete=models.CASCADE)
    photo = models.CharField(max_length = 255, blank = True, null = True)
    availability = models.BooleanField(default = True)
    rating = models.FloatField(default = 0.0)

    def __str__(self):
        return self.user.username

class Profile(models.Model):
    professional = models.OneToOneField(Professional, on_delete = models.CASCADE, related_name = 'profile')
    about = models.TextField(blank = True, null = True)
    title = models.CharField(max_length = 100, blank = True, null = True)
    year_of_experience = models.IntegerField(default = 0)

    def __str__(self):
        return f"{self.professional.user.username}'s Profile"
    
class ExperienceBackground(models.Model):
    worked_at = models.CharField(max_length = 100)
    duration = models.CharField(max_length = 50)
    title = models.CharField(max_length = 100)
    assigned_work = models.TextField()
    profile = models.ForeignKey(Profile, on_delete = models.CASCADE, related_name = 'experience_backgrounds')

    def __str__(self):
        return f"{self.title} at {self.worked_at}"

class Video(models.Model):
    professional = models.ForeignKey(Professional, on_delete = models.CASCADE, related_name = 'videos')
    video_url = models.CharField(max_length = 255)

    # setting display name(appears on the admin panel) of the Video model dynamically 
    #in this like(display name is going to set to whatever the video_url)
    def __str__(self):
        return self.video_url # we could have returned here e.g 'professional video'
    
class Image(models.Model):
    professional = models.ForeignKey(Professional, on_delete = models.CASCADE, related_name = 'images')
    image_url = models.CharField(max_length = 255)

    def __str__(self):
        return self.image_url

    

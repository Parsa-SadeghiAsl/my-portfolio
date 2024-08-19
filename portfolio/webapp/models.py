from django.db import models

# Home Models
class Home(models.Model):
    name = models.CharField(max_length = 20)
    greeting_1 = models.CharField(max_length=10)
    greeting_2 = models.CharField(max_length=10)
    picture = models.ImageField(upload_to='picture/')
    updated = models.DateTimeField(auto_now = True)

    def __str__(self):
        return self.name
    
    
# About Models
class About(models.Model):
    heading = models.CharField(max_length = 50)
    career = models.CharField(max_length = 20)
    description = models.TextField(blank=False)
    profile_pic = models.ImageField(upload_to='profile/')
    updated = models.DateTimeField(auto_now = True)

    def __str__(self):
        return self.career


# Contact Models
class Profile(models.Model):
    about = models.ForeignKey(About,
                              on_delete=models.CASCADE)
    social_name = models.CharField(max_length  = 20)
    link = models.URLField(max_length=200)
    

# Services Models
class Category(models.Model):
    name = models.CharField(max_length  = 20)
    updated = models.DateTimeField(auto_now  = True)
    
    class Meta:
        verbose_name = 'skill'
        verbose_name_plural = 'Skills'
        
        def __str__(self):
            return self.name
        


# skill Models
class skills(models.Model):
    skill_name = models.CharField(max_length   = 20)
    category = models.ForeignKey(Category, on_delete = models.CASCADE)
    
    


class portfolio(models.Model):
    image = models.ImageField(upload_to='portfolio/')
    link = models.URLField(max_length=200)

    def __str__(self):
        return self.link
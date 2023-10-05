from django.db import models

# Create your models here.
class Images(models.Model):
    home_image = models.ImageField(upload_to="images", null=True ,blank=True)
    about_image = models.ImageField(upload_to="images", null=True ,blank=True)


class CV(models.Model):
    cv_file = models.FileField(upload_to='cv/')



class about(models.Model):
    name = models.CharField(max_length=20)
    phone = models.CharField(max_length=20)
    email = models.EmailField(max_length=254 , null=True)
    location = models.CharField(max_length=50, default='Hasilpur.Punjab.Pakistan')

    def __str__(self):
        return self.name


class Projects(models.Model):
    title = models.CharField(max_length=30)
    desc = models.CharField (max_length=1000)
    image = models.ImageField(upload_to="images", null=True ,blank=True)

    def __str__(self):
        return self.title


class contact(models.Model):
    name = models.CharField(max_length=25)
    email = models.EmailField(max_length=255, null=True)
    desc = models.TextField()
    date = models.DateField()

    def __str__(self):
        return self.name




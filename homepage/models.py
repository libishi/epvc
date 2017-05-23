from __future__ import unicode_literals
from django.utils import timezone
from django.db import models

################################### HOMEPAGE ############################

# Create your models here.
class Logo(models.Model):
    logoname = models.CharField(null=True,max_length=20)
    photo = models.ImageField(null=True, blank=True)

class Centernewsmain(models.Model):
    photo = models.ImageField(null=True, blank=True)
    readmore = models.CharField(null=True,max_length=200)
    details = models.TextField()
    def __str__(self):
        return self.readmore
    
class Centernews1(models.Model):
    photo = models.ImageField(null=True, blank=True)
    readmore = models.CharField(null=True,max_length=200)
    details = models.TextField()
    def __str__(self):
        return self.readmore

class Centernews2(models.Model):
    photo = models.ImageField(null=True, blank=True)
    readmore = models.CharField(null=True,max_length=200)
    details = models.TextField()
    def __str__(self):
        return self.readmore
    
class Centernews3(models.Model):
    photo = models.ImageField(null=True, blank=True)
    readmore = models.CharField(null=True,max_length=200)
    details = models.TextField()
    def __str__(self):
        return self.readmore
    

############################# NAVIGATION ###########################3
class Adr(models.Model):
    photo = models.ImageField(null=True, blank=True)
    file1 = models.FileField(null=True, blank=True)
    file2 = models.FileField(null=True, blank=True)
    file3 = models.FileField(null=True, blank=True)
    file4 = models.FileField(null=True, blank=True)
    file5 = models.FileField(null=True, blank=True)
    
class Contactus(models.Model):
    contact_type = models.CharField(max_length=200)
    contact_details = models.CharField(max_length=200)
    def __str__(self):
        return self.contact_type
        
class Faqs(models.Model):
    q = models.CharField(max_length=200)
    a = models.TextField()
    def __str__(self):
        return self.q

class Regionalcenters(models.Model):
    paragraph1 = models.TextField(max_length=200, null=True, blank=True)
    paragraph2 = models.TextField(max_length=200, null=True, blank=True)
    paragraph3 = models.TextField(max_length=200, null=True, blank=True)
    
class Subscribe(models.Model):
    email = models.EmailField()
    def __str__(self):
        return self.q

################# PV DEPARTMENT ################    
class Guideline(models.Model):
    paragraph1 = models.TextField(max_length=200, null=True, blank=True)
    paragraph2 = models.TextField(max_length=200, null=True, blank=True)
    paragraph3 = models.TextField(max_length=200, null=True, blank=True)
            

class Psur(models.Model):
    paragraph1 = models.TextField(max_length=200, null=True, blank=True)
    paragraph2 = models.TextField(max_length=200, null=True, blank=True)
    paragraph3 = models.TextField(max_length=200, null=True, blank=True)

class Rmp(models.Model):
    paragraph1 = models.TextField(max_length=200, null=True, blank=True)
    paragraph2 = models.TextField(max_length=200, null=True, blank=True)
    paragraph3 = models.TextField(max_length=200, null=True, blank=True)

class Pvnewsletters(models.Model):
    month = models.CharField(max_length=2, null=True, blank=True)
    year = models.CharField(max_length=4, null=True, blank=True)
    details = models.CharField(max_length=200, null=True, blank=True)
    newsletter = models.FileField()
    def __str__(self):
        return str(self.month) + ' - ' + str(self.year)

class Pvddl(models.Model):
    month = models.CharField(max_length=2, null=True, blank=True)
    year = models.CharField(max_length=4, null=True, blank=True)
    pvddl = models.FileField(null=True, blank=True)

class Legislation(models.Model):
    paragraph1 = models.TextField(max_length=200, null=True, blank=True)
    paragraph2 = models.TextField(max_length=200, null=True, blank=True)
    paragraph3 = models.TextField(max_length=200, null=True, blank=True)
    link1 = models.FileField(null=True, blank=True)
    link2 = models.FileField(null=True, blank=True)
    link3 = models.FileField(null=True, blank=True)
    link4 = models.FileField(null=True, blank=True)
    link5 = models.FileField(null=True, blank=True)
    link6 = models.FileField(null=True, blank=True)
    link7 = models.FileField(null=True, blank=True)
    link8 = models.FileField(null=True, blank=True)
    link9 = models.FileField(null=True, blank=True)
    link10 = models.FileField(null=True, blank=True)
    link11 = models.FileField(null=True, blank=True)
    link12 = models.FileField(null=True, blank=True)
    
class Images(models.Model):
    guideline = models.ImageField(null=True, blank=True)
    psur = models.ImageField(null=True, blank=True)
    rmp = models.ImageField(null=True, blank=True)
    pvnewsletter = models.ImageField(null=True, blank=True)
    legisation = models.ImageField(null=True, blank=True)
    pvddl = models.ImageField(null=True, blank=True)
    
##########################    SUBSCRIBE   ###########################
class Post(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    
    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

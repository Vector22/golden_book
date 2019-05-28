"""post.models"""

from django.db import models
from django.contrib.auth.models import User


class Profil(models.Model):
    # The OneToOne relationship towards User's model
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    description = models.TextField(null=True, blank=True)
    web_site = models.URLField(null=True, blank=True)
    avatar = models.ImageField(null=True, upload_to="avatars/")
    signature = models.TextField(null=True, blank=True)
    suscribe_news = models.BooleanField(default=False)
    birth_date = models.DateField(verbose_name="Date of birth", null=True, blank=True)
    address_country = models.CharField(max_length=50, null=True, blank=True)
    address_city = models.CharField(max_length=50, null=True, blank=True)
    address_road = models.CharField(max_length=50, null=True, blank=True)
    address_zip_code = models.CharField(max_length=50, null=True, blank=True)

    class Meta:
        verbose_name = 'Profile'
        verbose_name_plural = 'Profiles'

    def __str__(self):
        return f"Profile of {self.user.username}"


class Category(models.Model):
    """The category class"""
    name = models.CharField(max_length=120)
    create_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
        ordering = ['name', ]

    def __str__(self):
        return self.name


class Post(models.Model):
    """The post class"""
    title = models.CharField(max_length=120)
    body = models.TextField()
    post_image = models.ImageField(null=True, blank=True, upload_to="images/")
    is_allowed = models.BooleanField(default=False)
    is_rejected = models.BooleanField(default=False)
    create_date = models.DateTimeField(auto_now_add=True)
    updateDate = models.DateTimeField(auto_now=True)

    author = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'
        ordering = ['title', ]

    def __str__(self):
        return f"{self.title}--{self.author.username}"

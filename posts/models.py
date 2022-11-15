from django.contrib.auth.models import User
from django.db import models
from django.core.validators import RegexValidator
from posts.validators import validate_image


class Post(models.Model):

    TYPE_POST = [
        ('BUSINESS', 'This post for Business'),
        ('PRIVATE', 'It’s Private post')
    ]

    STATUS_POST = [
        ('ACTIVE', 'Post is active'),
        ('DEACTIVATED', 'Post is deactivated')
    ]

    user_wishlist = models.ManyToManyField(User, related_name="user_wishlist", blank=True)
    owner = models.CharField(max_length=100)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex], max_length=17, unique=True, blank=True, null=True)
    title = models.CharField(max_length=100)
    text = models.TextField('Some information...')
    type = models.CharField(max_length=8, choices=TYPE_POST)
    price = models.FloatField(default=5)
    status = models.CharField(max_length=11, choices=STATUS_POST)
    image = models.ImageField(null=True, blank=True, upload_to="images/", validators=[validate_image])
    created = models.DateTimeField(verbose_name='date published')

    def __str__(self):
        return self.owner

    class Meta:
        verbose_name = 'Field'
        verbose_name_plural = 'Fields'

    def check_if_post_in_wishlist(self, user):
        return self.user_wishlist.filter(id=user.id).exists()
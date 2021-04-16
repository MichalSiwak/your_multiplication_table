from django.db import models
from django.contrib.auth.models import User

# STATUSES = (
#     (1, 'Parent'),
#     (2, 'Kid'),
# )


# class Profile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     account_type = models.IntegerField(choices=STATUSES, verbose_name='Typ konta', default=1)
#     profile_picture = models.ImageField(null=True, upload_to='profile')
#     points_counter = models.IntegerField(null=True)
#     available_points = models.IntegerField(null=True)

class User(User):
    parent = models.BooleanField(default=True)


class ProfileParent(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class ProfileKid(models.Model):
    parent = models.ForeignKey(ProfileParent, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    profile_picture = models.ImageField(null=True, upload_to='images/')
    points_counter = models.IntegerField(null=True)
    available_points = models.IntegerField(null=True)

    def __str__(self):
        return f'{self.user}'


class Categories(models.Model):
    name = models.CharField(max_length=255, verbose_name='Nazwa')
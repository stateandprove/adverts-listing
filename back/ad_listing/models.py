from django.db import models
from django.utils import timezone


class Category(models.Model):

    #unique=True will create index for this field.
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Categories"


class City(models.Model):

    # We'd also like to have unique city names so we can effectively filter
    # by this field. If there are two cities with the same name, we need to
    # specify a larger subdivision (e.g., Portland, Maine and Portland, Oregon)
    # However, in real-world scenarios, we may want to implement custom models 
    # for larger subdivisions. We'll reserve 100 chars for this.
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Cities"


class Advert(models.Model):
    title = models.CharField(max_length=250)
    created = models.DateTimeField(default=timezone.now)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    views = models.PositiveIntegerField(default=0)

    # The other option for the description field is models.TextField(), but
    # TextField() will produce much slower filtering results on large db sizes,
    # so it's preferable to limit the number of characters in the description.
    description = models.CharField(max_length=5000)

    def __str__(self):
        return self.title

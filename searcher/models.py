from django.db import models
from .lists import GRAPHICS, PROCESSORS
from django_resized import ResizedImageField

GAME_CATEGORIES = [('A', 'A'), ('AA', 'AA'), ('AAA', 'AAA')]
ITEM_TYPES = [('Game', 'Game'), ('Software', 'Software'), ('Other', 'Other')]
RAM_LIST = [(1,'1GB'), (2, '2GB'), (3, '4GB'), (4, '6GB'), (5, '8GB'),
(6, '12GB'), (7, '14GB'), (8, '16GB'), (9, '32GB'), (10, '64GB+')]

class Software(models.Model):
    name = models.CharField(max_length=150)
    acronym = models.CharField(max_length=50, null=True, blank=True)
    image = ResizedImageField(size=[500, 500], upload_to='softwares', null=True, blank=True, crop=['middle','center'], quality=85)
    sinopse = models.TextField(null=True, blank=True)
    category = models.CharField(max_length=3, null=True, blank=True, choices=GAME_CATEGORIES)
    item_type = models.CharField(max_length=30, null=True, blank=True, choices=ITEM_TYPES)
    developer = models.CharField(max_length=150, null=True, blank=True)
    publisher = models.CharField(max_length=150, null=True, blank=True)
    website = models.CharField(max_length=150, null=True, blank=True)

    min_graphics_level = models.FloatField(choices=GRAPHICS)
    min_processor_level = models.FloatField(choices=PROCESSORS)
    min_memory_level = models.FloatField()

    max_graphics_level = models.FloatField(choices=GRAPHICS)
    max_processor_level = models.FloatField(choices=PROCESSORS)
    max_memory_level = models.FloatField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Computer(models.Model):
    COMPUTERS_CATEGORIES = [('Laptop', 'Laptop'), ('Desktop', 'Desktop'), ('Apple', 'Apple'), ('Other', 'Other')]

    title = models.CharField(max_length=255)
    acronym = models.CharField(max_length=100, null=True, blank=True)
    image = ResizedImageField(size=[800, 800], upload_to='computers', null=True, blank=True, crop=['middle','center'], quality=85)
    description = models.TextField(null=True, blank=True)
    category = models.CharField(max_length=100, choices=COMPUTERS_CATEGORIES)
    manufacturer = models.CharField(max_length=150, null=True, blank=True)
    affiliate_link = models.URLField()
    price = models.FloatField()

    graphics_level = models.FloatField(choices=GRAPHICS)
    processor_level = models.FloatField(choices=PROCESSORS)
    memory_level = models.FloatField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class LeadList(models.Model):
    nome = models.CharField(max_length=255, null=True, blank=True)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15, null=True, blank=True)
    birthday = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.email
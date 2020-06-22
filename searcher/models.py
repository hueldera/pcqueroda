from django.db import models

class Software(models.Model):
    GAME_CATEGORIES = [('A', 'A'), ('AA', 'AA'), ('AAA', 'AAA')]

    name = models.CharField(max_length=150)
    acronym = models.CharField(max_length=50, null=True, blank=True)
    image = models.ImageField(upload_to='softwares', null=True, blank=True)
    sinopse = models.TextField(null=True, blank=True)
    category = models.CharField(max_length=3, null=True, blank=True, choices=GAME_CATEGORIES)
    developer = models.CharField(max_length=150, null=True, blank=True)
    publisher = models.CharField(max_length=150, null=True, blank=True)
    website = models.CharField(max_length=150, null=True, blank=True)

    min_graphics_level = models.IntegerField()
    min_processor_level = models.IntegerField()
    min_memory_level = models.IntegerField()

    max_graphics_level = models.IntegerField()
    max_processor_level = models.IntegerField()
    max_memory_level = models.IntegerField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Computer(models.Model):
    COMPUTERS_CATEGORIES = [('Notebook', 'Notebook'), ('Desktop', 'Desktop'), ('Apple', 'Apple'), ('Other', 'Other')]

    title = models.CharField(max_length=255)
    acronym = models.CharField(max_length=100, null=True, blank=True)
    image = models.ImageField(upload_to='computers', null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    category = models.CharField(max_length=100, choices=COMPUTERS_CATEGORIES)
    manufacturer = models.CharField(max_length=150, null=True, blank=True)
    affiliate_link = models.URLField()

    price = models.FloatField()

    graphics_level = models.IntegerField()
    processor_level = models.IntegerField()
    memory_level = models.IntegerField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

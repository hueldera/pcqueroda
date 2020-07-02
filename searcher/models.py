from django.db import models

GAME_CATEGORIES = [('A', 'A'), ('AA', 'AA'), ('AAA', 'AAA')]
ITEM_TYPES = [('Game', 'Game'), ('Software', 'Software'), ('Other', 'Other')]
RAM_LIST = [(1,'1GB'), (2, '2GB'), (3, '4GB'), (4, '6GB'), (5, '8GB'), 
(6, '12GB'), (7, '14GB'), (8, '16GB'), (9, '32GB'), (10, '64GB+')]
PROCESSOR_LIST = [(1, 'Lower Pentium/Athlon'), (2, 'Higher Pentium/Athlon'), 
(3, 'Lower i3/Ryzen/FX' ), (4, 'Higher i3/Ryzen/FX' ), (5, 'Lower i5/Ryzen/FX'), 
(6, 'Higher i5/Ryzen/FX' ), (7, 'Lower i7/Ryzen/FX'), (8, 'Higher i7/Ryzen/FX'),
(9 ,'Lower i9/Ryzen' ), (10, 'Higher i9/Ryzen' )]
GRAPHICS_LIST = [
(1, 'Lower Intel/GT/Vega'), (2, 'Medium Intel/GT/Vega'), (3, 'Higher Intel/GT/Vega'), 
(4, 'Lower Intel/GTX/Radeon'), (5, 'Intel/GTX/Radeon'), (6, 'Higher GTX/Radeon' ), 
(5, 'Lower RTX/Radeon'), (6, 'Medium RTX/Radeon'), (7, 'Higher RTX/Radeon' ), 
(8, 'Lower Titan/Radeon'), (9, 'Medium Titan/Radeon'), (10, 'Higher Titan/Radeon')
]

class Software(models.Model):
    name = models.CharField(max_length=150)
    acronym = models.CharField(max_length=50, null=True, blank=True)
    image = models.ImageField(upload_to='softwares', null=True, blank=True)
    sinopse = models.TextField(null=True, blank=True)
    category = models.CharField(max_length=3, null=True, blank=True, choices=GAME_CATEGORIES)
    item_type = models.CharField(max_length=30, null=True, blank=True, choices=ITEM_TYPES)
    developer = models.CharField(max_length=150, null=True, blank=True)
    publisher = models.CharField(max_length=150, null=True, blank=True)
    website = models.CharField(max_length=150, null=True, blank=True)

    min_graphics_level = models.IntegerField(choices=GRAPHICS_LIST)
    min_processor_level = models.IntegerField(choices=PROCESSOR_LIST)
    min_memory_level = models.IntegerField(choices=RAM_LIST)

    max_graphics_level = models.IntegerField(choices=GRAPHICS_LIST)
    max_processor_level = models.IntegerField(choices=PROCESSOR_LIST)
    max_memory_level = models.IntegerField(choices=RAM_LIST)

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

    graphics_level = models.IntegerField(choices=GRAPHICS_LIST)
    processor_level = models.IntegerField(choices=PROCESSOR_LIST)
    memory_level = models.IntegerField(choices=RAM_LIST)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

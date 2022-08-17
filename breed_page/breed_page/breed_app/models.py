from django.db import models

from breed_page.settings import BASE_DIR


blood_choices = [
    ('Hot', 'Hot'),
    ('Cold', 'Cold'),
    ('Warm', 'Warm')
]

discipline_choices = [
    ('Dressage', 'Dressage'),
    ('Show Jumping', 'Show Jumping'),
    ('Cross Country', 'Cross Country'),
    ('Eventing', 'Eventing'),
    ('Western Dressage', 'Western Dressage'),
    ('Reining', 'Reining'),
    ('Polo', 'Polo'),
    ('Horseball', 'Horseball'),
    ('Combined driving', 'Combined driving'),
    ('Flat racing', 'Flat racing'),
    ('Harness racing', 'Harness racing'),
    ('Skijoring', 'Skijoring'),
    ('Endurance Racing', 'Endurance Racing'),
    ('Vaulting', 'Vaulting'),
    ('Dancing', 'Dancing'),
    ('Rejoneo', 'Rejoneo'),
]


# Create your models here.

class Discipline(models.Model):
    name = models.CharField(max_length=32, choices=discipline_choices, unique=True, null=False)

    def __str__(self):
        return f"{self.name} discipline"


class Coat(models.Model):
    name = models.CharField(max_length=32, unique=True, null=False)

    def __str__(self):
        return f"{self.name} coat"


class Breed(models.Model):
    name = models.CharField(max_length=128, unique=True, null=False)
    description = models.TextField(max_length=2048, null=False)
    avg_height = models.FloatField(null=False)
    avg_weight = models.FloatField(null=False)
    country = models.CharField(max_length=128)
    blood = models.CharField(max_length=16, choices=blood_choices, null=False)
    image = models.ImageField(upload_to=BASE_DIR / 'breed_page/static/', null=True, blank=True)
    coat = models.ManyToManyField(Coat, related_name='breed_to_coats')
    discipline = models.ManyToManyField(Discipline, related_name='breed_to_disciplines')
    predecessor = models.ManyToManyField('self', symmetrical=False, related_name='breed_to_predecessors', null=True, blank=True)

    def __str__(self):
        return f"{self.name} breed"
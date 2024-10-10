from django.db import models

# Create your models here.


class Medication(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    side_effects = models.TextField()
    dosage = models.TextField()
    precautions = models.TextField()
    interactions = models.TextField()
    contraindications = models.TextField()
    warnings = models.TextField()

    def __str__(self):
        return self.name

from django.db import models
from django.utils.text import slugify

class Ticket(models.Model):
    name = models.CharField(max_length=150)
    slug = models.SlugField(max_length=50, unique=True)
    owner = models.ForeignKey('auth.User')
    description = models.CharField(max_length=300, blank=True, null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.name)
        super(Ticket, self).save(*args, **kwargs)

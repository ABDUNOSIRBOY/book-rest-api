from django.db import models

class Author(models.Model):

    name = models.CharField(max_length=255)
    is_dead = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.name}"

class Book(models.Model):

    title = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    about = models.TextField(blank=True, null=True)
    janr = models.CharField(max_length=255)
    pages_count = models.PositiveSmallIntegerField(default=0)
    orders_count = models.PositiveIntegerField(default=0)
    image = models.ImageField(upload_to='books/', blank=True, null=True)

    def __str__(self):
        return f"{self.title}"
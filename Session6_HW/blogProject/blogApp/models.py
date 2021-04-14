from django.db import models

# Create your models here.
class Article(models.Model):
    categories = [
        ('movie', 'movie'),
        ('drama', 'drama'),
        ('programming', 'programming')
    ]
    
    category = models.CharField(
        max_length=11,
        choices=categories,
        default='movie'
    )
    title = models.CharField(max_length=200)
    article = models.TextField()
    written_time = models.DateTimeField(null=True, auto_now_add=True)

    def __str__(self):
        return self.title
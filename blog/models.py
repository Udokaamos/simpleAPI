from django.db import models
from django.contrib.auth import get_user_model
from django.forms import model_to_dict

User = get_user_model()
# Create your models here.


class Post(models.Model):
    GENRES = (
        ("Romance", "Romance"),
        ("Sci-Fi", "Sci-fi"),
        ("Fantasy", "Fantacy"),
        ("Mystery", "Mystery"),
        ("Thriller", "Thriller"),
        ("Westerns", "Westerns")
    )
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete= models.CASCADE,related_name='blog_posts')
    updated_on = models.DateTimeField(auto_now= True)
    content = models.TextField(max_length=200)
    date_created = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    genre = models.CharField(max_length=355, choices=GENRES, default=True)
    like = models.BooleanField(blank=True, default=True)

    

    def __str__(self) -> str:
        return f"{self.title} by {self.artist}"
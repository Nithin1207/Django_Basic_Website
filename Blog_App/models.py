from django.db import models
from django.utils.text import slugify
# Create your models here.
class DataBase(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    image = models.ImageField(upload_to="image_folder",null=True)
    slug = models.SlugField(unique=False, blank=True) 

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"[Name :  {self.name}] ||  [Address :  {self.address}] || [Image :  {self.image}] || [Slug : {self.slug}]"



class Comment(models.Model):
    user_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    text = models.TextField()
    post = models.ForeignKey("DataBase",on_delete=models.CASCADE, related_name="comment")

    def __str__(self):
        return f"[User Name :  {self.user_name}] ||  [Email :  {self.email}] || [Text :  {self.text}] || [Post : {self.post}]"

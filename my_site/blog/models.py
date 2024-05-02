from django.db import models
from django.core.validators import MinLengthValidator

# Create your models here.

class Author(models.Model):
  First_name = models.CharField(max_length=50)
  Last_name = models.CharField(max_length=50)
  Email_address = models.EmailField( max_length=254)

  def full_name(self):
    return f'{self.First_name} {self.Last_name}'

  def __str__(self):
    return self.full_name()

class Tag(models.Model):
  Caption = models.CharField(max_length=15)

  def __str__(self):
    return self.Caption

class Post(models.Model):
  Title = models.CharField(max_length=150)
  Excerpt = models.CharField(max_length=200)
  Image = models.ImageField(upload_to='posts', null= True)
  Date = models.DateField(auto_now=True)
  Slug = models.SlugField(unique=True, db_index = True) #this set automaticaly db_index = True when we use the slugfield and also when we use unique=True it create the db_index = True automaticaly 
  Content = models.TextField(validators=[MinLengthValidator(10)]) #we don't need to set a max_length but we could

  author = models.ForeignKey(Author, on_delete=models.SET_NULL, null=True, related_name = 'Posts') #set the author field to null if we delete an related author
  tags = models.ManyToManyField(Tag)


  def __str__(self):
      return f'{self.Title}'
  


class Comment(models.Model):
  user_name = models.CharField(max_length=120)
  user_email = models.EmailField()
  text = models.TextField(max_length=400)
  post = models.ForeignKey(Post , on_delete=models.CASCADE, related_name='comments')

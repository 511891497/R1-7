from django.db import models

# Create your models here.
class Author(models.Model):
    AuthorId = models.IntegerField(primary_key=True)
    Name = models.CharField(max_length=50)
    Age = models.IntegerField()
    Country = models.CharField(max_length=50)

    def __unicode__(self):
        return u"%d %s %d %s"%(self.AuthorId,self.Name,self.Age,self.Country)

class Book(models.Model):
    ISBN = models.IntegerField(primary_key=True)
    Title = models.CharField(max_length=50)
    AuthorId = models.ForeignKey(Author)
    Publisher = models.CharField(max_length=50)
    Publishdate = models.DateField(max_length=50)
    Price = models.FloatField()

    def __unicode__(self):
        return u"%s %s %d %s %s %f" %(self.ISBN,self.Title,self.AuthorId.AuthorId,self.publisher,self.Publishdata,self.Price)

from django.db import models
# Create your models here.



class Author(models.Model):
    name = models.CharField(max_length=65, null=True)

    def _str_(self):
        return self.name

    class Meta:
        app_label = 'books'


class Book(models.Model):
    book = models.ForeignKey(Author, on_delete=models.CASCADE)
    book_description = models.TextField(max_length=225)
    title = models.CharField(max_length=45)
    genre = models.CharField(max_length=25, null=True)
    year = models.DateField(null=True)
    stock = models.IntegerField()
    rented = models.IntegerField()
    sold = models.IntegerField()
    buy_amount = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    rent_amount = models.DecimalField(max_digits=10, decimal_places=2, null=True)


class Review(models.Model):
    review = models.ForeignKey(Book, on_delete=models.CASCADE)
    rating = models.TextField(max_length=225)

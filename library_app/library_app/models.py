from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=30)


class Book(models.Model):
    title = models.CharField(max_length=30)
    isbn = models.CharField(max_length=30)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)


class Patron(models.Model):
    name = models.CharField(max_length=30)
    card_number = models.IntegerField()
    email = models.CharField(max_length=30)


# Join Table
class Hold(models.Model):
    date_placed = models.DateField()
    patron = models.ForeignKey(Patron, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)


# Join Table
class Loan(models.Model):
    patron = models.ForeignKey(Patron, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    due_date = models.DateField()
    is_renewed = models.BooleanField(default=False)



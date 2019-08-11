from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=30)
    year = models.IntegerField()

class Chapter(models.Model):
    title = models.CharField(max_length=30)

class Reader(models.Model):
    name = models.CharField(max_length=30)
    age = models.IntegerField()

class Author(models.Model):
    name = models.CharField(max_length=30)

class Books_readers(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    reader = models.ForeignKey(Reader, on_delete=models.CASCADE)

class Books_authors(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

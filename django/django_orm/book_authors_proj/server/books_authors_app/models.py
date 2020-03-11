from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=100)
    desc = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        s = '\n'
        s += f"title: {self.title}\n"
        s += f"desc: {self.desc}\n"
        return s

class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    notes = models.TextField()
    books = models.ManyToManyField(Book, related_name="authors")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        s = '\n'
        s += f"fisrt_name: {self.first_name}\n"
        s += f"last_name: {self.last_name}\n"
        return s
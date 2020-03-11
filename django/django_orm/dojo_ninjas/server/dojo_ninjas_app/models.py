from django.db import models


class Dojos(models.Model):
    name = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        s = '\n'
        s += f"name: {self.name}\n"
        s += f"city: {self.city}\n"
        s += f"state: {self.state}\n"
        return s


class Ninjas(models.Model):
    dojos = models.ForeignKey(
        Dojos, related_name="ninjas",
        on_delete=models.CASCADE
    )
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        s = '\n'
        s += f"first_name: {self.first_name}\n"
        s += f"last_name: {self.last_name}\n"
        return s

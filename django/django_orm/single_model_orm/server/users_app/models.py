from django.db import models

class User(models.Model):
    first_name = models.CharField(max_length= 45)
    last_name = models.CharField(max_length= 45)
    email = models.CharField(max_length= 100)
    age = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    def __str__(self):
        s = '\n'
        s += f"first_name: {self.first_name}\n"
        s += f"last_name: {self.last_name}\n"
        s += f"email: {self.email}\n"
        s += f"age: {self.age}\n"
        return s



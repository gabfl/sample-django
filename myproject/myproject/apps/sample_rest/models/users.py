from django.db import models


class User(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=200)

    def getUser(self, userId):
        users = self.getUsers()
        return users[userId]

    def getUsers(self):
        """List of users"""
        users = []
        users.append({'name': 'Gab', 'email': 'gab@gmail.com'})
        users.append({'name': 'Bob', 'email': 'bob@gmail.com'})
        users.append({'name': 'Tom', 'email': 'tom@gmail.com'})

        return users

    def __str__(self):
        return self.name

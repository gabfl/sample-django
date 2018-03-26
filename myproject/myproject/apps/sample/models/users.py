class User:

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

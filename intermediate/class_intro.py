class User:
    def __init__(self, id, username):
        self.id = id
        self.username = username
        self.followers = 0
        self.following = 0

    def follow(self, user):
        user.followers += 1
        self.following += 1


user1 = User("001", "Abner")

user2 = User("002", "Tapioca")

user1.follow(user2)

print(user1.followers)
print(user1.following)
print(user2.followers)
print(user2.following)

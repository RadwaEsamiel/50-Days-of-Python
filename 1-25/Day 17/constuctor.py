class User :
    def __init__(self,username,user_id):
        self.id = user_id
        self.username = username
        self.followers = 0
        self.following = 0

    def follow(self,user):
        user.followers += 1
        self.following += 1



user_1 = User("radwa", "123")
user_2 = User("angela", "456")

user_2.follow(user_1)
print(user_1.followers)
print(user_2.followers)
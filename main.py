# constrocture = initialize

class User:
    # constructor
    def __init__(self, user_id, username):
        # self is the object
        self.id = user_id
        self.username = username
        self.followers = 0
        self.following = 0

    def follow(self, user):
        user.followers += 1
        self.following += 1
    # pass # to next line


""" Manual """
# object = # class
user_1 = User("100", "angela")
user_2 = User("2", "adam")

user_1.follow(user_2)

print(user_1.followers)
print(user_1.following)
print(user_2.followers)
print(user_2.following)
# PascalCase: ThisIsAllWordsUpperCase
# camelCase: allWordsUpperCaseExceptTheFirst
# snake_case: all_words_lower_Case_separated_by_underscore


class User:

    #  constructor
    def __init__(self, user_id, username):  # self is the actual object being created and initialised
        self.id = user_id
        self.username = username
        self.followers = 0  # default value without adding it to the constructor attributes
        self.following = 0

    def follow(self, user):
        user.followers += 1
        self.following += 1


user_1 = User("001", "Ancuta")

print(f"User1: {user_1.username} with {user_1.followers} followers.")

user_2 = User("002", "Maria")
print(f"User2: {user_2.username}")

user_3 = User("003", "Gheorghe")
print(f"User2: {user_3.username}\n\n")

user_1.follow(user_2)
user_2.follow(user_1)
user_3.follow(user_1)

print(f"{user_1.username} has {user_1.followers} followers and is following {user_1.following} user(s).")
print(f"{user_2.username} has {user_2.followers} followers and is following {user_2.following} user(s).")
print(f"{user_3.username} has {user_3.followers} followers and is following {user_3.following} user(s).")




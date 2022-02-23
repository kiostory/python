# class User:         #User라는 class를 만들꺼야. User가 가진것, User가 할수 있는 것을 명시
#     pass            #별 정의없이 이번에는 그냥 넘어가자

class User:

    def __init__(self, user_id, user_name):
        self.id = user_id
        self.username = user_name
        self.followers = 0
        self.following = 0

    def follow(self, user):
        user.followers += 1
        self.following += 1


user1 = User("001", "kio")
user2 = User("002", "jack")

print(user1.id, user1.username, user1.followers)
print(user2)
print(user2.followers)

user1.follow(user2)
print(user1.username, user1.followers, user1.following)
print(user2.username, user2.followers, user2.following)




import time
from hashlib import sha1
from time import sleep


class User:
    users_list = []

    def __init__(self, nickname='', password='', age=0):
        self.nickname = nickname
        self.password = password
        self.age = age

    def __str__(self):
        return self.nickname

    def __repr__(self):
        return f'{self.nickname}, {self.password}, {self.age}'

    def __eq__(self, other):
        for user in self.users_list:
            if other == user.nickname:
                return user


class Video:
    videos_list = []

    def __init__(self, title='', duration=0, time_now=0, adult_mode=False):
        self.title = str(title)
        self.duration = duration
        self.time_now = time_now
        self.adult_mode = adult_mode

    def __repr__(self):
        return f"{self.title}, {self.duration}, {self.time_now}, {self.adult_mode}"

    def __eq__(self, other):
        for video in self.videos_list:
            if other == video.title:
                return video


class UrTube:
    def __init__(self):
        self.current_user = None

    def log_in(self, nickname, password):
        hash_obj = sha1(password.encode())
        hashed_pas = hash_obj.hexdigest()
        for x in User.users_list:
            if x.nickname == nickname and x.password == hashed_pas:
                self.current_user = x
                print(self.current_user)

    def register(self, nickname, password, age):
        if nickname == User():
            return print(f'Пользователь {nickname} уже существует')
        else:
            hash_obj = sha1(password.encode())
            hashed_pas = hash_obj.hexdigest()
            user_reg = User(nickname, hashed_pas, age)
            User.users_list.append(user_reg)
            self.current_user = user_reg

    def log_out(self):
        self.current_user = None

    def add(self, *add_videos):
        for v in add_videos:
            Video.videos_list.append(v)

    def get_videos(self, search):
        find_videos = []
        for video in Video.videos_list:
            if search.lower() in video.title.lower():
                find_videos.append(video.title)
        return find_videos

    def watch_video(self, video):
        if self.current_user:
            for vid in Video.videos_list:
                if vid.title == video:
                    if vid.adult_mode and self.current_user.age < 18:
                        print('Вам нет 18 лет, пожалуйста покиньте страницу')
                    else:
                        for sec in range(vid.time_now, vid.duration):
                            vid.time_now += 1
                            print(vid.time_now)
                            time.sleep(1)
        else:
            return print('Войдите в аккаунт, чтобы смотреть видео')


ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

# Добавление видео
ur.add(v1, v2)

# Проверка поиска
print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))

# Проверка на вход пользователя и возрастное ограничение
ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.watch_video('Для чего девушкам парень программист?')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Для чего девушкам парень программист?')

# Проверка входа в другой аккаунт
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
print(ur.current_user)

# Попытка воспроизведения несуществующего видео
ur.watch_video('Лучший язык программирования 2024 года!')

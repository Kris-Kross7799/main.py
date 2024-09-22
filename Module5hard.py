import time


class User:

    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = hash(password)
        self.age = age

    def __str__(self):
        return self.nickname

    def __eq__(self, other):
        if isinstance(other, User):
            return self.nickname == other.nickname

class Video:

    def __init__(self, title, duration, adult_mode=False):
        self.title = title
        self.duration = duration
        self.time_now = 0
        self.adult_mode = adult_mode

    def __str__(self):
        return self.title

    def __repr__(self):
        return self.title


class UrTube:

    def __init__(self):
        self.users = []
        self.videos = []
        self.current_user = None


    def register(self, nickname, password, age):
        new_user = User(nickname, password, age)
        if new_user in self.users:
            print(f'Пользователь {nickname} уже существует')
        else:
            self.users.append(new_user)
            self.current_user = new_user


    def log_out(self):
        self.current_user = None

    def get_videos(self, search_video):
        video_list = []
        for video in self.videos:
            if search_video.lower() in str(video).lower():
                video_list.append(video)
        return video_list

    def watch_video(self, search_video):
        if self.current_user is None:
            print("Войдите в аккаунт")
            return
        for i in self.videos:
            if search_video == i.title:
                if self.current_user.age < 18 and i.adult_mode:
                    print("Вам нет 18, пожалуйста, покиньте страницу")
                else:
                    while i.time_now < i.duration:
                        i.time_now += 1
                        print(i.time_now, end=' ')
                        time.sleep(1)
                    i.time_now = 0
                    print("Конец видео")

    def log_in(self, nickname, password):
        for i in self.users:
            if nickname == i.nickname and hash(password) == i.password:
                self.current_user = i
                return i

    def add(self, *args: Video):
        for i in args:
            if i.title not in self.videos:
                self.videos.append(i)


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



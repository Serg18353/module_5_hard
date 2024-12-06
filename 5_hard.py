import time
class User:
    def __init__(self, name, age, password):
        self.name = name
        self.age = age
        self.password = password

    def __str__(self):
        return (f'{self.name}')

    def __eq__(self, other):
        return self.name == other.name

class Video:
    def __init__(self, title, duration, time_now = 0, adult_mode = False):
        self.title = title
        self.duration = duration
        self.time_now = time_now
        self.adult_mode = adult_mode

    def __str__(self):
        return f'{self.title}'

class UrTube:
    def __init__(self):
        self.users = []
        self.videos = []
        self.current_user = None

    def log_in(self, nickname, password):
        for i in self.users:
            if i.name == nickname and hash(i.password) == hash(password):
                self.current_user = i.name
                return
        print(f'Неверный логин или пароль')

    def register(self, nickname, password, age):
        for i in self.users:
            if i.name == nickname:
                print(f'Пользователь {nickname} уже существует')
                return
        user = User(name=nickname, age=age, password=hash(password))
        self.users.append(user)
        self.current_user = user

    def log_out(self):
        self.current_user = None


    def add(self, *videos):
        for i in videos:
            for j in self.videos:
                if i.title == j.title:
                    break
            else:
                self.videos.append(i)

    def get_videos(self, word:str):
        founded_videos = []
        for i in self.videos:
            if word.lower() in i.title.lower():
                founded_videos.append(i.title)
        return founded_videos

    def watch_video(self, title):
        if self.current_user is None:
            print('Войдите в аккаунт, чтобы смотреть видео')
            return
        for i in self.videos:
            if i.title == title:
                if i.adult_mode and self.current_user.age < 18:
                    print('Вам нет 18 лет, пожалуйста покиньте страницу')
                    return
                while i.time_now < i.duration:
                    print(i.time_now, end=' ')
                    time.sleep(1)
                    i.time_now += 1
                print('Конец видео')
                i.time_now = 0  # перезаписываем время





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

# # Проверка входа в другой аккаунт
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
print(ur.current_user)

# Попытка воспроизведения несуществующего видео
ur.watch_video('Лучший язык программирования 2024 года!')
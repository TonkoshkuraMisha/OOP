class Video:
    def create(self, name):
        self.name = name

    def play(self):
        print(f"воспроизведение видео {self.name}")


class YouTube:
    videos = []  # Статический список для хранения объектов Video

    @classmethod
    def add_video(cls, video):
        cls.videos.append(video)

    @classmethod
    def play(cls, video_indx):
        if 0 <= video_indx < len(cls.videos):
            video = cls.videos[video_indx]
            video.play()


# Создание объектов Video
v1 = Video()
v2 = Video()

# Задание имен для видео
v1.create("Python")
v2.create("Python ООП")

# Добавление видео в YouTube
YouTube.add_video(v1)
YouTube.add_video(v2)

# Воспроизведение первого и второго видео
YouTube.play(0)  # воспроизведение видео Python
YouTube.play(1)  # воспроизведение видео Python ООП

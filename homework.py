class InfoMessage:
    """Информационное сообщение о тренировке."""
    def __init__(self,
                 training_type: str,
                 duration: float,
                 distance: float,
                 speed: float,
                 calories: float) -> None:
        self.training_type = training_type
        self.duration = duration
        self.distance = distance
        self.speed = speed
        self.calories = calories

    def get_message(self) -> str:
        info_message = (f'Тип тренировки: {self.training_type}; '
                        f'Длительность: {self.duration:.3f} ч.; '
                        f'Дистанция: {self.distance:.3f} км; '
                        f'Ср. скорость: {self.speed:.3f} км/ч; '
                        f'Потрачено ккал: {self.calories:.3f}.')
        return info_message


class Training:
    """Базовый класс тренировки."""
    LEN_STEP = 0.65
    M_IN_KM = 1000
    M_IN_HOUR = 60

    def __init__(self,
                 action: int,
                 duration: float,
                 weight: float,
                 ) -> None:
        self.action = action
        self.duration = duration
        self.weight = weight

    def get_distance(self) -> float:
        """Получить дистанцию в км."""
        distance = self.action * self.LEN_STEP / self.M_IN_KM
        return distance

    def get_mean_speed(self) -> float:
        """Получить среднюю скорость движения."""
        mean_speed = self.get_distance() / self.duration
        return mean_speed

    def get_spent_calories(self) -> float:
        """Получить количество затраченных калорий."""
        pass

    def show_training_info(self) -> InfoMessage:
        """Вернуть информационное сообщение о выполненной тренировке."""
        info = InfoMessage(self.__class__.__name__,
                           self.duration,
                           self.get_distance(),
                           self.get_mean_speed(),
                           self.get_spent_calories())
        return info


class Running(Training):
    """Тренировка: бег."""
    def get_spent_calories(self) -> float:
        coeff_calorie_1 = 18
        coeff_calorie_2 = 20
        calories = ((coeff_calorie_1 * self.get_mean_speed() - coeff_calorie_2)
                    * self.weight / self.M_IN_KM
                    * self.duration * self.M_IN_HOUR)
        return calories


class SportsWalking(Training):
    """Тренировка: спортивная ходьба."""
    def __init__(self,
                 action: int,
                 duration: float,
                 weight: float,
                 height: float) -> None:
        super().__init__(action, duration, weight)
        self.height = height

    def get_spent_calories(self) -> float:
        coeff_calorie_1 = 0.035
        coeff_calorie_2 = 0.029
        calories = ((coeff_calorie_1 * self.weight
                    + (self.get_mean_speed()**2 // self.height)
                    * coeff_calorie_2 * self.weight)
                    * self.duration * self.M_IN_HOUR)
        return calories


class Swimming(Training):
    """Тренировка: плавание."""
    LEN_STEP = 1.38

    def __init__(self,
                 action: int,
                 duration: float,
                 weight: float,
                 length_pool: float,
                 count_pool: float) -> None:
        super().__init__(action, duration, weight)
        self.length_pool = length_pool
        self.count_pool = count_pool

    def get_mean_speed(self) -> float:
        mean_speed = (self.length_pool * self.count_pool
                      / self.M_IN_KM / self.duration)
        return mean_speed

    def get_spent_calories(self) -> float:
        coeff_calories_1 = 1.1
        coeff_calories_2 = 2
        calories = ((self.get_mean_speed() + coeff_calories_1)
                    * coeff_calories_2 * self.weight)
        return calories


def read_package(workout_type: str, data: list) -> Training:
    """Прочитать данные полученные от датчиков."""
    training_type = {'SWM': Swimming,
                     'RUN': Running,
                     'WLK': SportsWalking}
    training = training_type[workout_type]
    return training(*data)


def main(training: Training) -> None:
    """Главная функция."""
    info = training.show_training_info()
    print(info.get_message())


if __name__ == '__main__':
    packages = [
        ('SWM', [720, 1, 80, 25, 40]),
        ('RUN', [15000, 1, 75]),
        ('WLK', [9000, 1, 75, 180]),
    ]

    for workout_type, data in packages:
        training = read_package(workout_type, data)
        main(training)

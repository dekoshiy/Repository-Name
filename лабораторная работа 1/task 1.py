import doctest


class Formula1Bolide:
    def __init__(self, team: str, max_speed: int, fuel_level: float):
        """
        Создание и подготовка к работе объекта "Болид Формулы-1".

        :param team: Название команды
        :param max_speed: Максимальная скорость болида в км/ч
        :param fuel_level: Текущий уровень топлива в процентах (от 0 до 100)

        :raise TypeError: Если тип аргумента не соответствует аннотации
        :raise ValueError: Если значение аргумента некорректно

        Примеры:
        >>> bolid = Formula1Bolide("Ferrari", 350, 80.5)
        >>> bolid.team
        'Ferrari'
        >>> bolid.max_speed
        350
        >>> bolid.fuel_level
        80.5
        """
        if not isinstance(team, str):
            raise TypeError("Название команды должно быть строкой")
        if not team:
            raise ValueError("Название команды не может быть пустым")
        self.team = team

        if not isinstance(max_speed, int):
            raise TypeError("Максимальная скорость должна быть целым числом")
        if max_speed <= 0:
            raise ValueError("Максимальная скорость должна быть положительным числом")
        self.max_speed = max_speed

        if not isinstance(fuel_level, (int, float)):
            raise TypeError("Уровень топлива должен быть числом")
        if not (0 <= fuel_level <= 100):
            raise ValueError("Уровень топлива должен быть от 0 до 100 процентов")
        self.fuel_level = fuel_level

    def accelerate(self, speed_increase: int) -> None:
        """
        Ускорение болида на заданную величину.

        :param speed_increase: Увеличение скорости в км/ч
        :raise ValueError: Если увеличение скорости отрицательное

        Примеры:
        >>> bolid = Formula1Bolide("Mercedes", 340, 50)
        >>> bolid.accelerate(20)
        """
        if not isinstance(speed_increase, int):
            raise TypeError("Увеличение скорости должно быть целым числом")
        if speed_increase < 0:
            raise ValueError("Увеличение скорости должно быть положительным числом")
        ...

    def brake(self) -> None:
        """
        Применение торможения болида.

        :return: None

        Примеры:
        >>> bolid = Formula1Bolide("Red Bull", 355, 60)
        >>> bolid.brake()
        """
        ...

    def pit_stop(self, fuel_amount: float) -> float:
        """
        Проведение пит-стопа: дозаправка болида.

        :param fuel_amount: Объем добавляемого топлива в процентах
        :return: Новый уровень топлива после пит-стопа

        Примеры:
        >>> bolid = Formula1Bolide("McLaren", 345, 30.0)
        >>> bolid.pit_stop(45.0)
        75.0
        """
        if not isinstance(fuel_amount, (int, float)):
            raise TypeError("Объем топлива должен быть числом")
        if fuel_amount < 0:
            raise ValueError("Объем топлива должен быть положительным числом")
        ...


class Bed:
    def __init__(self, size: str, material: str, occupancy: int):
        """
        Создание и подготовка к работе объекта "Кровать"

        :param size: Размер кровати (например, "King", "Queen", "Single")
        :param material: Материал каркаса (например, "Wood", "Metal", "IKEA")
        :param occupancy: Максимальное количество людей, которые могут спать

        :raise TypeError: Если тип аргумента не соответствует аннотации
        :raise ValueError: Если значение аргумента некорректно

        Примеры:
        >>> bed = Bed("Queen", "Wood", 2)
        >>> bed.size
        'Queen'
        >>> bed.material
        'Wood'
        >>> bed.occupancy
        2
        """
        if not isinstance(size, str):
            raise TypeError("Размер кровати должен быть строкой")
        if not size:
            raise ValueError("Размер кровати не может быть пустым")
        self.size = size

        if not isinstance(material, str):
            raise TypeError("Материал должен быть строкой")
        if not material:
            raise ValueError("Материал не может быть пустым")
        self.material = material

        if not isinstance(occupancy, int):
            raise TypeError("Количество людей должно быть целым числом")
        if occupancy <= 0:
            raise ValueError("Количество людей должно быть положительным числом")
        self.occupancy = occupancy
        self.is_occupied = False

    def occupy(self) -> None:
        """
        Занять кровать.

        :return: None

        Примеры:
        >>> bed = Bed("Single", "Metal", 1)
        >>> bed.occupy()
        """
        ...

    def vacate(self) -> None:
        """
        Освободить кровать.

        :return: None

        Примеры:
        >>> bed = Bed("King", "Wood", 2)
        >>> bed.vacate()
        """
        ...

    def change_sheets(self, new_material: str) -> None:
        """
        Смена постельного белья/материала.

        :param new_material: Новый материал белья.

        :raise ValueError: Если материал пустой.

        Примеры:
        >>> bed = Bed("Queen", "Wood", 2)
        >>> bed.change_sheets("Cotton")
        """
        if not isinstance(new_material, str):
            raise TypeError("Материал должен быть строкой")
        if not new_material:
            raise ValueError("Материал не может быть пустым")
        ...


class WiredHeadphones:
    def __init__(self, brand: str, model: str, cable_length: float):
        """
        Создание и подготовка к работе объекта "Проводные наушники"

        :param brand: Марка наушников
        :param model: Модель наушников
        :param cable_length: Длина кабеля в метрах

        :raise TypeError: Если тип аргумента не соответствует аннотации
        :raise ValueError: Если значение аргумента некорректно

        Примеры:
        >>> headphones = WiredHeadphones("Sony", "MDR-ZX110AP", 1.2)
        >>> headphones.brand
        'Sony'
        >>> headphones.model
        'MDR-ZX110AP'
        >>> headphones.cable_length
        1.2
        """
        if not isinstance(brand, str):
            raise TypeError("Марка наушников должна быть строкой")
        if not brand:
            raise ValueError("Марка наушников не может быть пустой")
        self.brand = brand

        if not isinstance(model, str):
            raise TypeError("Модель наушников должна быть строкой")
        if not model:
            raise ValueError("Модель наушников не может быть пустой")
        self.model = model

        if not isinstance(cable_length, (int, float)):
            raise TypeError("Длина кабеля должна быть числом")
        if cable_length <= 0:
            raise ValueError("Длина кабеля должна быть положительным числом")
        self.cable_length = cable_length
        self.is_plugged_in = False

    def plug_in(self) -> None:
        """
        Подключение наушников к устройству (вставить штекер).

        :return: None

        Примеры:
        >>> headphones = WiredHeadphones("Sennheiser", "HD 206", 3.0)
        >>> headphones.plug_in()
        """
        ...

    def unplug(self) -> None:
        """
        Отключение наушников от устройства (вынуть штекер).

        :return: None

        Примеры:
        >>> headphones = WiredHeadphones("Audio-Technica", "ATH-M50x", 1.2)
        >>> headphones.unplug()
        """
        ...

    def adjust_volume_level(self, level: int) -> None:
        """
        Регулировка уровня громкости.

        :param level: Уровень громкости (от 0 до 100).

        :raise ValueError: Если уровень громкости выходит за допустимые пределы.

        Примеры:
        >>> headphones = WiredHeadphones("Beats", "urBeats3", 1.2)
        >>> headphones.adjust_volume_level(50)
        """
        if not isinstance(level, int):
            raise TypeError("Уровень громкости должен быть целым числом")
        if not (0 <= level <= 100):
            raise ValueError("Уровень громкости должен быть от 0 до 100")
        ...


if __name__ == "__main__":
    doctest.testmod()  # тестирование примеров для всех классов сразу

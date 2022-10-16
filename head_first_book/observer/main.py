from weather import WeatherData
from display import CurrentConditionsDisplay


weather_data = WeatherData()
conditions = CurrentConditionsDisplay()

if __name__ == '__main__':
    # Добавляем Субъект (weather_data) для Наблюдателя (conditions)
    conditions.add_subject(weather_data)
    # Субъект обновляет данные и оповещает всех Наблюдателей
    weather_data.set_measurements(35.5, 120, 130)
    conditions.display()
    # Субъект снова обновляет данные и снова оповещает
    weather_data.set_measurements(22, 121.1, 165.7)
    conditions.display()  # Данные в Наблюдателе также изменились

    print("The End")


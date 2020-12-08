# polytech_weather_bot

В данном курсовом проекте необходимо было разработать Telegram-бота на языке программирования Python, который собирает информацию о погоде из трёх различных источников и предоставляет её в структурированном виде пользователю по запросу. Во время разработки программы нашей команде необходимо было пройти все основные этапы создания программного обеспечения и улучшить свои навыки в создании качественных программных продуктов.

## Участники
Проект выполнили студенты группы 3530904/80102:
* Атаманова С.О.
* Кузнецов С.А.
* Тагиев А.Д.
* Шерман М.Л.

## Этапы проекта
### Постановка проблемы
В современном мире пользователям гораздо проще пользоваться мессенджерами, чем информационными сайтами, поэтому, чтобы сократить время поиска погоды, наша команда решила создать Telegram-бота, который с помощью простой команды смог бы показывать погоду в заданной местности. Для достоверности данных мы предоставляем пользователю информацию о погоде из трёх различных источников: Yandex.ru, Yr.no, openweathermap.org.

### Требования
* Пользователь должен иметь возможность получать данные о погоде из трёх источников
* Данные о погоде должны предоставляться в соответствии с адресом, введённым пользователем
* Если введённый адрес существует (как в России, так и в любой другой стране), то бот должен предоставить прогноз погоды
* Необходимо добавить обработку данных погоды и в зависимости от типа погоды (дождь, снег) предоставлять иконку с соответствующим изображением
* Должна быть реализована возможность сохранять избранный адрес для пользователя, по которому короткой командой можно получить данные о погоде
* Необходимо предоставить пользователю возможность передавать адрес боту с помощью геометки
* Бот должен быть доступен любому пользователю мессенджера Telegram
* Сборка и тестирование проекта должны выполняться одной командой в терминале

### Диаграммы
* Context Diagram
* Container Diagram

### Кодирование и отладка
Проект написан на языке программирования Python версии 3.8 с использованием библиотек python-telegram-bot (отвечает за поддержку бота серверами Telegram), beutifulsoup4 и requests (помогают получать данные с сайтов). Сборка проекта производилась с помощью Docker в контейнерах python:3.8-slim.

### Тестирование
Тестирование производилось с использованием стандартной библиотеки Python – unittest.

### Сборка
Для запуска проекта необходимы два токена, которые надо записать в файл src/config.py. Токен с названием token можно получить от бота мессенджера Telegram – BotFather. Второй токен с названием owm_api_key можно получить при регистрации на сайте OpenWeatherMap.
Сборка и тестирование проекта осуществляется с помощью команды: sh script.sh
При этом надо находиться в директории с проектом.
Script.sh создаёт контейнер с тестами, запускает его, после выполнения тестов контейнер удаляется и создаётся новый контейнер с нашим проектом.

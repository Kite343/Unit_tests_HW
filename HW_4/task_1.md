Задание 1. Ответьте письменно на вопросы:

1.  Почему использование тестовых заглушек может быть полезным при написании модульных тестов?

        Использование заглушек повышает автономность теста и его гибкость. Не нужно подгонять состояние системы для конкретного случая, можно настроить заглушку на возвращение нужного значения при вызове определенного метода.

2. Какой тип тестовой заглушки следует использовать, если вам нужно проверить, что метод был вызван с определенными аргументами?

        Следует использовать "spy" (наблюдатель). Спай позволяет отследить вызов метода и аргументы, с которыми он был вызван.       

3. Какой тип тестовой заглушки следует использовать, если вам просто нужно вернуть определенное значение или исключение в ответ на вызов метода?

        Stub. Stub-обьекты  предоставляют готовые ответы на наши вызовы,  они возвращают предопределённое значение.

4. Какой тип тестовой заглушки вы бы использовали для имитации  взаимодействия с внешним API или базой данных?

        В таком случае рекомендуется использовать "mock" (имитация). Мок предоставляет контролируемую имитацию внешнего ресурса, что позволяет провести тестирование в изолированной среде без реальных запросов к внешним ресурсам.
# readyscript_demo
Тесты для сайта https://mega.readyscript.ru/


## Запуск в докере

создать образ:
```sh
docker build -t readyscript_demo .
```

запустить контейнер:
```sh
docker run --name ready_demo readyscript_demo
```

## Запуск локально всех тестов
```sh
pytest tests
```

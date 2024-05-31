# Detection_project

Проект по курсу инженерии данных 2024, выполнили студенты МПИ-23-1-1

## Предварительные требования

### Установка проекта

```shell
python3.9 -m venv .detection_project
pip install -r requirements.txt
```

### Pre-commit

Для установки `pre-commit` следует выполнить следующие команды:

```shell
pip3 install pre-commit
pre-commit install
```

### Загрузка весов

Перед запуском проекта настоятельно рекоммендуется загрузить веса по [данной ссылке](https://github.com/ultralytics/assets/releases/download/v8.2.0/yolov8x.pt) и расположить их в директории **`./models`**:

```bash
mle-project-1
├── ...
├── models # <- в директории models
└── ...
```

## Выполненные задачи

- [x] Добавление pre-commit хуков
- [x] Подготовка модели детекции
- [ ] Подготовка бекэнда проекта
- [ ] Написание тестов
- [ ] Подготовка CI/CD

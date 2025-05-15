# Titanic Survival Prediction with CatBoost

Проект для предсказания выживания пассажиров Титаника с использованием CatBoost.

## Состав проекта

1. **Django Web Interface**  
   - Минималистичный веб-интерфейс (без полноценного фронтенда, только формы для ввода/выбора признаков)
   - Реализованы формы ввода данных и отображение результатов

2. **Prediction API**  
   - REST API для взаимодействия между веб-интерфейсом и ML-моделью
   - Принимает входные параметры, возвращает предсказание

3. **Dockerized Infrastructure**  
   - Каждый компонент развернут в отдельном контейнере Docker
   - Оркестрация через docker-compose

## Технологический стек

- ML: CatBoost
- Backend: Django + Django REST Framework
- Инфраструктура: Docker, docker-compose

## Запуск проекта

```bash
docker-compose up --build

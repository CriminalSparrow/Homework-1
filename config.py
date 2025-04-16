from pathlib import Path

# Базовый путь проекта (автоматически определяется)
PROJECT_ROOT = Path(__file__).parent.resolve()

# Пути к данным
DATA_PATH = PROJECT_ROOT / 'data'
RAW_DATA = DATA_PATH / 'data.csv'
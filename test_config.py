from config import PROJECT_ROOT, DATA_PATH, RAW_DATA
from pathlib import Path

def test_paths():
    print("\n[TEST DEBUG] Current working directory:", Path.cwd())
    print("[TEST DEBUG] PROJECT_ROOT:", PROJECT_ROOT)
    print("[TEST DEBUG] DATA_PATH contents:", list(DATA_PATH.glob('*')))
    print("[TEST DEBUG] RAW_DATA exists:", RAW_DATA.exists())

if __name__ == "__main__":
    test_paths()
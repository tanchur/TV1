import unittest
import sys
import os

# Добавляем текущую директорию в путь Python
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

if __name__ == '__main__':
    # Находим и запускаем все тесты
    loader = unittest.TestLoader()
    start_dir = 'tests'
    suite = loader.discover(start_dir)

    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
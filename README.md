# City Summary

## Установка
pip install -r requirements.txt

## Запуск
python main.py --city Moscow
python main.py --city Moscow --currency EUR

   ## Тесты
   pip install -r requirements.txt
   python -m pytest -v

   Тесты клиентов используют `unittest.mock` и не обращаются к сети.
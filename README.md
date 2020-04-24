## Консольный клиент для API Trello для базового функционала

Используемые библиотеки: requests, sys.

В auth_params указываются ключ и токен для доступа к API.  
В board_id указывается короткий id доски (например, M84PWQ9O).

При запуске файла из консоли без параметров выполняется функция read. 
При запуске файла из консоли с параметрами выполняются функции, указанные в параметрах. Остальные параметры при запуске файла принимаются как параметры для функций.

**Функция read**  
Выводит в консоль список колонок из доски и список задач в каждой колонке с коротким id для каждой задачи.  
Пример запуска: `python trello-api.py`  
      
**Функция create**  
Создает задачу с указанным именем в указанной колонке. В качестве параметров принимает имя задачи, имя колонки. Ничего не возвращает.  
Пример запуска: `python trello-api.py create "посмотреть" "Готово"`

**Функция createColumn**  
Создает колонку с указанным именем. В качестве параметра принимает имя колонки. Ничего не возвращает.  
Пример запуска: `python trello-api.py createColumn "Выполняется"`

**Функция move**  
Перемещает задачу в указанную колонку. В качестве параметра принимает короткий id задачи, имя колонки. Ничего не возвращает.  
Пример запуска: `python trello-api.py move 4 "Выполняется"`

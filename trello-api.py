import requests
import sys
  
# Данные авторизации в API Trello  
auth_params = {    
    'key': "",    
    'token': "", }  
  
# Адрес, на котором расположен API Trello 
base_url = "https://api.trello.com/1/{}"
board_id = ""

def read():      
    # Получим данные всех колонок на доске  
    column_data = requests.get(base_url.format('boards') + '/' + board_id + '/lists', params=auth_params).json()
    # Выведем название каждой колонки и всех заданий, которые к ней относятся:      
    for column in column_data:     
        task_data = requests.get(base_url.format('lists') + '/' + column['id'] + '/cards', params=auth_params).json()      
        print('\n=====' + column['name'] + '===== (количество задач: ' + str(len(task_data)) + ')')
        if not task_data:      
            print('\t' + 'Нет задач!')      
            continue      
        for task in task_data:      
            print('\t - ' + task['name'] + ' [idShort: ' + str(task['idShort']) + ']')  

def create(name, column_name):      
    # Получим данные всех колонок на доске      
    column_data = requests.get(base_url.format('boards') + '/' + board_id + '/lists', params=auth_params).json()      
    # Переберём данные обо всех колонках, пока не найдём ту колонку, которая нам нужна      
    for column in column_data:      
        if column['name'] == column_name:      
            # Создадим задачу с именем name в найденной колонке      
            requests.post(base_url.format('cards'), data={'name': name, 'idList': column['id'], **auth_params})
            break

def createColumn(name):
    # Получаем длинный id для нашей доски по короткому id
    responseget = requests.get(base_url.format('boards') + '/' + board_id, params=auth_params).json()
    # Создаем новую колонку (список) в нашей доске
    requests.post(base_url.format('lists'), data={'name': name, 'idBoard': responseget['id'], **auth_params})

def move(taskShortID, column_name):    
    # Получим данные всех колонок на доске    
    column_data = requests.get(base_url.format('boards') + '/' + board_id + '/lists', params=auth_params).json()
    # Среди всех колонок нужно найти задачу по короткому id и получить её длинный id    
    task_id = None    
    for column in column_data:    
        column_tasks = requests.get(base_url.format('lists') + '/' + column['id'] + '/cards', params=auth_params).json()   
        for task in column_tasks:
            if taskShortID == str(task['idShort']):    
                task_id = task['id']     
                break    
        if task_id:    
            break    
    # Теперь, когда у нас есть длинный id задачи, которую мы хотим переместить    
    # переберём данные обо всех колонках, пока не найдём ту, в которую мы будем перемещать задачу    
    for column in column_data:    
        if column['name'] == column_name:    
            # И выполним запрос к API для перемещения задачи в нужную колонку    
            requests.put(base_url.format('cards') + '/' + task_id + '/idList', data={'value': column['id'], **auth_params})    
            break  

if __name__ == "__main__":    
    if len(sys.argv) <= 2:    
        read()    
    elif sys.argv[1] == 'create':    
        create(sys.argv[2], sys.argv[3])    
    elif sys.argv[1] == 'move':    
        move(sys.argv[2], sys.argv[3])
    elif sys.argv[1] == 'createColumn':    
        createColumn(sys.argv[2])
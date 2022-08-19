documents = [
        {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
        {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
        {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}]

directories = {
        '1': ['2207 876234', '11-2', '5455 028765'],
        '2': ['10006'],
        '3': []
      }

shelf_list = list(directories.keys())


def people(number_input):
    for element in documents:
        if number_input == element['number']:
            return element['name']

# people("2207 876234")
# people("11-2")
# people("10006")
# people("10007")

def add_doc(type_input,number_input,name_input,shelf_input):
    # type_input = input('Введите тип нового документа: ')
    # number_input = input('Введите номер нового документа: ')
    # name_input = input('Введите имя и фамилию владельца нового документа: ')
    # shelf_input = input(f'Введите номер полки из списка {shelf_list}, для размещения документа {number_input}: ')

    if shelf_input in shelf_list:
        documents.append({'type':type_input, 'number':number_input, 'name':name_input})
        directories.setdefault(shelf_input,[]).append(number_input)
        result = 'success'
        return result
    else:
        result = 'shelf not found'
        return result

# add_doc('222','222','222','3')
# add_doc('222','222','222','4')


def delete(number_delete):
    # number_delete = input('Введите номер удаляемого документа: ')
    for document in documents:
        if number_delete in document.values():
            documents.remove(document)
            # result = 'success deleted from documents'
            # return result

            for key,value in directories.items():
                if number_delete in value:
                    value.remove(number_delete)
                    result = 'success deleted from documents and directories'
                    return result
        else:
            result = 'not found'
            return result

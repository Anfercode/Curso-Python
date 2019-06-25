'''Clientes'''

import sys
import csv

CLIENT_TABLE = '.\clients.csv'
CLIENT_SCHEMA = ['Name','Company','Email','Position']

clients = []
# ! incompleto de linea 10 - 24
def _initialize_clients_from_storage():
    with open(CLIENT_TABLE,m='r') as f:
        reader = csv.DictReader(f,fieldnames=[])

        for row in reader:
            clients.append(row)


def _save_clients_to_storage():
    tmp_table_name = f'{CLIENT_TABLE}.tmp'
    with open(tmp_table_name,mode='w') as f:
        writer = csv.DictWriter(f,fieldnames=CLIENT_SCHEMA)
        writer.writerow(clients)


def create_client(client):
    global clients

    if client not in clients:
        clients.append(client)
    else:
        print("Client already in client's list")


def list_clients():
    global clients

    for idx, client in enumerate(clients):
        print(f"{idx},{client['Name']},{client['Company']},{client['Email']},{client['Position']}")


def update_client(client_name):
    global clients

    for id, client in enumerate(clients):
        if client['Name'] == client_name:

            _print_options('U')
            command = input()
            command = command.upper()

            if command == 'N':
                client['Name'] = input('Insert the updated Name: ')
            elif command == 'C':
                client['Company'] = input('Insert the updated Company: ')
            elif command == 'E':
                client['Email'] = input('Insert the updated Company: ')
            elif command == 'P':
                client['Position'] = input('Insert the updated Company: ')
            elif command == 'A':
                clients[id] = _input_client_info()

            list_clients()
            return None

    print(f'The client {client_name} is not in our client\'s list')

def delete_client(client_name):
    global clients

    for id, client in enumerate(clients):
        if client_name == client['Name']:
            clients.pop(id)
            list_clients()
            return None

    print('client is not in clients list')


def search_client(client_name):
    global clients

    for client in clients:
        if client['Name'] != client_name:
            continue
        else:
            return True


def _input_client_info():
    client = {
            'Name' : _get_client_field('Name'),
            'Company' : _get_client_field('Company'),
            'Email' : _get_client_field('Email'),
            'Position' : _get_client_field('Position')
    }

    return client


def _get_client_field(field_name):
    field = None

    while not field:
        field = input(f'What is the client\'s {field_name}? : ')

    return field


def _get_client_name():
    client_name = None

    while not client_name:
        client_name = input('What is the client name: ')

        if client_name == 'exit':
            client_name = None
            break

    if not client_name:
        sys.exit()

    return client_name


def _print_options(option):

    option = option.upper()

    if option == 'W':
        print('\nWELCOME TO PLATZI VENTAS')
        print('*'*50)
        print('what do you do today?')
        print('[C]reate Client')
        print('[U]pdate Client')
        print('[D]elete Client')
        print('[S]earch Client')
        print('[E]xit')
    elif option == 'U':
        print('\nClient found!, what value do you want update?')
        print('*'*50)
        print('[N]ame')
        print('[C]ompany')
        print('[E]mail')
        print('[P]osition')
        print('[A]ll')
    else:
        print('Invalid Option')


if __name__ == '__main__':

    while True:

        _print_options('W')

        command = input()
        command = command.upper()

        if command == 'C':
            create_client(_input_client_info())
            list_clients()

        elif command == 'D':
            client_name = _get_client_name()
            delete_client(client_name)

        elif command == 'U':
            client_name = _get_client_name()
            update_client(client_name)

        elif command == 'S':
            client_name = _get_client_name()
            found = search_client(client_name)
            if found:
                print('The client is in the client\'s list')
            else:
                print(f'The client {client_name} is not in our client\'s list')
        elif command == 'E':
            print('Thanks for using us')
            break
        else:
            print('Invalid Command')
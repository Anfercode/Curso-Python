'''Clientes'''


import sys

clients = [
    {
        'Name' : 'Pablo',
        'Company' : 'google',
        'Email' : 'Pablo@google.com',
        'Position' : 'Software engineer',
    },
    {
        'Name' : 'Ricardo',
        'Company' : 'Facebook',
        'Email' : 'Ricardo@facebook.com',
        'Position' : 'Data engineer',
    },
]

def create_client(client):
    global clients

    if client not in clients:
        clients.append(client)
    else:
        print("Client already in client's list")


def list_clients():
    global clients

    for idx, client in enumerate(clients):
        print(f"{idx}:{client['Name']}")


def update_client(client_name,updated_client_name):
    global clients
    if client_name in clients:
        index = clients.index(client_name)
        clients[index] = updated_client_name
        list_clients()
    else:
        print('client is not in clients list')


def delete_client(client_name):
    global clients

    if client_name in clients:
        clients.remove(client_name)
        list_clients()
    else:
        print('client is not in clients list')


def search_client(client_name):
    global clients

    for client in clients:
        if client != client_name:
            continue
        else:
            return True


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


def _print_welcome():
    print('WELCOME TO PLATZI VENTAS')
    print('*'*50)
    print('what do you do today?')
    print('[C]reate Client')
    print('[U]pdate Client')
    print('[D]elete Client')
    print('[S]earch Client')

if __name__ == '__main__':
    _print_welcome()

    command = input()
    command = command.upper()

    if command == 'C':
        client = {
            'Name' : _get_client_field('Name'),
            'Company' : _get_client_field('Company'),
            'Email' : _get_client_field('Email'),
            'Position' : _get_client_field('Position')
        }
        create_client(client)
        list_clients()

    elif command == 'D':
        client_name = _get_client_name()
        delete_client(client_name)

    elif command == 'U':
        client_name = _get_client_name()
        updated_client_name = input('what is the updated client name: ')
        update_client(client_name , updated_client_name)

    elif command == 'S':
        client_name = _get_client_name()
        found = search_client(client_name)
        if found:
            print('The client is in the client\'s list')
        else:
            print(f'The client: {client_name} is not in our client\'s list')

    else:
        print('Invalid Command')
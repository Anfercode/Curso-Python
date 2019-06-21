

clients = 'tomas,juan,'

def create_client(client_name):
    global clients
    
    if client_name not in clients:
        clients += client_name
        _add_comma()
    else:
        print("Client already in client's list")

def list_clients():
    global clients

    print(clients)
    print(clients)

def update_client(client_name,updated_client_name):
    global clients
    if client_name in clients:
        clients = clients.replace(client_name + ',' ,updated_client_name +',')
        list_clients()
    else:
        print('client is not in client list')
    

def _add_comma():
    global clients

    clients += ','

def _get_client_name():
    return input('What is the client name: ')

def _print_welcome():
    print('WELCOME TO PLATZI VENTAS')
    print('*'*50)
    print('what do you do today?')
    print('[C]reate Client')
    print('[U]pdate Client')
    print('[D]elete Client')

if __name__ == '__main__':
    _print_welcome()
    
    command = input()
    command = command.upper()

    if command == 'C':
        client_name = _get_client_name()
        create_client(client_name)
        list_clients()
    elif command == 'D':
        pass
    elif command == 'U':
        client_name = _get_client_name()
        updated_client_name = input('what is the updated client name')
        update_client(client_name , updated_client_name)
    else:
        print('Invalid Command')
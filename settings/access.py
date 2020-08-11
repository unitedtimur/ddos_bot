import os

print('Database ', os.environ['DATABASE'])
print('USER ', os.environ['USER'])
print('PASS ', os.environ['PASSWORD'])
print('HOST ', os.environ['HOST'])
print('PORT ', os.environ['PORT'])
print('TOKEN ', os.environ['TOKEN'])
print('GROUP_ID ', os.environ['GROUP_ID'])

postgres = {
    'database': os.environ['DATABASE'],
    'user': os.environ['USER'],
    'password': os.environ['PASSWORD'],
    'host': os.environ['HOST'],
    'port': int(os.environ['PORT'])
}

vk = {
    'token': os.environ['TOKEN'],
    'group_id': str(os.environ['GROUP_ID'])
}

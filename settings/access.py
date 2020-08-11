import os

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

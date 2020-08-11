import os

postgres = {
    'database': os.environ['DATABASE'],
    'user': os.environ['USER'],
    'password': os.environ['PASSWORD'],
    'host': os.environ['HOST'],
    'port': os.environ['PORT']
}

vk = {
    'token': os.environ['TOKEN'],
    'group_id': os.environ['GROUP_ID']
}

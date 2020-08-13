import os

local = True

postgres = {}
vk = {}

if not local:
    postgres = {
        'database': os.environ['DATABASE'],
        'user': os.environ['USER'],
        'password': os.environ['PASSWORD'],
        'host': os.environ['HOST'],
        'port': int(os.environ['PORT_DB'])
    }

    vk = {
        'token': os.environ['TOKEN'],
        'group_id': str(os.environ['GROUP_ID'])
    }
else:
    postgres = {
        'database': 'dcfl9d56h5r0jk',
        'user': 'ozgwxzyzaqvntq',
        'password': '4db02f3675bc93522b42d749e1ecef04bb06b80d584549f70df54fa9f1487007',
        'host': 'ec2-46-137-79-235.eu-west-1.compute.amazonaws.com',
        'port': 5432
    }

    vk = {
        'token': 'd59d9c293e141282e9888280161eccec554ae2d5d2756e0a2cf046fb9998dc1f25bf654429c292734d03e',
        'group_id': '197296135'
    }

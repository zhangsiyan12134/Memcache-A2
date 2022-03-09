import os


class Config(object):
    INSTANCE_ID = 1  # the ID of backend app(1-8)
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    IMAGE_PATH = '/home/siyan/Documents/ECE1779/Assignment_2/Memcache/image_library'
    ALLOWED_FORMAT = {'jpg', 'jpeg', 'png', 'gif', 'tiff'}
    SCHEDULER_API_ENABLED = True
    SCHEDULER_TIMEZONE = "America/Toronto"
    JOB_INTERVAL = 5  # interval for memcache statistic data updates(in seconds)
    DB_CONFIG = {
        'user': 'siyan',
        'password': 'zhangsiyan123456',
        'host': 'localhost',
        'database': 'Assignment_1'
    }
    ASW_CONFIG = {
        'REGION': 'us-east-1',
        'AWS_ACCESS_KEY_ID': 'AKIA2NPVZMNR5BHCTGFV',
        'SECRET_ACCESS_KEY': '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'
    }





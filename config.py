import os


class Config(object):
    INSTANCE_ID = 1  # the ID of backend app(1-8)
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    IMAGE_PATH = '/home/siyan/Documents/ECE1779/Assignment_2/Memcache/image_library'
    ALLOWED_FORMAT = {'jpg', 'jpeg', 'png', 'gif', 'tiff'}
    SCHEDULER_API_ENABLED = True
    SCHEDULER_TIMEZONE = "America/Toronto"
    JOB_INTERVAL = 5  # interval for memcache statistic data updates(in seconds)
    RDS_CONFIG = {
        'host': 'ece1779.cxbccost2b0y.us-east-1.rds.amazonaws.com',
        'port': 3306,
        'user': '',
        'password': '',
        'database': 'ECE1779'
    }
    AWS_CONFIG = {
        'REGION': 'us-east-1',
        'AWS_ACCESS_KEY_ID': '',
        'SECRET_ACCESS_KEY': ''
    }





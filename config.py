import os


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    IMAGE_PATH = '/home/siyan/Documents/ECE1779/Assignment_1/Assignments_Git/BackendApp/Lab1/image_library'
    ALLOWED_FORMAT = {'jpg', 'jpeg', 'png', 'gif', 'tiff'}
    SCHEDULER_API_ENABLED = True
    SCHEDULER_TIMEZONE = "America/Toronto"
    JOB_INTERVAL = 5  # interval for memcache statistic data updates(in seconds)
    DB_CONFIG = {
        'user': 'root',
        'password': 'ece1779pass',
        'host': 'localhost',
        'database': 'Assignment_1'
    }
    ASW_CREDENTIAL = {
        'AWS_REGION': 'us-east-1',
        'AWS_ACCESS_KEY_ID': 'AKIA2NPVZMNR5BHCTGFV',
        'AWS_SECRET_ACCESS_KEY': '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'
    }




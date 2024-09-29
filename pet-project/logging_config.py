from logging.config import dictConfig


def configure_logging():
    dictConfig(
        {
            'version': 1,
            'disable_existing_loggers': False,
            'formatters': {
                'console': {
                    'class': 'logging.Formatter',
                    'datefmt': '%Y-%m-%d %H:%M:%S',
                    'format': '%(name)s: %(lineno)s - %(message)s'
                },
                'file': {
                    'class': 'logging.Formatter',
                    'datefmt': '%Y-%m-%d %H:%M:%S',
                    'format': '%(name)s: %(lineno)s - %(message)s'
                }
            },
            'handlers': {
                'default': {
                    'class': 'rich.logging.RichHandler',
                    'level': 'DEBUG',
                    'formatter': 'console',
                },
                'rotating_file': {
                    'class': 'logging.handlers.RotatingFileHandler',
                    'level': 'DEBUG',
                    'formatter': 'file',
                    'filename': 'pet_project.log',
                    'maxBytes': 1024 * 1024,
                    'backupCount': 2,
                    'encoding': 'utf-8',
                }
            },
            'loggers': {
                'uvicorn': {
                    'handlers': ['default', 'rotating_file'],
                    'level': 'INFO',
                },
                'main': {
                    'handlers': ['default', 'rotating_file'],
                    'level': 'INFO',
                    'propagate': False,

                }
            }
        }
    )
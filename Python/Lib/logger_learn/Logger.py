import logging
import logging.config

LOGGING = {
    'version':  1,
    'formatters': {
        'brief': {
            'format': '{message!s}',
            'style': '{'
        },
        'default': {
            'format': '{asctime!s} {levelname!s:8} {name!s:15} {message!s}',
            'datefmt': '%Y/%m/%d %H:%M:%S'
        },
        # 'custom': {
        #     'class': 'CustomAdapter',
        #     'moduleName': __name__,
        #     'yaa': 'test'
        # }
    },
    # 'filters': {
    #     'special': {
    #         'class': 'SpecialFilter',
    #     }
    # },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'level': 'DEBUG',
            'formatter': 'brief'
        }
    },
    'loggers': {
        'root.this': {
            'handlers': ['console'],
            'level': 'INFO',
            # 'filters': ['special'],
        }
    }}


class CustomAdapter(logging.LoggerAdapter):
    def process(self, msg, kwargs):
        return f'[{self.extra["moduleName"]}][{self.extra["yaa"]}] {msg}', kwargs


if __name__ == '__main__':
    # logger = logging.getLogger()
    # logging.basicConfig(level=logging.DEBUG)
    # adapter = CustomAdapter(logger, {'moduleName': __name__, 'yaa': 'test'})

    # adapter.info('this')
    logging.config.dictConfig(LOGGING)
    logger = CustomAdapter(logging.getLogger('root.this'), {
                           'moduleName': 'test', 'yaa': 'test'})
    logger.info('test')

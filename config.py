import multiprocessing

workers = multiprocessing.cpu_count() * 2 + 1
bind = 'unix:apiagro.sock'
umask = 0o007
reload = True

#logging
accesslog = 'logs/access.log'
errorlog = 'logs/err.log'
import multiprocessing

workers = multiprocessing.cpu_count() * 2 + 1
bind = 'unix:apiagro.sock'
#bind = '0.0.0.0:5000'
umask = 0o007
reload = True

#logging
accesslog = 'logs/access.log'
errorlog = 'logs/err.log'

# certificate = 'ssl/cer.crt'
# keyfile = 'ssl/cer.key'
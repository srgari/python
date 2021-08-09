def starwars():
    import time
    lala = dict(
        header = '\033[95m',
        okblue = '\033[94m',
        okcyan = '\033[96m',
        okgreen = '\033[92m',
        warning = '\033[93m',
        fail = '\033[91m',
        endc = '\033[0m',
        bold = '\033[1m',
        underline = '\033[4m',
        )

    while True:
        for x in lala.values():
            print(f'\r {x} May the force be with you!', end = '', flush = True)
            time.sleep(1)

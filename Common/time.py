from datetime import datetime

def time_ct():
    current_time = datetime.now().strftime('%m-%d-%H-%M-%S')
    return current_time

import snowboydecoder
import signal

interrupted = False
sensitivity = 0.5
model = 'KAIVA.pmdl'

def signal_handler(signal, frame):
    global interrupted
    interrupted = True

def interrupt_callback():
    global interrupted
    return interrupted

def start(callback_function):
    # capture SIGINT signal, e.g., Ctrl+C
    signal.signal(signal.SIGINT, signal_handler)

    detector = snowboydecoder.HotwordDetector(model, sensitivity=sensitivity)
    print('Standby...')

    # main loop
    detector.start(detected_callback=callback_function,
                   interrupt_check=interrupt_callback,
                   sleep_time=0.03)

    detector.terminate()

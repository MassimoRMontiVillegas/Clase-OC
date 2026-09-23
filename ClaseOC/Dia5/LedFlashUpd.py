import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
LED_PIN1 = 17
GPIO.setup(LED_PIN1, GPIO.OUT)
LED_PIN2 = 18
GPIO.setup(LED_PIN2, GPIO.OUT)
LED_PIN5 = 22
GPIO.setup(LED_PIN5, GPIO.OUT)
LED_PIN4 = 23
GPIO.setup(LED_PIN4, GPIO.OUT)
LED_PIN6 = 24
GPIO.setup(LED_PIN6, GPIO.OUT)
LED_PIN3 = 27
GPIO.setup(LED_PIN3, GPIO.OUT)


    try:
        print("Semáforo Activo (Presiona Ctrl+C para salir)")
        while True:
            GPIO.output(LED_PIN1, True)
            GPIO.output(LED_PIN2, False)
            GPIO.output(LED_PIN3, False)
            GPIO.output(LED_PIN4, False)
            GPIO.output(LED_PIN5, False)
            GPIO.output(LED_PIN6, True)
            time.sleep(1)
            GPIO.output(LED_PIN1, True)
            GPIO.output(LED_PIN2, False)
            GPIO.output(LED_PIN3, False)
            GPIO.output(LED_PIN4, True)
            GPIO.output(LED_PIN5, False)
            GPIO.output(LED_PIN6, False)
            time.sleep(1)
            GPIO.output(LED_PIN1, True)
            GPIO.output(LED_PIN2, True)
            GPIO.output(LED_PIN3, True)
            GPIO.output(LED_PIN4, False)
            GPIO.output(LED_PIN5, False)
            GPIO.output(LED_PIN6, False)
            time.sleep(1)
            GPIO.output(LED_PIN1, False)
            GPIO.output(LED_PIN2, True)
            GPIO.output(LED_PIN3, False)
            GPIO.output(LED_PIN4, False)
            GPIO.output(LED_PIN5, True)
            GPIO.output(LED_PIN6, False)
            time.sleep(1)
            GPIO.output(LED_PIN1, False)
            GPIO.output(LED_PIN2, True)
            GPIO.output(LED_PIN3, True)
            GPIO.output(LED_PIN4, False)
            GPIO.output(LED_PIN5, False)
            GPIO.output(LED_PIN6, False)
            time.sleep(1)
            GPIO.output(LED_PIN1, True)
            GPIO.output(LED_PIN2, True)
            GPIO.output(LED_PIN3, False)
            GPIO.output(LED_PIN4, True)
            GPIO.output(LED_PIN5, False)
            GPIO.output(LED_PIN6, False)
            time.sleep(1)
    except KeyboardInterrupt:
        print("Desactivando Semáforo...")
        time.sleep(0.5)
        print("Semáforo Desactivado.")
    finally:
        GPIO.cleanup()

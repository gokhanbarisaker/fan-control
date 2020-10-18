from gpiozero import CPUTemperature, PWMLED
from time import sleep
import sys
import traceback


def cool(pwm, target):
    while cpu.temperature > target:
        pwm.value = 1.0
        sleep(2)


def run(cpu, pwm):
    while True:
        temp = cpu.temperature

        if temp > 50:
            cool(pwm, 40)
        else:
            pwm.value = 0.0

        sleep(2)


if __name__ == '__main__':     # Program entrance
    print('Starting fan control...')
    cpu = CPUTemperature()
    pwm = PWMLED(17)

    try:
        run(cpu, pwm)
    except KeyboardInterrupt:
        pwm.value = 0.0
    except Exception:
        traceback.print_exc(file=sys.stdout)

    sys.exit(0)


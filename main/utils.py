import subprocess
from gpiozero import CPUTemperature


def get_gpiozero_temperature():
    cpu = CPUTemperature()
    return cpu.temperature


def get_system_temperature():
    process = subprocess.Popen(['/opt/vc/bin/vcgencmd', 'measure_temp'],
                               stdout=subprocess.PIPE,
                               stderr=subprocess.PIPE,
                               universal_newlines=True)
    stdout, stderr = process.communicate()
    return stdout

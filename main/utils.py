import subprocess


def get_system_temperature():
    process = subprocess.Popen(['/opt/vc/bin/vcgencmd', 'measure_temp'],
                               stdout=subprocess.PIPE,
                               stderr=subprocess.PIPE)
    stdout, stderr = process.communicate()
    return stdout

# fan-control
Ice tower fan control service for the raspberry pi os.

## Dependencies

- Python 3
- https://gpiozero.readthedocs.io/en/stable/

## Installation

1. Copy the service file to the `/etc/systemd/system` folder
```sh
sudo cp fan-control.service /etc/systemd/system/fan-control.service
```

2. Copy the python file to the `/usr/local/sbin` folder
```sh
sudo cp fan-control.py /usr/local/sbin/fan-control.py
```

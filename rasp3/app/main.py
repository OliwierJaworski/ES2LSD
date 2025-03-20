import serial
import socket
import json
import re

server_ip = '192.168.1.77'  
server_port = 50000        

# Accumulator for sensor data
sensor_data = {}

def read_serial_and_send():

    ser = serial.Serial('/dev/ttyUSB0', 115200)
    while True:
        if ser.in_waiting > 0:
            line = ser.readline().decode('utf-8').strip()
            print('Received data from COM port:', line)

            process_sensor_data(line)

            if all(key in sensor_data for key in ['temperature', 'humidity', 'pressure', 'Radiation', 'Watermark 1', 'Watermark 2', 'Watermark 3']):
                send_data_to_server(sensor_data)
                reset_sensor_data()

def process_sensor_data(line):
    global sensor_data 

    try:
        if 'Internal Temperature' in line:
            temp_str = line.split('Internal Temperature: ')[1].split(' ')[0]
            if temp_str:
                sensor_data['temperature'] = float(temp_str)

        if 'Humidity' in line:
            humidity_str = line.split('Humidity: ')[1].split(' ')[0]
            if humidity_str:
                sensor_data['humidity'] = float(humidity_str)

        if 'Pressure' in line:
            pressure_str = line.split('Pressure: ')[1].split(' ')[0]
            if pressure_str:
                sensor_data['pressure'] = float(pressure_str)

        if 'Radiation' in line:
            radiation_match = re.search(r'(\d+\.\d+)', line)
            if radiation_match:
                sensor_data['Radiation'] = float(radiation_match.group(1))

        if 'PT100' in line:
            pt100_str = line.split('PT100: ')[1].split(' ')[0]
            if pt100_str:
                sensor_data['temperature'] = float(pt100_str)

        if 'Watermark 1' in line:
            watermark1_str = line.split('Watermark 1 - Frequency: ')[1].split(' ')[0]
            if watermark1_str:
                sensor_data['Watermark 1'] = float(watermark1_str)

        if 'Watermark 2' in line:
            watermark2_str = line.split('Watermark 2 - Frequency: ')[1].split(' ')[0]
            if watermark2_str:
                sensor_data['Watermark 2'] = float(watermark2_str)

        if 'Watermark 3' in line:
            watermark3_str = line.split('Watermark 3 - Frequency: ')[1].split(' ')[0]
            if watermark3_str:
                sensor_data['Watermark 3'] = float(watermark3_str)

    except Exception as e:
        print(f"Error processing data: {e}")

def send_data_to_server(data):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        message = json.dumps(data)
        sock.sendto(message.encode('utf-8'), (server_ip, server_port))
        print(f"Data sent to {server_ip}:{server_port} via UDP.")
    except Exception as e:
        print(f"Error sending data: {e}")
    finally:
        sock.close()

def reset_sensor_data():
    global sensor_data
    sensor_data = {}

if __name__ == '__main__':
    read_serial_and_send()


#!/usr/bin/env python3

from bottle import route, run
import subprocess, os, json, sys, re, psycopg2, string, shutil, glob, time

os.system('modprobe w1-gpio')
os.system('modprobe w1-therm')

base_dir = '/sys/bus/w1/devices/'
device_folder = glob.glob(base_dir + '28*')[0]
device_file = device_folder + '/w1_slave'

t_old = 999;

print(device_file);

def read_temp_raw():
    f = open(device_file, 'r')
    lines = f.readlines()
    f.close()
    return lines

def read_temp():
    lines = read_temp_raw()
    while lines[0].strip()[-3:] != 'YES':
        time.sleep(0.2)
        lines = read_temp_raw()
    equals_pos = lines[1].find('t=')
    if equals_pos != -1:
        temp_string = lines[1][equals_pos+2:]
        temp_c = float(temp_string) / 1000.0
        temp_f = temp_c * 9.0 / 5.0 + 32.0
        return temp_c

@route('/temp')
def red_temp():
    global t_old
    tC = read_temp()
    if (tC != t_old):
        print(tC)
    t_old = tC
    return {'temp':str(tC)}

@route('/')
def hello():
    return "ds18b20-ws\n"
    
if __name__ == "__main__":
    try:
        run(host="0.0.0.0", port=18020,
            debug=True, quiet=False)
    except Exception as e:
        print(e)


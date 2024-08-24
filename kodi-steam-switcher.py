import configparser
import os
import psutil
from flask import Flask, request
import subprocess
import signal

# Load configuration
config = configparser.ConfigParser()
config.read('config.ini')

kodi_path = config['Paths']['kodi_path']
steam_path = config['Paths']['steam_path']
last_launched = config['AppState']['last_launched']

app = Flask(__name__)

def kill_process_by_name(name):
    for proc in psutil.process_iter(['pid', 'name']):
        if proc.info['name'].lower() == name.lower():
            os.kill(proc.info['pid'], signal.SIGTERM)

def start_application(path):
    subprocess.Popen([path])

def update_last_launched(app_name):
    config['AppState']['last_launched'] = app_name
    with open('config.ini', 'w') as configfile:
        config.write(configfile)

@app.route('/kodi', methods=['GET'])
def launch_kodi():
    kill_process_by_name('Steam.exe')
    start_application(kodi_path)
    update_last_launched('kodi')
    return 'Kodi launched'

@app.route('/steam', methods=['GET'])
def launch_steam():
    kill_process_by_name('kodi.exe')
    start_application(steam_path)
    update_last_launched('steam')
    return 'Steam launched'

@app.route('/restart', methods=['GET'])
def restart_pc():
    # Command to restart the PC
    subprocess.Popen(["shutdown", "/r", "/t", "0"])
    return 'Restarting the PC'

if __name__ == '__main__':
    # Start Kodi if last_launched is None
    if last_launched == 'None' or not last_launched:
        start_application(kodi_path)
        update_last_launched('kodi')
    elif last_launched == 'kodi':
        start_application(kodi_path)
    elif last_launched == 'steam':
        start_application(steam_path)

    app.run(host='0.0.0.0', port=8888)
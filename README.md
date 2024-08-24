# kodi-steam-switcher
Simple Python script enabling quick switching between Kodi and Steam for Windows HTPCs

# Install
Copy the contents into the directory of your choice

Create a shortcut to `run.bat` in your Windows "Startup" start menu folder

# Usage
## Kill Kodi and start Steam
Make sure you set Steam to launch as Big Picture mode

`curl http://computer_ip:8888/steam`

## Kill Steam and launch Kodi
`curl http://computer_ip:8888/kodi`

## Restart PC
`curl http://computer_ip:8888/restart`

# HomeAssistant integration
If you want to automate using HomeAssistant (voice command, buttons), add this to your `configuration.yaml` file

```
rest_command:
  start_steam:
    url: "http://computer_ip:8888/steam"
  start_kodi:
    url: "http://computer_ip:8888/kodi"
  restart_pc:
    url: "http://computer_ip:8888/restart"
```

# Notes
* Make sure your firewall allows traffic for this server (port 8888)
* Launching Kodi (for instance) when Kodi is already running won't trigger anything, no risks of being interrupted during a movie by mistake
* The script remembers the last used app in `config.ini`

# Immersion tips
Random suggestions to make your Windows HTPC feel less like Windows

* You can set the `run.bat` shortcut properties to start "Minimized" to keep a clean screen after the PC has booted and between switched
* Disable Windows sounds
* Disable Desktop Icons and set a nice background
* Set a nice Lock Screen background
* Hide the Taskbar
* Disable Mouse Input in Kodi System settings to avoid having a cursor pop up for a few seconds at startup
* Disable your Windows user password
* Some motherboards can boot as soon as power is detected, this is useful if you want to turn the PC on through a connected power socket without much tinkering. You can enable this in your BIOS/UEFI settings (check your motherboard user manual for more details)

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

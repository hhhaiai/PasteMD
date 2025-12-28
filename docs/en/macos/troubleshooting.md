## Troubleshooting

::: warning Important
Before troubleshooting, make sure all permissions are granted and the app has been restarted to apply permission changes.

The macOS version has only been tested on macOS 26. Other versions may have unknown issues.

macOS support is still limited. Thanks for your patience.

If you have questions, join QQ group 1073549447 or open an issue.
:::

### Hotkey not responding

1. **Check Accessibility permission**: System Settings -> Privacy & Security -> Accessibility
2. **Check hotkey enabled**: menu bar -> "Enable Hotkey" (should be checked)
3. **Try a different hotkey**: avoid conflicts with system shortcuts
4. **Restart the app**: quit and relaunch

### App detection fails

1. **Check Screen Recording permission**: System Settings -> Privacy & Security -> Screen Recording
2. **Refresh permission status**: Settings -> Permissions -> "Refresh"
3. **Check logs**: menu bar -> "View Logs"

### Word insert / Excel write fails

1. **Check Automation permission**: System Settings -> Privacy & Security -> Automation -> PasteMD
2. **Re-authorize**: restart PasteMD and ensure permission is granted
3. **Make sure Office is open**: Word/Excel must be the foreground app

### WPS paste fails

1. **Check Input Monitoring permission**: System Settings -> Privacy & Security -> Input Monitoring
2. **Re-authorize**: restart PasteMD and ensure permission is granted
3. **Confirm WPS is foreground**: WPS must be the active window

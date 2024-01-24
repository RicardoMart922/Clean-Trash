import subprocess

def recycle_bin_cleanup():
    powershell_command = 'echo Y | PowerShell.exe -NoProfile -Command Clear-RecycleBin'

    try:
        subprocess.run(powershell_command, shell=True, check=True)
        print("Recycle bin cleaned successfully using PowerShell!")
    except subprocess.CalledProcessError as e:
        print(f"Error while cleaning the recycle bin: {e}")

if __name__ == "__main__":
    recycle_bin_cleanup()

import os
import subprocess

# Function to execute adb commands and return the output
def adb_command(command):
    result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    return result.stdout.decode('utf-8'), result.stderr.decode('utf-8')

# Function to check if a device is connected
def check_device():
    output, error = adb_command("adb devices")
    if error:
        print(f"Error: {error}")
        return False
    if "device" in output:
        print("Device connected.")
        return True
    else:
        print("No device connected.")
        return False

# Function to list directories/files on the device
def list_device_files(path):
    output, error = adb_command(f"adb shell ls {path}")
    if error:
        print(f"Error: {error}")
        return []
    return output.split()

# Function to pull files from the device
def pull_files(source, destination):
    command = f"adb pull {source} {destination}"
    output, error = adb_command(command)
    if error:
        print(f"Error: {error}")
    else:
        print(f"Successfully backed up {source} to {destination}")

# Main function
def main():
    if not check_device():
        return

    # Directories/files to back up
    paths_to_backup = [
        "/sdcard/DCIM",
        "/sdcard/Pictures",
        "/sdcard/Documents"
    ]

    backup_location = "backup"
    if not os.path.exists(backup_location):
        os.makedirs(backup_location)

    for path in paths_to_backup:
        files = list_device_files(path)
        if files:
            for file in files:
                full_path = os.path.join(path, file)
                print(f"Backing up {full_path}...")
                pull_files(full_path, backup_location)

if __name__ == "__main__":
    main()

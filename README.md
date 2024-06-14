Python script that can back up data from an Android device. This script will use the Android Debug Bridge (ADB) tool to interact with the Android device.

Requirements:

  ADB Installed: Ensure you have ADB installed and added to your system's PATH.
  USB Debugging Enabled: Enable USB debugging on your Android device.
  Python Installed: Ensure you have Python installed on your system.

Script Overview:
   The script will:
     Connect to the Android device using ADB.
     List the directories/files you want to back up.
     Pull the specified directories/files to your local machine.

Instructions:

    Install ADB: If ADB is not installed, download and install it from here.
    
    Enable USB Debugging: On your Android device, enable USB debugging from the Developer Options.
    
    Run the Script:
        Connect your Android device to your computer via USB.
        Ensure your computer recognizes the device (you may need to accept a prompt on your Android device to allow USB debugging).
        Run the script using python backup_android.py.

Explanation:

   adb_command: Executes ADB commands and returns the output.
    
   check_device: Checks if an Android device is connected.
    
   list_device_files: Lists files in a specified directory on the device.
    
   pull_files: Pulls (copies) files from the Android device to the local machine.
    
   main: The main function orchestrates the backup process by specifying which directories to back up and where to save them on the local machine.

Note:

  Modify paths_to_backup to include other directories or files you wish to back up.
  Ensure ADB has the necessary permissions to access the files on your Android device.

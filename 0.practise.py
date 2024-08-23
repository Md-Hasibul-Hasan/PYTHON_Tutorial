# import os,shutil

# # print(os.getcwd())
# # print(os.path.exists("os.py"))

# # if os.path.exists("mov1"):
# #     print("already exists")
# # else:
# #     os.makedirs("mov1/mov2")


# # os.remove("myfile.txt")
# # f=open("myfile3.txt","a")
# # print(f.closed())

# # os.makedirs("mov")
# # os.remove(r"E:\PYTHON Projects\Python_Tutorial\myfile.txt")
# # # os.rmdir("mov")
# # os.open("e:")
# # help(list)

# shutil.rmtree("mov")


# # INSTALL ESPTOOL PYTHON SCRIPT

# pip install esptool

# # FLASH

# esptool.py --chip esp32 --port COM3 --baud 115200 --before default_reset --after hard_reset write_flash -z --flash_mode dio --flash_freq 40m --flash_size detect 0x1000 bootloader.bin 0x10000 NodeMCU.bin 0x8000 partitions_singleapp.bin


import time

def display_remaining_time(time_in_millis):
    hours = time_in_millis // 3600000
    minutes = (time_in_millis % 3600000) // 60000
    seconds = (time_in_millis % 60000) // 1000

    # Clear the previous text area (Simulation, since there's no display like tft in Python)
    print("\033c", end="")  # Clear console

    # Display formatted time
    print(f"TIME: {hours:02}:{minutes:02}:{seconds:02}")

def motor_working():
    motor_off_minute = .2  # Example value, set appropriately
    motor_running_second = 5  # Example value, set appropriately
    motor_forward = True  # Example initial state

    motor_off = motor_off_minute * 60 * 1000
    motor_running = motor_running_second * 1000

    motor_start_time = time.time() * 1000  # Current time in milliseconds

    while True:

        current_time = time.time() * 1000  # Update current time in milliseconds
        remaining_time_millis = 0

        if current_time - motor_start_time <= motor_off:
            # Motor OFF
            print("MOTOR: OFF")
            remaining_time_millis = motor_off - (current_time - motor_start_time)
            remaining_time_millis=int(remaining_time_millis)
            print(f" remain time {remaining_time_millis}")

        elif current_time - motor_start_time > motor_off and current_time - motor_start_time <= (motor_off + motor_running):
            # Motor ON
            if motor_forward:
                print("MOTOR: Run F")
            else:
                print("MOTOR: Run B")
            remaining_time_millis = (motor_off + motor_running) - (current_time - motor_start_time)
            remaining_time_millis=int(remaining_time_millis)
            print(f" remain time {remaining_time_millis}")

        else:
            # Reset motor state and timer
            motor_start_time = time.time() * 1000
            motor_forward = not motor_forward
            remaining_time_millis = 0
            print("MOTOR: OFF")

        # Display remaining time
        display_remaining_time(remaining_time_millis)

        # Sleep for a while to simulate delay (e.g., 1 second)
        # time.sleep(.500)

# Example call to motor_working()
motor_working()

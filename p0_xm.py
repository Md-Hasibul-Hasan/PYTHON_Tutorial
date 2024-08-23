# from datetime import datetime
# t=datetime.now()
# m=datetime(2024,4,20)
# print(m-t)



# from datetime import datetime

# current_time = datetime.now()
# future_date = datetime(2024, 4, 20)

# time_difference = future_date - current_time

# # Convert timedelta to string and remove milliseconds
# time_difference_str = str(time_difference).split('.')[0]

# print("Time remaining until April 20, 2024:", time_difference_str)




# from datetime import datetime

# current_time = datetime.now()
# future_date = datetime(2024, 4, 20)

# time_difference = future_date - current_time

# # Extract days, hours, minutes, and seconds from timedelta
# days = time_difference.days
# hours, remainder = divmod(time_difference.seconds, 3600)
# minutes, seconds = divmod(remainder, 60)

# # Construct a string representation
# time_difference_str = f"{days} days {hours} hours {minutes} minutes {seconds} seconds"

# print( time_difference_str)






# from datetime import datetime
# import time

# while True:
#     current_time = datetime.now()
#     future_date = datetime(2024, 4, 20)

#     time_difference = future_date - current_time

#     # Extract days, hours, minutes, and seconds from timedelta
#     days = time_difference.days
#     hours, remainder = divmod(time_difference.seconds, 3600)
#     minutes, seconds = divmod(remainder, 60)

#     # Construct a string representation
#     time_difference_str = f"{days} days {hours} hours {minutes} minutes" # {seconds} seconds

#     print(time_difference_str)

#     time.sleep(60)  # Wait for 5 seconds before updating again







from datetime import datetime, timedelta
import time

future_date = datetime(2024,7,23,0,0,0,0)
next_update =time.time()

date=datetime.now()
print(date)
print(future_date)
print(future_date-date)

# while True:
#     current_time = time.time()
    
#     if current_time >= next_update:
#         time_difference = future_date - datetime.now()

#         # Extract days, hours, minutes, and seconds from timedelta
#         days = time_difference.days
#         hours, remainder = divmod(time_difference.seconds, 3600)
#         minutes, seconds = divmod(remainder, 60)

#         # Construct a string representation
#         time_difference_str = f"{days} days {hours} hours {minutes} minutes {seconds} seconds"

#         print(time_difference_str)

#         # Set the next update time to one minute from now
#         next_update += 60
    
#     # Check for updates every 100 milliseconds
#     time.sleep(0.1)



# from datetime import datetime, timedelta
# import time

# future_date = datetime(2024, 7, 23)
# next_update = time.time()


# while True:
#     current_time = time.time()
    
#     if current_time >= next_update:
#         time_difference = future_date - datetime.now()

#         # Extract days, hours, minutes, and seconds from timedelta
#         days = time_difference.days
#         hours, remainder = divmod(time_difference.seconds, 3600)
#         minutes, seconds = divmod(remainder, 60)

#         # Construct a string representation
#         time_difference_str = f"{days} days {hours} hours {minutes} minutes {seconds} seconds"

#         print(time_difference_str)

#         # Set the next update time to one minute from now
#         next_update += 60
    
#     # Check for updates every 100 milliseconds
#     time.sleep(0.1)








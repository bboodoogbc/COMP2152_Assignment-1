# Author: Billy Boodoo
# Assignment: #1



# STEP b: Create 4 variables.
# ---------------------------

# string
gym_member = "Alex Alliton"

# float
preferred_weight_kg = 20.5

# int
highest_reps = 25

# boolean
membership_active = True



# STEP c: Create a dictionary named workout_stats.
# ------------------------------------------------

# This dictionary uses names as keys and stores three workout times in minutes as a tuple of integers
workout_stats = {
    "Alex": (15, 20, 25),
    "Jamie": (15, 15, 90),
    "Taylor": (45, 55, 10)
}

temp_dict = {}



# STEP d: Calculate total workout minutes using a loop and add to dictionary.
# ---------------------------------------------------------------------------

# Loops through each key in the dictionary. Each key has a tuple of workout times
# Stores the value of each tuple in workout_data variable
for name, workout_data in workout_stats.items():

    # Unpack the tuple into three variables
    yoga, running, weightlifting = workout_data

    # Creates new key with name and stores in new_key
    new_key = name + "_total_time"

    total_workout = yoga + running + weightlifting

    temp_dict[new_key] = total_workout

# Adds the temp_dict with new keys and values to workout_stats dictionary.
workout_stats.update(temp_dict)



# STEP e: Create a 2D nested list called workout_list.
# ----------------------------------------------------

# This list will be a list of different list
workout_list = []

# Loops through dictionary workout_stats
for name, workout_data in workout_stats.items():

    # Checks dictionary item data type for tuples
    if isinstance(workout_data, tuple):

        # Coverts tuple to list
        temp_list = list(workout_data)

        # Adds temp_list to main workout_list to make a nested list
        workout_list.append(temp_list)



# STEP f: Slice the workout_list.
# --------------------------------

# Loops though the list row by row
for row in workout_list:
    
    # Slices and prints only the 1st and 2nd column of the row
    print(f"Yoga & Running Minutes: {row[0:2]}")

# Loops through list starting at 2 to last row to the end
for row in workout_list[-2:]:

    # Prints the last column for each row in the loop.
    print(f"Weightlifting: {row[-1]}")



# STEP g: Check if any friend total >= 120 minutes.
# -------------------------------------------------

# Loops through dictionary workout_stats
for name, total_time in workout_stats.items():
    
    # Checks only the total workout time using data type int
    if isinstance(total_time, int) and total_time >= 120:

        # Removes exrta text from key to retrive name only
        splice_name = name.replace("_total_time", "")
        print(f"Great job staying active, {splice_name}!")



# STEP h: Accept user input and search for friend.
# -------------------------------------------------

# Accepts user input.
user_input = input("Please enter name you would like to search for: ")

# Converts to lowercase to easier comparasion 
lc_user_input = user_input.lower()

# Variable to check if name is found to trigger not found message
found = False

# Loop through dictionary and checks key or name for a match
for name in workout_stats:

    # Converts to lowercase to easier comparasion 
    lc_name = name.lower()

    # If name is found prints all the info of that key or name in the dictionary+
    if lc_user_input == lc_name:
        print(f"Name: {name}")
        print(f"Yoga: {workout_stats[name][0]}")
        print(f"Running: {workout_stats[name][1]}")
        print(f"Weightlifting: {workout_stats[name][2]}")
        found = True
        break

if found == False:
    print(f"Friend {user_input} not found in the records.")



# STEP i: Find the friend with highest and lowest total workout time.
# -------------------------------------------------------------------

# To find the highest min worked out
highest_total = 0
highest_friend = ""

# To find the lowest min worked out
lowest_total = float('inf')
lowest_friend = ""

# Loops through dictionary workout_stats
for name, total_time in workout_stats.items():
    
    # Checks only the total workout time using data type int
    if isinstance(total_time, int):

        # If total_time is greater than highest_total update highest_total and highest_friend
        if total_time > highest_total:
            highest_total = total_time
            highest_friend = name

        # If total_time is less than lowest_total update lowest_total and lowest_friend
        if total_time < lowest_total:
            lowest_total = total_time
            lowest_friend = name

print(f"Friend with highest workout time: {highest_friend} with {highest_total} minutes.")
print(f"Friend with lowest workout time: {lowest_friend} with {lowest_total} minutes.")
import sys
from tabulate import tabulate

def read_driver_info(file_path):
    with open (file_path,"r") as f:
        data=f.readlines()
    return data

def read_the_location(data):
    location_of_race=data[0]
    return location_of_race

def read_driver_code_name(data):

    lap_times = {}
    for line in data[1:]:  # Skip the first line
        driver_code = line[:3]  # Extract the driver code
        lap_time = float(line[3:])  # Extract the lap time and convert to float

        if driver_code in lap_times:
            if isinstance(lap_times[driver_code], list):
                lap_times[driver_code].append(lap_time)
            else:
                lap_times[driver_code] = [lap_times[driver_code], lap_time]
        else:
            lap_times[driver_code] = lap_time

    return lap_times


def get_driver_info():
    driver_info = {}

    with open("f1_drivers.txt", "r") as file:
        for line in file:
            parts = line.strip().split(",")
            driver_code = parts[1]  # Extract the driver code
            driver_name = parts[2]  # Extract the driver name
            team_name = parts[3]  # Extract the team name

            # Add driver data to the dictionary
            driver_info[driver_code] = {
                "name": driver_name,
                "team": team_name
            }

    return driver_info

def display_fastest_lap_times(lap_times, driver_info):
    # Calculate the fastest lap time for each driver
    fastest_times = {driver: min(times) for driver, times in lap_times.items()}

    # Sort the drivers by their fastest lap time in ascending order
    sorted_fastest_times = sorted(fastest_times.items(), key=lambda x: x[1])

    # Create a table for the result
    table = []
    for driver, fastest_time in sorted_fastest_times:
        driver_name = driver_info[driver]['name']
        team_name = driver_info[driver]['team']
        table.append([driver, driver_name, team_name, fastest_time])

    # Display the results in a table format
    print(tabulate(table, headers=["Driver Code", "Driver Name", "Team", "Fastest Lap Time"], tablefmt="grid"))



def main():
    if len(sys.argv) != 2:
        print("Usage : Python main.py < lap_times_1.txt >")
    file_path= sys.argv[1] # terminal bata file path pass garda kheri ko indexing ( python try.py argument )

    data=read_driver_info(file_path)
    location = read_the_location(data)
    print(f"The location of race is: ",location)
    dri_code = read_driver_code_name(data)
    driver_info=get_driver_info()
    display_fastest_lap_times(dri_code, driver_info)


if __name__ == "__main__":
    main()
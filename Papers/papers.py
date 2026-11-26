"""
A smart traffic light system controls an intersection based on time of day: "Peak"/"Off-Peak";
traffic density: "High", "Medium", "Low"; and emergency vehicle detection: "Yes"/"No". If an emergency
vehicle is detected, the light must turn green immediately. During peak hours, green light duration is
extended for high traffic, kept normal for medium traffic, and reduced for low traffic. During offpeak hours, green remains normal. Write a Python program using nested if-else statements to read
these inputs and print the appropriate traffic light action. 
Input: Enter time of day: Peak
Enter traffic density : High
Emergency vehicle detected? : No
Output: Traffic Light Action: Extend GREEN light duration
"""

time = input("Enter time of day: ")
density = input("Enter traffic density: ")
emergency = input("Emergency vehicle deteched: ")


if emergency == "Yes":
    print("Green For Emergency")
else:
    if time == "Peak":
        if density == "High":
            print("Green light duration extended")
        else:
            if density == "Medium":
                print("Normal duration")
            else:
                if density == "Low":
                    print("Reduced")
    if time == "Off-Peak":
        print("Green Normal")
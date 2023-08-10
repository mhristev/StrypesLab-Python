import random

# Define constants
DAYS = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
HOURS = list(range(8, 21))  # 8 AM to 8 PM

# Define constraints
constraints = {
    'person1': [('Monday', 12, 17)],
}

# Define required hours per person per week
required_hours_per_person = 40

# Generate schedule
def generate_schedule():
    schedule = {day: {} for day in DAYS}
    
    for day in DAYS:
        for hour in HOURS:
            schedule[day][hour] = None
    
    for person in constraints:
        for shift in constraints[person]:
            day, start_hour, end_hour = shift
            for hour in range(start_hour, end_hour + 1):
                schedule[day][hour] = person
    
    for person in constraints:
        assigned_hours = sum(1 for day in DAYS for hour in HOURS if schedule[day][hour] == person)
        remaining_hours = required_hours_per_person - assigned_hours
        available_slots = [(day, hour) for day in DAYS for hour in HOURS if schedule[day][hour] is None]
        random.shuffle(available_slots)
        while remaining_hours >= 8 and available_slots:
            day, _ = available_slots.pop()
            for hour in range(8, 17):
                if schedule[day][hour] is None:
                    schedule[day][hour] = person
                    remaining_hours -= 1
    
    return schedule

# Print schedule
def print_schedule(schedule):
    print("   ", end="")
    for day in DAYS:
        print(f"{day:9}", end="")
    print()
    for hour in HOURS:
        print(f"{hour:02}:00", end="  ")
        for day in DAYS:
            person = schedule[day][hour]
            print(f"{person if person else '-':9}", end="")
        print()

# Generate and print the schedule
schedule = generate_schedule()
print_schedule(schedule)

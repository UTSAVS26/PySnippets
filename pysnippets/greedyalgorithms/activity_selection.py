def activity_selection(activities):
    if not activities:  # Check if the activities list is empty
        return []
    
    # Sort activities based on finish time
    activities.sort(key=lambda x: x[1])
    
    # Initialize the list with the first selected activity
    selected_activities = [(activities[0][0], activities[0][1])]
    
    # Track the last selected activity index
    last_selected = 0
    
    # Iterate through the remaining activities
    for i in range(1, len(activities)):
        if activities[i][0] >= activities[last_selected][1]:
            selected_activities.append((activities[i][0], activities[i][1]))
            last_selected = i
    
    return selected_activities

def main():
    n = int(input("Enter the number of activities: "))
    activities = []
    
    print("Enter start and finish times for each activity:")
    for i in range(n):
        start, finish = map(int, input(f"Activity {i + 1}: ").split())
        activities.append((start, finish))
    
    selected_activities = activity_selection(activities)
    
    print("The following activities are selected:")
    for activity in selected_activities:
        print(f"({activity[0]}, {activity[1]})", end=" ")

if __name__ == "__main__":
    main()

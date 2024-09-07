"""
This problem was asked by Amazon.

You are given a list of data entries that represent entries and exits of groups of people into a building.
An entry looks like this:

{"timestamp": 1526579928, count: 3, "type": "enter"}

This means 3 people entered the building. An exit looks like this:

{"timestamp": 1526580382, count: 2, "type": "exit"}

This means that 2 people exited the building. timestamp is in Unix time.

Find the busiest period in the building, that is, the time with the most people in the building.
Return it as a pair of (start, end) timestamps.
You can assume the building always starts off and ends up empty, i.e. with 0 people inside.
"""

def busiest_period(movement_list):
    building_states = [(None, None, 0)]

    for movement in movement_list:
        last_building_state = building_states[-1]
        if movement["type"] == "enter":
            if last_building_state[2] == 0:
                new_building_state = (movement["timestamp"], movement["timestamp"], last_building_state[2] + movement["count"])
            else:
                new_building_state = (last_building_state[0], movement["timestamp"], last_building_state[2]+movement["count"])
            building_states.append(new_building_state)
        else:
            # exit movement
            last_building_state = building_states[-1]
            new_building_state = (last_building_state[0], movement["timestamp"], last_building_state[2] - movement["count"])
            building_states.append(new_building_state)
    building_states.sort(key=lambda x: x[2],reverse=True)
    return building_states[0][0], building_states[0][1]


def busiest_period_2(movement_list):
    periods = (None, None)

    num_people, max_num_people = 0, 0

    # sort the entries by timestamp
    sorted_entries = sorted(movement_list, key=lambda e: e["timestamp"])

    for i, entry in enumerate(sorted_entries):
        if entry["type"] == "enter":
            num_people+=entry["count"]
        else:
            num_people-=entry["count"]

        if num_people > max_num_people:
            max_num_people = num_people
            periods = (entry["timestamp"], sorted_entries[i+1]["timestamp"])

    return periods
if __name__ == '__main__':
    building_movements = [
        {"timestamp": 1526579928, "count": 2, "type": "enter"},
        {"timestamp": 1526579938, "count": 2, "type": "exit"},
        {"timestamp": 1526579948, "count": 5, "type": "enter"},
        {"timestamp": 1526579958, "count": 7, "type": "enter"},
        {"timestamp": 1526579968, "count": 8, "type": "exit"},
        {"timestamp": 1526579988, "count": 10, "type": "enter"},
        {"timestamp": 1526579988, "count": 14, "type": "exit"}
    ]
    events = [
        {"timestamp": 1526579928, "count": 3, "type": "enter"},
        {"timestamp": 1526579982, "count": 4, "type": "enter"},
        {"timestamp": 1526580054, "count": 5, "type": "exit"},
        {"timestamp": 1526580128, "count": 1, "type": "enter"},
        {"timestamp": 1526580382, "count": 3, "type": "exit"}
    ]

    #
    print(busiest_period(building_movements))
    print(busiest_period_2(building_movements))


    print(busiest_period(events))
    print(busiest_period_2(events))

"""
This problem was asked by Facebook.

Given an unordered list of flights taken by someone, each represented as
(origin, destination) pairs, and a starting airport, compute the person's itinerary.
If no such itinerary exists, return null. If there are multiple possible itineraries,
return the lexicographically smallest one. All flights must be used in the itinerary.

For example, given the list of flights [('SFO', 'HKO'), ('YYZ', 'SFO'), ('YUL', 'YYZ'), ('HKO', 'ORD')]
and starting airport 'YUL', you should return the list ['YUL', 'YYZ', 'SFO', 'HKO', 'ORD'].

Given the list of flights [('SFO', 'COM'), ('COM', 'YYZ')] and starting airport 'COM', you should return null.

Given the list of flights [('A', 'B'), ('A', 'C'), ('B', 'C'), ('C', 'A')] and starting airport 'A',
you should return the list ['A', 'B', 'C', 'A', 'C'] even though ['A', 'C', 'A', 'B', 'C'] is also a valid itinerary.
However, the first one is lexicographically smaller.
"""

def get_dest(valid_filght_tuple):
    return valid_filght_tuple[0][1]


def find_valid_itinerary(list_of_flights, starting_point, valid_list=[]):
    # list of flights empty, then found a a valid list
    if len(list_of_flights) == 0 and len(valid_list)>0:
        return valid_list+[starting_point]

    # go over all the flights to find a valid origin point
    valid_flights = []
    for i in range(len(list_of_flights)):
        if list_of_flights[i][0] == starting_point:
            # found a flight with a valid origin
            valid_flights.append((list_of_flights[i], i))  # append tuple of ((origin, dest), entry_#)

    if len(valid_flights) == 0:
       return None

    # get the lexicographically first one
    valid_flights.sort(key=get_dest)

    # pick the first valid flight
    valid_list.append(valid_flights[0][0][0])

    # new starting point
    starting_point = valid_flights[0][0][1]

    # remove the flight taken
    flight_taken = valid_flights[0][1]

    return find_valid_itinerary(list_of_flights[:flight_taken]+list_of_flights[flight_taken+1:], starting_point,valid_list)

if __name__ == '__main__':
    # list_of_flights = [('SFO', 'HKO'), ('YYZ', 'SFO'), ('YUL', 'YYZ'), ('HKO', 'ORD')]
    # start = 'YUL'

    #print(find_valid_itinerary(list_of_flights, start))

    #print(find_valid_itinerary([('SFO', 'COM'), ('COM', 'YYZ')], 'COM'))

    print(find_valid_itinerary([('A', 'B'), ('A', 'C'), ('B', 'C'), ('C', 'A')], 'C'))

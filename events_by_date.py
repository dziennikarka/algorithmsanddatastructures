from datetime import datetime, timedelta
import http_req

# defining constants
DAYS = 30

time_now = datetime.utcnow()
time_future = time_now + timedelta(days=DAYS)

starting_time_iso = time_now.isoformat()
ending_time_iso = time_future.isoformat()

# function that chooses one name in any language


def choose_name(names):

    for lang, name in names.items():
        if name:
            return name
    return 'No name'


# function that searches events between today and today + days
def filter_events(events_to_filter):
    filtered_events = []
    for event in events_to_filter:
        event_day = event['event_dates']['starting_day']
        if event_day:
            if(event_day >= starting_time_iso and event_day <= ending_time_iso):
                filtered_events.append(event)
    return filtered_events

# function that sorts out events according to the starting date


def insertion_sort(events_to_sort):
    i = 1
    while i < len(events_to_sort):
        j = i
        while j > 0 and events_to_sort[j-1]['event_dates']['starting_day'] > events_to_sort[j]['event_dates']['starting_day']:
            temp_var = events_to_sort[j]
            events_to_sort[j] = events_to_sort[j-1]
            events_to_sort[j-1] = temp_var
            j = j - 1
        i = i + 1
    return events_to_sort


def main():
    # reading the data
    events = http_req.search_events()
    events_filtered = filter_events(events)

    # printing out filtered but unsorted list
    for event in events_filtered:
        print(choose_name(event['name']))
        print(event['event_dates']['starting_day'])

    sorted_list = insertion_sort(events_filtered)

    print()
    print('------------------------------------------------------------------------------')
    print('HERE IS SORTED LIST')
    print('------------------------------------------------------------------------------')

    # printing out a date and a name for the sorted list
    for event in sorted_list:
        print(choose_name(event['name']))
        print(event['event_dates']['starting_day'])

    # -------------------------printing out all the event per day----------------------------
    event_date = datetime.strptime(
        sorted_list[0]['event_dates']['starting_day'], '%Y-%m-%dT%H:%M:%S.%fZ').date()
    print(event_date)
    print()

    for i in range(len(sorted_list) - 1):
        e_date = datetime.strptime(
            sorted_list[i]['event_dates']['starting_day'], '%Y-%m-%dT%H:%M:%S.%fZ')
        hour = e_date.hour
        minute = e_date.minute
        name = choose_name(sorted_list[i]['name'])

        if(e_date.date() == event_date):

            print("{:02d}:{:02d} {:s}".format(hour, minute, name))
        else:
            event_date = e_date.date()
            print()
            print(event_date)
            print()
            print("{:02d}:{:02d} {:s}".format(hour, minute, name))
    # ------------------------------printing out day programme ends here--------------------------


if __name__ == '__main__':
    main()

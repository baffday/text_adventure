# Text Adventure
import random

def msg(room):
    if room['msg'] == '': #there is a custom message
        return "You have entered the " + room['name'] + '.'
    else:
        return room['msg']

def get_choice(room, dir):
    if dir == 'N':
        choice = 0
    elif dir == 'E':
        choice = 1
    elif dir == 'S':
        choice = 2
    elif dir == 'W':
        choice = 3
    else:
        return -1

    if room['directions'][choice] == 0:
        return 4
    else:
        return choice

def main():
    dirs = (0, 0, 0, 0) #default

    balcony = {'name': 'Balcony', 'directions':dirs, 'msg':''}
    bedroom1 = {'name': 'Bedroom 1', 'directions':dirs, 'msg':''}
    bedroom2 = {'name': 'Bedroom 2', 'directions':dirs, 'msg':''}
    hallwaynorth = {'name': 'Hallway North', 'directions':dirs, 'msg':''}
    hallwaymiddle = {'name': 'Hallway Middle', 'directions':dirs, 'msg':''}
    hallwaysouth = {'name': 'Hallway South', 'directions':dirs, 'msg':''}
    gamesroom = {'name': 'Games Room', 'directions':dirs, 'msg':''}
    lounge = {'name': 'Lounge', 'directions':dirs, 'msg':''}
    diningroom = {'name': 'Dining Room', 'directions':dirs, 'msg':''}
    kitchen = {'name': 'Kitchen', 'directions':dirs, 'msg':''}

    #directions are tuples: rooms to the (N, E, S, W)
    balcony['directions'] = (bedroom1, hallwaymiddle, bedroom2, 0)
    bedroom1['directions'] = (0, hallwaynorth, balcony, 0)
    bedroom2['directions'] = (balcony, hallwaysouth, 0, 0)
    hallwaynorth['directions'] = (0, 0, hallwaymiddle, bedroom1)
    hallwaymiddle['directions'] = (hallwaynorth, gamesroom, hallwaysouth, balcony)
    hallwaysouth['directions'] = (hallwaymiddle, lounge, 0, bedroom2)
    gamesroom['directions'] = (0, diningroom, lounge, hallwaymiddle)
    lounge['directions'] = (gamesroom, kitchen, 0, hallwaysouth)
    diningroom['directions'] = (0, 0, kitchen, gamesroom)
    kitchen['directions'] = (diningroom, 0, 0, lounge)

    #rooms where the jewels might be
    rooms = [gamesroom, lounge, diningroom, kitchen]
    room_with_jewels = random.choice(rooms)
    jewels_found = False
    room = balcony
    print ('''
The house is shrouded in darkness.
Can you find the jewels and get out without being caught?
            ''')

    while True:
        if jewels_found and room['name'] == 'Balcony':
            print ('''
You\'ve got the jewels back to the balcony.
Time to sneak down your rope and get those jewels to your fence.
Payday!
                    ''')
            break;
        elif not jewels_found and room['name'] == room_with_jewels['name']:
            jewels_found = True
            print(msg(room) + ' You found the jewels! Get out quick!')
            room['msg'] = ('You\'re back in the ' + room['name'] + '! You\'ve already got the jewels. '
                        + 'Time to escape before you are found!')
        else:
            print(msg(room))
            room['msg'] = 'You are back in the ' + room['name']

        stuck = True
        while stuck:
            dir = input("Which direction do you want to go: N, E, S, or W?").upper()
            choice = get_choice(room, dir)
            if choice == -1:
                dir = print ("Please enter N, E, S or W?")
            elif choice == 4:
                dir = print ("You cannot go that way.")
            else:
                room = room['directions'][choice]
                stuck = False

main()

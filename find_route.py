def find_route(total_miles, chargers):
    current_position = 0
    current_index= 0
    ev_range = 300
    route = []

    # while current_position <= total_miles:

    #     for i in range(current_index, len(chargers)):
    #         if chargers[i] - current_position >  ev_range:
    #             break

    #     current_index = i-1
    #     current_position = chargers[current_index]
    #     if route and current_position == route[-1]:
    #         return None
    #     route.append(current_position)

    #     print(f'current_index: {current_index}')
    #     print(f'current_position: {current_position}')
    #     print(f'route: {route}')

        

    # if (route[-1]+ev_range) >= total_miles:
    #     return route
    # return None
    while current_position<= total_miles:
        print(f'current_index: {current_index}')
        print(f'current_position: {current_position}')
        print(f'route: {route}')
        temp = 0
        for i in range(current_index, len(chargers)):
            print()
            if current_position + 300 <= chargers[i]:
                print(f'Found Charger: {chargers[i]}')
                pass
            else:
                current_index = i - 1
                current_position = chargers[current_index]
                route.append(current_position)
                break

        print(f'current_index: {current_index}')
        print(f'current_position: {current_position}')
        print(f'route: {route}')
        break 
        


print(f'Answer: {find_route(1000, [10, 250, 310, 500,650, 900])}')
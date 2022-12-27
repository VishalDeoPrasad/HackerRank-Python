def migratoryBirds(arr):
    # create a dictionary where each unique represent key and count as value
    unique_birds = set(arr)
    bird_count = {}
    for bird in unique_birds:
        bird_count[bird] = arr.count(bird)
    sorted_x = {k: v for k, v in sorted(bird_count.items(), key=lambda item: item[1])}
    #print(sorted_x)
    value_list = list(sorted_x.values())
    key_list = list(sorted_x.keys())
    #print(value_list, key_list)

    if value_list[-1] == value_list[-2]:
        if key_list[-1] < key_list[-2]:
            return key_list[-1]
        else:
            return key_list[-2]
    else:
        return key_list[-1]

print(migratoryBirds([1,4,4,4,5,3]))
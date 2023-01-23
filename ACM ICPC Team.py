def normalize_string(topic):
    new_topic = []
    for i in range(len(topic)):
        temp_lst = []
        for j in range(len(topic[0])):
            if topic[i][j] == '1':
                temp_lst.append(j+1)
        
        new_topic.append(temp_lst)
        temp_lst = []
    return new_topic
            

def acmTeam(topic):
    # Write your code here
    topic = normalize_string(topic)
    pair_list = []
    for i in range(len(topic)-1):
        for j in range(i+1, len(topic)):
            pair_list.append(len(set(topic[i]+topic[j])))
    print(pair_list)
    return max(pair_list), pair_list.count(max(pair_list))

topic1 = ['10101', '11110', '00010']
topic = ['10101' ,'11100', '11010', '00101']

print(acmTeam(topic))
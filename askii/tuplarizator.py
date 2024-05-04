

def make_tuple(file, num_of_str = 17):
    proto_list = []
    with open(file, 'r') as f:
        
        for i in range(num_of_str):
            line = f.readline().rstrip('\n')
            proto_list.append(line)
    
    
    # proto_list = []
    # for i in range(num_of_str):
    #     line = file.readline().rstrip('\n')
    #     if len(line) < str_len:
    #         line = line.ljust(str_len)
    #     elif len(line) > str_len:
    #         line = line[:str_len]
    #     proto_list.append(r"{}".format(file.readline()))
    # print(proto_list)
    return proto_list




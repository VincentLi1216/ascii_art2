import json

def mapping(list, down_boun, up_boun):
    _max = max(list)
    _min = min(list)
    normalized = [(x-_min)/(_max-_min) for x in list]
    ans = [down_boun+x*(up_boun-down_boun) for x in normalized]
    return ans


def find_closest(lst, target):
    """
    Find the number in the list that is closest to the target.
    """
    return min(lst, key=lambda x: abs(float(x) - target))

def json_reader(file_path):
    with open(file_path) as f:  
        data = json.load(f)
    return data

def json_writer(data, file_path):
    with open(file_path, "w") as f:
        json.dump(data, f, indent = 4)
    


if __name__ == "__main__":
    
    # l1 = [1,2,3,4]
    # print(mapping(l1, 0, 255))

    # lst = [1, 5, 8, 12, 20]
    # target = 10

    # closest_number = find_closest(lst, target)
    # print(closest_number)
    
    # print(json_reader("./darkness_dict.json"))
    pass

def mapping(list, down_boun, up_boun):
    _max = max(list)
    _min = min(list)
    normalized = [(x-_min)/(_max-_min) for x in list]
    ans = [down_boun+x*(up_boun-down_boun) for x in normalized]
    return ans




if __name__ == "__main__":
    l1 = [1,2,3,4]
    print(mapping(l1, 0, 255))

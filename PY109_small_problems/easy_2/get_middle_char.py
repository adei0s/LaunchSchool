def center_of(string):
    if len(string) % 2 == 1:
        center_idx = len(string)//2
        return string[center_idx]
    else:
        left_idx = len(string)//2 - 1
        return string[left_idx : left_idx + 2]

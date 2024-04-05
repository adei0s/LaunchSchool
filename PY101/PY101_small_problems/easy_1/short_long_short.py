def short_long_short(str1, str2):
    if len(str1) <= len(str2):
        short_str = str1
        long_str = str2
    else:
        short_str = str2
        long_str = str1
    
    return short_str + long_str + short_str

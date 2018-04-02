def num_of_patterns(astr,pattern):
    astr, pattern = astr.strip(), pattern.strip()
    if pattern == '':return 0

    ind, count, start_flag = 0,0,0
    while True:
        try:
            if start_flag == 0:
                ind = astr.index(pattern)
                start_flag = 1
            else:
                ind += 1 + astr[ind+1:].index(pattern)
            count += 1
        except:
            break
    return count

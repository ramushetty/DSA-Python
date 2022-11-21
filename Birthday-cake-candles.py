def birthdayCakeCandles(candles):
    max_num = max(candles)
    # count = 0
    # for i in candles:
    #     if max_num == i:
    #         count += 1
    # if count > 1:
    #     return count
    # return 1
    return candles.count(max_num)



print(birthdayCakeCandles([3,1,2,3]))
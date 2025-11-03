def convert2binary(num: int) -> str:
    result = " "
    while num > 0:
        if num % 2 == 0:
            result += "0"
        else:
            result += "1"
        num = num // 2
    result = result[::-1]
    return result


print(convert2binary(13))

"""Time Complexity : O(log2N)
    Space Complexity : O(log2N)"""


def decimal_to_binary(n:int):
    if n == 1:
        return "1"
    if n == 0:
        return "" 
    quotient = int(n/2)
    remainder = n%2
    if remainder == 1:
        return decimal_to_binary(quotient)+"1"
    else: return decimal_to_binary(quotient)+"0"

print(decimal_to_binary(13)) #1101
print(decimal_to_binary(25)) #11001
print(decimal_to_binary(1379)) # 10101100011
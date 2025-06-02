# format specifiers = {:flags} format a value based on what flags are inserted

# :.(number)f = round to that many decimal places (fixed point)
# :(number) = allocate that many spaces
# :03 = allocate and zero pad that many spaces
# :< = left justify
# :> = right justify
# :^ = center align
# :+ = use a plus sign to indicate positive value
# := = place sign to leftmost position
# :  = insert a space before positive numbers
# :, = comma seperator

price1 = 30000.5676
price2 = -898996.68
price3 = 12097887.34
# :.(number)f = round to that many decimal places (fixed point)
# print(f"Price 1 is ${price1:.2f}") # round up to 2 decimal places
# print(f"Price 2 is ${price2:.2f}") # round up to 2 decimal places
# print(f"Price 3 is ${price3:.2f}") # round up to 2 decimal places

# :(number) = allocate that many spaces
# print(f"Price 1 is ${price1:10}") # now has a total of 10 spaces
# print(f"Price 2 is ${price2:10}") # now has a total of 10 spaces
# print(f"Price 3 is ${price3:10}") # now has a total of 10 spaces

# :03 = allocate and zero pad that many spaces
# print(f"Price 1 is ${price1:010}") # add zero at the front
# print(f"Price 2 is ${price2:010}") # add zero at the front
# print(f"Price 3 is ${price3:010}") # add zero at the front

# :< = left justify
# print(f"Price 1 is ${price1:<10}") # move to the left
# print(f"Price 2 is ${price2:<10}") # move to the left
# print(f"Price 3 is ${price3:<10}") # move to the left

# :> = right justify
# print(f"Price 1 is ${price1:>10}") # move to the right
# print(f"Price 2 is ${price2:>10}") # move to the right
# print(f"Price 3 is ${price3:>10}") # move to the right

# :^ = center align
# print(f"Price 1 is ${price1:^10}") # align to the center
# print(f"Price 2 is ${price2:^10}") # align to the center
# print(f"Price 3 is ${price3:^10}") # align to the center

# :+ = use a plus sign to indicate positive value
# print(f"Price 1 is ${price1:+10}") # add a plus sign
# print(f"Price 2 is ${price2:+10}") # add a plus sign
# print(f"Price 3 is ${price3:+10}") # add a plus sign

# := = place sign to leftmost position
# print(f"Price 1 is ${price1:= =}") # place sign to leftmost position
# print(f"Price 2 is ${price2:= =}") # place sign to leftmost position
# print(f"Price 3 is ${price3:= =}") # place sign to leftmost position

# :  = insert a space before positive numbers
# :, = comma seperator
print(f"Price 1 is ${price1:,}") # add comma
print(f"Price 2 is ${price2:,}") # add comma
print(f"Price 3 is ${price3:,}") # add comma




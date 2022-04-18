'''
1 chocolates equals 1 rupee and for every 3 wrappers you will receive 1 chocolate
'''

money = 15
chacolates = money
wrapper = chacolates


while(wrapper>=3):
    extra_chacolates = int(wrapper/3)
    print(f"extra_chacolates : {extra_chacolates}")

    wrapper = int(wrapper/3) + int(wrapper%3)
    print(f"wrapper : {wrapper}")

    chacolates += extra_chacolates
    print(f"chacolates : {chacolates}")


print(f"Total {chacolates} chocolates for money {money}")
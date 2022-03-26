money = int( input("Enter $: ") )

bills_20 = money // 20
bills_5 = ( money - bills_20 * 20 ) // 5
bills_1 = money % 5

print( bills_20, "x $20 +", bills_5, "x $5 +", bills_1, "x $1" )
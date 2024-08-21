#INCOME TAX CALCULATOR. 13/1/2023
#Vaibhavi Singhania S6-C
'''The program inputs the annual income of a person and calculate the payable income tax.
The Income Tax slabs are as follows:
If income is upto Rs. 2,50,000 , income tax is nil.
If income is Rs. 2,50,001 to Rs. 5,00,000 , income tax is 5% above ₹ 2,50,000.
If income is Rs. 5,00,001 to Rs. 7,50,000 , income tax is ₹ 12,500 + 10% above ₹ 5,00,000.
If income is Rs. 7,50,001 ro Rs. 10,00,000 , income tax is ₹ 37,500 + 15% above ₹ 7,50,000.
If income is Rs. 10,00,001 to Rs. 12,50,000, income tax is ₹ 75,000 + 20% above ₹ 10,00,000.
If income is Rs. 12,50,001 to Rs. 15,00,000 , income tax is ₹ 1,25,000 + 25% above ₹ 12,50,000.
If income is above Rs. 15,00,000 , income tax is 3₹ 1,87,500 + 30% above ₹ 15,00,000.
'''
income=int(input("Please enter your annual income in INR: " )) 
if (income<=250000):
    print("Your Income Tax Slab is: Upto Rs. 2,50,000 , income tax is nil.")
    print("No tax") 
elif (income<=500000):
    print("Your Income Tax Slab is: Rs. 2,50,001 to Rs. 5,00,000 , income tax is 5% above ₹ 2,50,000.")
    print("Tax is Rs ", ((income-250000)/20)) 
elif (income<=750000):
    print("Your Income Tax Slab is: Rs. 5,00,001 to Rs. 7,50,000 , income tax is ₹ 12,500 + 10% above ₹ 5,00,000.")
    print("Tax is Rs ", ((income-500000)/10) + 12500) 
elif (income<=1000000):
    print("Your Income Tax Slab is: Rs. 7,50,001 ro Rs. 10,00,000 , income tax is ₹ 37,500 + 15% above ₹ 7,50,000.")
    print("Tax is Rs ", (3*(income-750000)/20) + 37500) 
elif (income<=1250000):
    print("Your Income Tax Slab is: Rs. 10,00,001 to Rs. 12,50,000, income tax is ₹ 75,000 + 20% above ₹ 10,00,000.")
    print("Tax is Rs ", ((income-1000000)/5) + 75000) 
elif (income<=1500000):
    print("Your Income Tax Slab is: Rs. 12,50,001 to Rs. 15,00,000 , income tax is ₹ 1,25,000 + 25% above ₹ 12,50,000.")
    print("Tax is Rs ", ((income-1250000)/4) + 125000) 
else:
    print("Your Income Tax Slab is: Above Rs. 15,00,000 , income tax is 3₹ 1,87,500 + 30% above ₹ 15,00,000.")
    print("Tax is Rs ", (3*(income-1500000)/10) + 187500) 

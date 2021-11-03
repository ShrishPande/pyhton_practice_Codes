amount = int(input("Enter the value\n"))

fiveh = amount//500
amount = amount%500

twoh = amount//200
amount = amount%200

hun = amount//100
amount = amount%100

fifty = amount//50
amount = amount%50

twenty = amount//20
amount = amount%20

five = amount//5

print("500:",fiveh)
print("200:",twoh)
print("100:",hun)
print("50:",fifty)
print("20:",twenty)
print("5:",five)
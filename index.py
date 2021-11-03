amount =int(input("Enter Thhe value"))-100

twok = amount//2000
amount = amount%2000

fivek = amount//500
amount = amount%500

twhu = amount//200
amount = amount%200

hun = amount//100

print("2000:",twok)
print("500:",fivek)
print("200:",twhu)
print("100:",hun+1)
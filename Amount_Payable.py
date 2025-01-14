#Program to find amount payable for a given vaule of principal,rate and time .
#Ask user to provied input for principal,rate,time.
principal=int(input('Enter Principal Amount:'))
rate=int(input('Enter Interst Rate% Per Anumm:'))
time=int(input('Enter Time To Find Interst:'))
#Find simple interst amount= (P x R x T)/ 100 for the above user input.
si=(principal * rate * time)/ 100
#Find amount payable= = Principal + SI.
ap=principal+si
#Show output on the screen
print("Amount Payable = ",ap," for Principal = ",principal," , rate% = ",rate," and time = ",time )




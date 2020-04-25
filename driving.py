country = input('Please enter your nationality: ')
age = input('Please enter your age: ')
age = int(age)
if country == 'Taiwan' or country == 'Hong Kong':
	if age >= 18:
		print('You can now apply the driving licences!')
	else:
		print('You are not allowed to apply the driving licences!')
elif country == 'America':
	if age >= 16:
		print('You can now apply the driving licences!')
	else:
		print('You are not allowed to apply the driving licences!')
else:
	print('You can only type Taiwan / America / Hong Kong')
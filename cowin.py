from requests import get 

pincode = input('Enter Pin Code: ') # Taking Pincode and Date as user input
date = input('Enter Date: ') #DD-MM-YYYY Format ----> You can mention this if you want

# The link for API call -:
link = f'https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByPin?pincode={pincode}&date={date}'

data = get(link).json() # Getting the data

center_num = len(data['centers'])  # Total Number of centers

## Formatting 
print()
print('                               >>> RESULTS <<<                               ')
print('-----------------------------------------------------------------------------')
print(f'Date : {date} | Pincode : {pincode}') # Printing the date and pincode

if center_num != 0:
    print(f'Total number of centers in your area: {center_num}')
else:
    print('Sorry, no center found in your area at the moment. Try again later!')
    print('-----------------------------------------------------------------------------')
    print()

for center in range(center_num): # To print the name of centers in a particular order
    print()
    print(f'[{center+1}] Center Name: ', data['centers'][center]['name'])

    fee = data['centers'][center]['fee_type'] # Storing the fee_type in fee var

    print('----------------------------------------------------------------')
    print('    Date        Vaccine        Age          Fee          Slots  ')
    print('----------------------------------------------------------------')

    sessions = data['centers'][center]['sessions'] # Storing the Sessions in sessions var

    for session in range(len(sessions)): # To print the data in sessions in an order
        print('{0:^12} {1:^13} {2:^11} {3:^14} {4:^12}'.format(sessions[session]['date'], sessions[session]['vaccine'], sessions[session]['min_age_limit'], fee, sessions[session]['available_capacity']))
                
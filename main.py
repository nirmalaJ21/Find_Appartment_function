def apt_search1(city,max_rent,min_beds,pet_allowed):
   if pet_allowed == 'True':
     print(f"\nWelcome to GC Property Management! Looking up listings in {city} for {min_beds} bedroom apartments that allow pets, all within a budget of ${max_rent} per month...")
   else:
     print(f'\nWelcome to GC Property Management! Looking up listings in {city} for {min_beds} bedroom apartments, all within a budget of ${max_rent} per month...')

def apt_search2(city ,max_rent,min_beds = 2,pet_allowed = True):
    if pet_allowed is None:
        print(f'\tWelcome to GC Property Management! Looking up listings in {city} for {min_beds} bedroom apartments, all within a budget of {max_rent}per month...')
    elif min_beds is None:
        print(f'\tWelcome to GC Property Management! Looking up listings in {city} that allow pets within a budget of {max_rent}per month...')
    else:
        print(f"\tWelcome to GC Property Management! Looking up listings in {city} for {min_beds}bedroom apartments that allow pets, all within a budget of ${max_rent} per month...")


# Examples of calling the function with different arguments
# Named arguments calling def apt_search1  function when boolean is True
print('\t\nNamed arguments calling def apt_search1  function when boolean is True'.upper())
print('*' *100)
apt_search1(city='Michigan',max_rent = '2000',min_beds='2',pet_allowed ='True')
print('*' *100)
#Named arguments calling def apt_search1 when boolean is False
print('\t\t\n Named arguments calling def apt_search1 when boolean is False.'.upper())
print('*' *100)
apt_search1('Michigan','2000','2','False')
print('*' *100)
# Uses default value of min_beds = 2,pet_allowed = True in def apt_search2 function /min_beds and pets_allowed both omitted.
print('*' *100)
print('Uses default value /min_beds and pets_allowed both omitted in search2 function.'.upper())
print('*' *100)
apt_search2('Michigan','2000')

# calling search2 function with no min_beds and just pets_allowed
print('*' *100)
print('calling search2 function with no min_beds and just pets_allowed'.upper())
print('*' *100)
apt_search2('Michigan','2000',None,'True')
# calling search2 function with just min_beds and no pets_allowed
print('*' *100)
print('calling search2 function with just min_beds and no pets_allowed'.upper())
print('*' *100)
apt_search2('Michigan','2000','3',None)

add_one_hundred  = lambda x : x +100
square_num = lambda x: x*2
concatenate = lambda x: '-' + x
divide_by_three = lambda x : x/3
print('\n\nCalling add_one_hundred lambda function:',add_one_hundred(9))
print('\nCalling square_num lambda function:',square_num(4))
print('\nCalling concatenate lambda function:',concatenate(' hello'))
print('\nCalling divide_by_three lambda function:',divide_by_three(9))





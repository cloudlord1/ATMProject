pin=1234
balance=10000
count=0
"""atm project that takes in pin, starts with a balance of 10000  and runs 3 times, it charges 100 for
 transfer .The PIN is 1234, the balance is 10000"""

#menu
for i in range(1,4):
    print('Welcome to providus Bank ATM')
    print('Please insert your card')
    wpin=int(input('enter your 4-digit pin: '))
    if wpin==pin:
        #options
        print('What type of account do you have','\n', '1- Savings', '2-Current')
        account_type=int(input('What type of account do you have? :'))
        if account_type==1 or account_type==2:
            print('What do you want to do today?','\n', 'Press 1 to checekbalance','\n', 'Press 2 to withdraw',
        '\n', 'Press 3 to transfer','\n', 'press 4 to exit')
        makechoice=int(input('What do you want to do today :'))
        #checkbalance
        if makechoice==1:
            print('Dear User your balance is', 'N', balance )
        #withdraw
        elif makechoice==2:
            print('Press 1 to withdrawl 500', '\n', 'press 2 to withdrawl 1000', '\n', 
            'press 3 to withdrawl 2000','\n', 'press 4 to withdrawl 5000' )
            withdrawal_amount=int(input('How much do you want to withdraw :'))
            if withdrawal_amount==1:
                print('please wait')
                balance=balance-500
            elif withdrawal_amount==2:
                print('please wait')
                balance= balance-1000
            elif withdrawal_amount==3:
                print('please wait')
                balance= balance-2000
            elif withdrawal_amount==4:
                print('please wait')
                balance= balance-5000
            print ('your current balance is:','N',balance)
            #transfer
        elif makechoice==3:
            print('Please note there will be a charge of N100 per transfer ')
            print('Press 1  to perform local transfer','\n', 'Press 2 to transfer to other banks')
            transfer_coefficient= int(input('Where do you want to tranfer: '))
            #local_transfer
            if transfer_coefficient==1:
                account_num1=int(input('enter 10-digit account number :'))
                print('Press 1 to transfer 1000', '\n', 'press 2 to transfer 2000', '\n', 
            'press 3 to transfer 5000','\n', 'press 4 to tranfer 10000' )
                how_much1=int(input('how much should be transferred :'))
                if how_much1==1:
                    print('please wait, 1000 is being sent to',account_num1)
                    balance=balance-1100
                elif how_much1==2:
                    print('please wait, 2000 is being sent to',account_num1)
                    balance= balance-2100
                elif how_much1==3:
                    print('please wait, 5000 is being sent to',account_num1)
                    balance= balance-5100
                elif how_much1==4:
                    print('please wait, 10000 is being sent to',account_num1)
                    balance= balance-10100
                #transfer to other bank
            if transfer_coefficient==2:
                nameofbank=input('enter the name of the bank: ')
                account_num1=int(input('enter 10-digit account number :'))
                print('\n','Press 1 to transfer 1000', '\n', 'press 2 to transfer 2000', '\n', 
            'press 3 to transfer 5000','\n', 'press 4 to tranfer 10000' )
                how_much2=int(input('how much should be transferred :'))
                if how_much2==1:
                    print('please wait, N1000 is being sent to',account_num1)
                    balance=balance-1100
                elif how_much2==2:
                    print('please wait, N2000 is being sent to',account_num1)
                    balance= balance-2100
                elif how_much2==3:
                    print('please wait, N5000 is being sent to',account_num1)
                    balance= balance-5100
                elif how_much2==4:
                    print('please wait, N10000 is being sent to',account_num1)
                    balance= balance-10100
        else :
            print('Thank you for banking with us at Providus')
    else:
        print('Wrong userpin ')
    count+=count
    print('this is the number', i, 'count')
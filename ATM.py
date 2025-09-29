import psycopg2
import random

conn = psycopg2.connect(host="localhost",user="postgres",password="sukh2003",database="test",port=5432)
c = conn.cursor()



# c.execute('CREATE TABLE acc_details (acc_no BIGINT PRIMARY KEY CHECK (LENGTH(acc_no::TEXT) = 11) NOT NULL,  name VARCHAR(100) NOT NULL, phone_no BIGINT CHECK (LENGTH(phone_no::TEXT) = 10) NOT NULL,balance DECIMAL(10, 2) NOT NULL, pin INT CHECK (LENGTH(pin::TEXT) = 4)) ')
# conn.commit()

# c.execute("INSERT INTO acc_details (acc_no, name, phone_no, balance, pin)VALUES(12345678901, 'John Doe', 9876543210, 1500.50, 1234),(23456789012, 'Jane Smith', 8765432109, 3200.75, 2345),(34567890123, 'Alice Brown', 7654321098, 10000.00, 3456), (45678901234, 'Bob Johnson', 6543210987, 540.25, 4567), (56789012345, 'Charlie Davis', 5432109876, 8900.00, 5678)")

# # c.execute("INSERT INTO acc_details (acc_no, name, phone_no, balance)VALUES(67890123456, 'David Lee', 4321098765, 7800.50), (78901234567, 'Eva Green', 3210987654, 4100.75),(89012345678, 'Frank Miller', 2109876543, 6700.00),(90123456789, 'Grace Wilson', 1098765432, 520.25), (12345098765, 'Henry Moore', 1987654321, 2300.00)")

# c.execute("ALTER TABLE acc_details ADD card_no BIGINT UNIQUE CHECK (card_no >= 1000000000000000 AND card_no <= 9999999999999999)")
# conn.commit()





def pin():
    global pin_
    pin_ = (input('Enter the Four PIN : '))
    if len(pin_) == 4 and pin_.isdigit():
        c.execute(f'select * from acc_details where card_no = {card_1} and pin = {pin_}')
        result = c.fetchall()
        c.execute(f'select * from acc_details where card_no = {card_1} and pin is null')
        re = c.fetchall()
        if result:
            print('valid pin')
            options()
        elif re:
            print('pin generation')
            
           
        else:
            print('invalid pin')

        
        
    else:
        print('ENTER FOUR DIGIT PIN')
    
    
def options():
    global pin_
    print('enter what operation you want to do \n1. deposit\n2.withdraw\n3.check bal\n4.QUIT')
    select = int(input('enter the selected option : '))
    if select == 1:
        amt = int(input('Enter the amount you want to deposit : '))
        c.execute(f'update acc_details set balance = {amt} + balance where pin = {pin_}')
            
        c.execute(f'select balance from acc_details where pin = {pin_}')
        ubal = c.fetchall()
        print(f'your current balance is {ubal}')
            
    elif select == 2:
            
        amt1 = int(input('Enter the amount you want to deposit : '))
        c.execute(f'update acc_details set balance = balance - {amt1} where pin = {pin_}')
            
        c.execute(f'select balance from acc_details where pin = {pin_}')
        ubal1 = c.fetchall()
            
        print(f'your current balance is {ubal1}')
        print(f'ammout you withdarw is {amt1}')

    elif select == 3:
        c.execute(f'select balance from acc_details where pin = {pin_}')
        d = c.fetchall()
        for i in d :
            print(f'your current balance is {d}')
    elif select == 4:
        print('thank you for using ATM')
    else:
        print('enter valid option')
        

print("WELCOME TO ATM \nENTER YOUR CARD")
card_1 = int(input('type the card no here  : '))
c.execute(f'select balance,pin,acc_no from acc_details where card_no = {card_1} and pin is not null')
card_2 = c.fetchall()
c.execute(f'select * from acc_details where card_no = {card_1} and pin is null')
re = c.fetchall()


if re:
    print('Account is present but there is no pin genaration requried')
    phone = input('enter your registed phone no. : ')
    c.execute(f'select * from acc_details where phone_no = {phone}')
    pd = c.fetchall()
    
    if pd:
        print('phone no matches')
        otp = random.randint(1000, 9999)
        print(otp)
        otp1 = int(input('enter the otp : '))
        
        if otp == otp1:
            print('otp matchs')
            ping = int(input('enter the pin you want to generate for your ATM card : '))
            c.execute(f'update acc_details set pin = {ping} where phone_no = {phone}')
            conn.commit()
            print('pin generated succesfully')
            
        else:
            print('not match')
    
    else:
        print('number not present')
    
          
        
elif card_2:
    print('account present')
    pin()
    
else:
    print('account not present')
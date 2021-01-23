blockchain = []
def switch(flag):
    flag = not flag
    return flag

def dialog():
    usr_select = input("Please enter \n  a to insert new amount \n  b to checkout the whole chain \n  q to exit \n")
    return usr_select
def seperator_line():
    print("=================================================================")
def process_usr_input():
    flag = True
    while (flag):
        seperator_line()
        usr_select = dialog()
        if (usr_select == 'a'):
            usr_session_amount = get_transaction_amount()
            add_transaction(usr_session_amount, return_last_transaction())
            print("\n****** Amount saved, back to menu ******")
        elif (usr_select == 'b'):
            return_blockchain()
        elif (usr_select == 'q'):
            print("exiting")
            flag = switch(flag)
        else:
            print("****** Incorrect input, please re-enter ******")
            pass

def get_transaction_amount():
    flag = True
    entered_amount = input("\nPlease enter the amount: ")
    while(flag):
        try:
            amount = float(entered_amount)
            switch(flag)
        except Exception as ex:
            print("'{}' is NOT a correct transaction amount, please re-enter \n {}".format(entered_amount, ex))
            exit(0)
        else:
            return amount

def return_last_transaction():
    if len(blockchain) >= 1:
        return blockchain[-1]
    return None

def add_transaction(transaction_amount, last_transaction = [0]):
    if last_transaction == None:
        last_transaction = [0]
    blockchain.append([last_transaction, transaction_amount])

def return_blockchain():
    print("\n****** The current blockchain is: {} ******\n".format(blockchain))

process_usr_input()

owner = "hash later"
blockchain = []
open_transactions = []
genesis_block =
    {'prev_hash': '',
    'index': 0,
    'transaction': []}

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
            trx_response = get_transaction_amount()
            recipient, amount = trx_response
            add_transaction(receiver = recipient, amount = amount)
            print("\n****** Amount saved, back to menu ******")
            seperator_line()
        elif (usr_select == 'b'):
            return_blockchain()
            seperator_line()
        elif (usr_select == 'q'):
            print("exiting")
            flag = switch(flag)
        else:
            print("****** Incorrect input, please re-enter ******")
            pass

def get_transaction_amount():
    trx_recipient = input("Please enter recipient: ")
    trx_amount = float(input("\nPlease enter the amount: "))
    return trx_recipient, trx_amount

def return_last_transaction():
    if len(blockchain) >= 1:
        return blockchain[-1]
    return genesis_block

def add_transaction(sender = owner, receiver, amount = 1):
    transaction = {"sender":send, "receiver":receive, "amount"= amount}
    open_transaction.append(transaction)

def return_blockchain():
    print("\n****** The current blockchain is: {} ******\n".format(blockchain))

def mining_block():
    last_block = return_last_transaction()
    for keys in last_block:

    block =
    {'prev_hash':'hash',
    'index': len(blockchain),
    'transaction': open_transactions}



process_usr_input()

blockchain = []
def switch(flag):
    flag = not flag
    return flag

def dialog():
    flag = True
    while (flag):
        usr_input = input("Please enter \n  a to insert new amount \n  b to checkout the whole chain \n  q to exit \n")
        if (usr_input == 'a'):
            add_to_blockchain(float(input("\nPlease enter the amount: ")))
            print("\n****** Amount saved, back to menu ******\n")
        elif (usr_input == 'b'):
            return_blockchain()
        elif (usr_input == 'q'):
            print("exiting")
            flag = switch(flag)
        else:
            print("****** Incorrect input, please re-enter ******\n")
            pass

def init():
    blockchain.append(1)
def add_to_blockchain(input):
    blockchain.append([blockchain[-1], input])

def return_blockchain():
    print("\n****** The current blockchain is: {} ******\n".format(blockchain))

init()
dialog()

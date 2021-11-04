def subtract_funds1(account: str, amount: int):
    '''Subtract funds from bank account then return; '''
    bank[account] -= amount
    return

def subtract_funds2(account: str, amount: int):
    '''Subtract funds from bank account then ⁧''' ;return
    bank[account] -= amount
    return

bank = {'alice': 100}

subtract_funds2('alice', 50)
print(bank)
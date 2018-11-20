import json
import os
import hashlib

blockchain_dir = os.curdir + '/blocks/'

def get_hash(filename):
    hash_ = ''
    with open(filename, 'rb') as file:
        hash_ = hashlib.sha256(file.read()).hexdigest()
    return hash_


def write_block(lender, amount, borrower):
    max_file = max([int(file) for file in os.listdir(blockchain_dir)])
    new_file = str(max_file + 1)
    new_hash = get_hash(blockchain_dir + str(max_file))

    data = {
        'lender': lender,
        'amount': amount,
        'borrower': borrower,
        'hash': new_hash
    }

    with open(blockchain_dir + new_file, 'w') as file:
        json.dump(data, file, indent=4, ensure_ascii=False)


def check_integrity():
    files = os.listdir(blockchain_dir)
    files = sorted([int(file) for file in files])
    results = []
    
    for file in files[1:]:
        with open(blockchain_dir + str(file)) as checking:
            hash_from_file = json.load(checking)['hash']
        
        actual_hash = get_hash(blockchain_dir + str(file - 1))
        if hash_from_file == actual_hash:
            res = 'Ok'
        else:
            res = 'Corrupted'
        results.append({'block':(file - 1), 'result': res})

    results.append({'block':(files[-1]), 'result': 'not checked'})
    return results


def create_initial_block():
    new_file = str(0)
    
    data = {
        'lender': '',
        'amount': '',
        'borrower': '',
        'hash': ''
    }

    with open(blockchain_dir + new_file, 'w') as file:
        json.dump(data, file, indent=4, ensure_ascii=False)


if __name__ == '__main__':
    create_initial_block()
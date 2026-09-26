def main():
    random_dic = {
        111 : 'someone called 01',
        222 : 'someone called 02',
        777 : 'someone called 07'
    }

    random_dic[999] = 'someone called 09'
    
    del random_dic[222]

    print(f"Calling by the key {random_dic[999]}")

main()
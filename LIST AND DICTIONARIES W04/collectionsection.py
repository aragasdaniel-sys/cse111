def main():
    # COMPOUND LIST
    clist = [1,2,3,['a','b','c']]
    v=clist[3]
    print(v[1])
    print()

    ### DICTIONARIES ###
    book = {
        'name':'1 Neph', 
        'chapters': 20
    }
    #     KEY  -  VALUE
    print(book['name'])

    # UPDATE
    book['name'] = '1 Nephi'

    # ADD
    book['stdwork']='Book of Mormon'

    # REMOVE
    del book['chapters']

    print(book)

if __name__ == "__main__":
    main()

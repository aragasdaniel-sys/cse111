def read_list(filename):
    text_list = []
    with open(filename, "rt") as provinces_text:
        for line in provinces_text:
            clean_line = line.strip()
            text_list.append(clean_line)
    
    return text_list
            
def modify_list(provinces):
    # Remove first element
    provinces.pop(0)
    # Remove last element
    provinces.pop()
    for i in range(len(provinces)):
        if provinces[i] == "AB":
            provinces[i] = "Alberta"
    count = provinces.count("Alberta")

    return count


def main():
    provinces_list = read_list("provinces.txt")
    print(provinces_list)

    alberta_count = modify_list(provinces_list)
    print(f"Alberta occurs {alberta_count} times in the modified list")

if __name__ == "__main__":
    main()
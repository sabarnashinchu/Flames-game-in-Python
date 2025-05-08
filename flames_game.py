def get_flames_result(name1, name2):
    # Convert names to lowercase and remove spaces
    name1 = name1.lower().replace(" ", "")
    name2 = name2.lower().replace(" ", "")
    
    # Create a list of remaining letters after removing common letters
    remaining_letters = []
    for char in name1:
        if char not in name2:
            remaining_letters.append(char)
    for char in name2:
        if char not in name1:
            remaining_letters.append(char)
    
    # Calculate the number of remaining letters
    count = len(remaining_letters)
    
    # FLAMES dictionary
    flames = {
        1: "Friends",
        2: "Love",
        3: "Affection",
        4: "Marriage",
        5: "Enemy",
        0: "Siblings"
    }
    
    # Calculate the result
    while count > 6:
        count = count % 6
    
    return flames[count]

def main():
    print("Welcome to the FLAMES Game!")
    print("FLAMES stands for:")
    print("F - Friends")
    print("L - Love")
    print("A - Affection")
    print("M - Marriage")
    print("E - Enemy")
    print("S - Siblings")
    print("\n" + "="*50 + "\n")
    
    while True:
        name1 = input("Enter the first name: ").strip()
        name2 = input("Enter the second name: ").strip()
        
        if not name1 or not name2:
            print("Please enter valid names!")
            continue
            
        result = get_flames_result(name1, name2)
        print(f"\nThe relationship between {name1} and {name2} is: {result}")
        
        play_again = input("\nDo you want to play again? (yes/no): ").lower()
        if play_again != 'yes':
            print("\nThanks for playing FLAMES!")
            break
        print("\n" + "="*50 + "\n")

if __name__ == "__main__":
    main() 
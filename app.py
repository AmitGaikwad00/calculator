from cal import add,sub


def main():
    print('cal')
    print("""
          select
          1. add
          2. sub
          """)
    
    user_input = int(input("select"))
    
    a = int(input("value A "))
    b = int(input("value B "))
    
    
    if user_input == 1:
        result = add(a,b)
    elif user_input ==2:
        result = sub(a,b)
        
    print(f"result: {result}")
        
if __name__ == "__main__":
    main()
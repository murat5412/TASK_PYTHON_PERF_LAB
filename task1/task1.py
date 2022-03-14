#Task1 
import sys

def main():
    
    try:
        n, m=map(int,input().split())
    except ValueError:
        print("Type Error!")
        sys.exit(1)

    str_string = "1"
    k=1

    while( ((k+m-1) % n) != 1 ):
        if( (( k+m-1) % n ) == 0 ):
            k=n
            str_string = str_string + str(k)
        else:
            k = (k + m - 1) % n
            str_string = str_string + str(k)

    print(str_string)

main()

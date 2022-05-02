#!/usr/bin/env python3
# Created by Marc Coffi
# Created in May 2022
# This program displays numbers from 1000 to 2000


def main():
    # Printing numbers from 1000 to 2000
    for counter in range(1000, 2001):
        # If the number is divisible by 5 then go to the next line
        if counter % 5 == 0 and counter != 1000:
            print()

        print(counter, end=" ")


if __name__ == "__main__":
    main()

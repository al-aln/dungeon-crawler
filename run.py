#!/usr/bin/env python3

import game
import sys
import curses


def main():
    # try:
    curses.wrapper(game.run)
    # except KeyboardInterrupt:
    #     print("\nCaught KeyboardInterrupt signal. Exiting...")
    #     sys.exit()


if __name__ == "__main__":
    main()

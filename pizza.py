#!/usr/bin/env python3
# Created by: Liam Fletcher
# Created on: Sep 2021
# This program calculates the cost of pizza

import constants

def main():
    # this function calculates the cost of a pizza

    # input
    diameter = int(input("Enter diameter of pizza you would "+"like (inch): "))
    # process
    sub_totaL = (constants.LABOR + constants.RENT + (diameter * constants.COST_PER_INCH))
    totaL = sub_totaL + (sub_totaL * constants.HST)
    # output
    print("The cost for a {0} inch pizza is ${1:,.2f}".format(diameter, totaL))
    print("\nDone.")


if __name__ == "__main__":
    main()
    
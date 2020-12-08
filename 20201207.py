import pandas as pd
import numpy as np
import math


# Fund Investment

def investment(y1, y2, y3):
    year1 = y1 - 2020
    year2 = y2 - 2020
    year3 = y3 - 2020
    # Calculate compound interest on annual investment
    year2020 = round(32000 * pow(1.04, year1 * 12), -2)
    year2021 = round(32000 * pow(1.04, year2 * 12), -2)
    year2022 = round(32000 * pow(1.04, year3 * 12), -2)
    profitability = year2020 + year2021 + year2022 - (32000 * 3)
    return profitability


Profit = investment(2023, 2022, 2021)
print(Profit)

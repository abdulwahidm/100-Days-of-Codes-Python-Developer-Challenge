"""
The names of files related to sales in a certain company was generated (fnames list):

[
    "01_sales.csv",
    "02_sales.csv",
    "03_sales.csv",
    "04_sales.csv",
    "05_sales.csv",
    "06_sales.csv",
    "07_sales.csv",
    "08_sales.csv",
    "09_sales.csv",
    "10_sales.csv",
    "11_sales.csv",
    "12_sales.csv",
    "13_sales.csv",
    "14_sales.csv",
    "15_sales.csv",
    "16_sales.csv",
    "17_sales.csv",
    "18_sales.csv",
    "19_sales.csv",
    "20_sales.csv",
    "21_sales.csv",
    "22_sales.csv",
    "23_sales.csv",
    "24_sales.csv",
]

The path to the working directory:

/eval

Using the built-in os module transform the names of the files (fnames list). 
Set the first 12 files to directory called 2020, the next 12 files to directory called 2021. 
Assign absolute paths to the paths variable (list).

In response, print each path as shown below.

Tip:

>>> help(os.path.join)
 
Help on function join in module ntpath:
 
join(path, *paths)
    # Join two (or more) paths.

Expected result:

/eval/2020/01_sales.csv
/eval/2020/02_sales.csv
/eval/2020/03_sales.csv
/eval/2020/04_sales.csv
/eval/2020/05_sales.csv
/eval/2020/06_sales.csv
/eval/2020/07_sales.csv
/eval/2020/08_sales.csv
/eval/2020/09_sales.csv
/eval/2020/10_sales.csv
/eval/2020/11_sales.csv
/eval/2020/12_sales.csv
/eval/2021/13_sales.csv
/eval/2021/14_sales.csv
/eval/2021/15_sales.csv
/eval/2021/16_sales.csv
/eval/2021/17_sales.csv
/eval/2021/18_sales.csv
/eval/2021/19_sales.csv
/eval/2021/20_sales.csv
/eval/2021/21_sales.csv
/eval/2021/22_sales.csv
/eval/2021/23_sales.csv
/eval/2021/24_sales.csv

"""

import os
 
 
fnames = [f"{str(i).zfill(2)}_sales.csv" for i in range(1, 25)]
paths = [
    os.path.join(os.getcwd(), '2020', fname)
    if idx < 12
    else os.path.join(os.getcwd(), '2021', fname)
    for idx, fname in enumerate(fnames)
]
 
for path in paths:
    print(path)

#!/usr/bin/env python
"""Extract relevant columns.
"""

import csv

with open('defcore.csv', 'r') as infile:
    reader = csv.reader(infile)
    read_iter = iter(reader)

    # Read past the 2 header lines
    read_iter.next()
    read_iter.next()

    rows = [[row[0]] + row[6:9] for row in read_iter]

    # Ignore the percentages at the bottom
    del rows[-1]

    # Add the spreadsheet row numbers
    for i, row in enumerate(rows, 3):
        row.insert(0, str(i))
    print(rows[0])
    rows[0][0] = 'Row'

    # Candidate Capabilities,TC Future Direction,Complete,Stable
    widths = []
    for i in range(len(rows[0])):
        widths.append(max(len(row[i])+2 for row in rows))

    fmt = '{0:>%d} {1:<%d} {2:^%d} {3:^%d} {4:^%d}' % tuple(widths)

    header = ' '.join('=' * wid for wid in widths)

    print(header)
    print(fmt.format(*rows[0]))
    print(header)
    for row in rows[1:]:
        print(fmt.format(*row))
    print(header)

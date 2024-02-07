#!/usr/bin/python3
"""Script to compute metrics from stdin"""

import sys

def print_stats(total_size, status_codes):
    """Print statistics"""
    print("File size: {}".format(total_size))
    for code, count in sorted(status_codes.items()):
        if count > 0:
            print("{}: {}".format(code, count))

def main():
    """Main function"""
    total_size = 0
    status_codes = {"200": 0, "301": 0, "400": 0, "401": 0,
                    "403": 0, "404": 0, "405": 0, "500": 0}
    line_count = 0

    try:
        for line in sys.stdin:
            line_count += 1
            data = line.split()
            if len(data) > 2:
                total_size += int(data[-1])
                code = data[-2]
                if code in status_codes:
                    status_codes[code] += 1

            if line_count % 10 == 0:
                print_stats(total_size, status_codes)

    except KeyboardInterrupt:
        print_stats(total_size, status_codes)
        raise
    except BrokenPipeError:
        pass

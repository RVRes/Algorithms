from typing import Callable, Generator

FILE_NAME = r'Temp/cities.csv'


def is_file_closed(file_name):
    # test if file is closed
    try:
        with open(FILE_NAME, "r"):
            print('File Closed')
    except IOError:
        print('File opened!')


# Example of data conveyor built using generators
def filter_file_using_genexp_conveyor(file_name: str, filter_function: Callable) -> Generator | None:
    # generator that receives strings from file
    lines = (line for line in open(file_name) if line.strip())

    # generator that gives list of fields from each string
    list_line = (list(map(str.strip, s.split(","))) for s in lines)

    # getting field names - the first raw
    cols = next(list_line)

    # creating generator of dicts with field names as keys and data as values.
    log_dicts = (dict(zip(cols, data)) for data in list_line)

    # generator that filters needed values
    finding = (
        f"{log['LatD']:>02}.{log['LatM']:>02}.{log['LatS']:>02}{log['NS']} "
        f"{log['LonD']:>02}.{log['LonM']:>02}.{log['LonS']:>02}{log['EW']} "
        f" {log['City']:>12}, {log['State']}"
        for log in log_dicts
        if filter_function(log)
    )
    return finding


# Example of common generator function
def filter_file_using_genereators(file_name: str, filter_function: Callable):
    with open(file_name) as f:
        cols = None
        for line in f:
            if not line.strip():
                continue
            else:
                list_line = map(str.strip, line.split(","))
                if not cols:
                    cols = list(list_line)
                    continue
                log = dict(zip(cols, list_line))
                if filter_function(log):
                    yield f"{log['LatD']:>02}.{log['LatM']:>02}.{log['LatS']:>02}{log['NS']} " \
                          f"{log['LonD']:>02}.{log['LonM']:>02}.{log['LonS']:>02}{log['EW']} " \
                          f" {log['City']:>12}, {log['State']}"


# field_names ['LatD', 'LatM', 'LatS', 'NS', 'LonD', 'LonM', 'LonS', 'EW', 'City', 'State']

print(*filter_file_using_genexp_conveyor(FILE_NAME, lambda x: 'Springfield' in x['City']), sep='\n')
is_file_closed(FILE_NAME)

print(*filter_file_using_genereators(FILE_NAME, lambda x: 'Springfield' in x['City']), sep='\n')
is_file_closed(FILE_NAME)

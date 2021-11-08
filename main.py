import sys

from Reader import *
from Utils import *


if __name__ == '__main__':
    if len(sys.argv) > 2:
        print(f'Too many arguments ({len(sys.argv)}). You need to specify only the file')
        for x in sys.argv:
            print(x)
        sys.exit()
    elif len(sys.argv) < 2:
        data = read_json("exemplu.json")
    else:
        data = read_json(sys.argv[1])
    for x in sys.argv:
        print(x)
    CloudCtx.check_number_of_entries()
    show_cloud_ctx_data(data)
    CloudCtx.check_number_of_entries()
    sort_by_current_health(data)
    show_cloud_ctx_data(data)
    CloudCtx.check_number_of_entries()
    sort_by_last_modified_date(data)
    show_cloud_ctx_data(data)

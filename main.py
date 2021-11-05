from Reader import *
import sys
def show_cloudCtx_data(data=[]):
    for x in data:
        print(x)
        print('*'*60)

def sort_by_last_modified_date(data=[]):
    return data.sort(key=lambda x: x.lastModified, reverse= True)
def sort_by_current_health(data=[]):
    return data.sort(key=lambda x: x.HealthInst.current_health, reverse= False)

def check_number_of_entries():
    print(f"There are {CloudCtx.count} entries of cloudCtx")

if __name__ == '__main__':
    if(len(sys.argv)>2):
        print('Too many arguments ('+str(len(sys.argv))+'). You need to specify only the file')
        for x in sys.argv:
            print(x)
        sys.exit()
    for x in sys.argv:
        print(x)
    data = read_json(sys.argv[1])
    check_number_of_entries()
    show_cloudCtx_data(data)
    check_number_of_entries()
    sort_by_current_health(data)
    show_cloudCtx_data(data)
    check_number_of_entries()
    sort_by_last_modified_date(data)
    show_cloudCtx_data(data)
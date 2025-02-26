import csv
import os


def get_obj_path():
    os.path.dirname(__file__).split('common')[0]

def read_csv(csvpath):
    with open(csvpath,mode='r',encoding='utf-8') as f:
        row=csv.reader(f)
        #raw = f.readline()
        data=[]
        for line in row:
            data.append(line)
        return data

# def write_csv(csvpath, data):
#     with open(csvpath, mode='w', encoding='utf-8') as f:
#         writes = csv.writer(f)
#         writes.writerow(data)

if __name__ == '__main__':
    raw1 = read_csv('../data/login_by_phone.csv')
    # write_csv('../data/output.csv', raw1)
    print("the records read from the csv file are - ", type(raw1), raw1)
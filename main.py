#!/usr/bin/python3
"""main module"""
from app_logic.csv_handler import get_csv_name
from app_logic.csv_handler import check_ref
from app_logic.csv_handler import read_from_csv
from app_logic.csv_handler import save_to_csv
from app_logic.csv_handler import update_csv
from app_logic.print_label import generate_label
from datetime import datetime

printer = 'Godex G500'
print('Welcome to Rework Tracker APP!!!!')
operator = input('Enter your Work Code!!!\n')
step = ''
option = input('Please Select an Option:\n1- Start Rework\n2- Finish rework\n')
if option == '1':
    step = 'start_rework'
    filename = get_csv_name(step)
    print(filename)
    ref = input('Enter a Valid Reference!!\n')
    ref_data = check_ref(ref)
    if ref_data is None:
        print('Reference Not Exist on Database!!!!')
        exit(-1)
    rework_card = input('Scan Rework Card\n')
    path = 'data/data_rework/{}'.format(filename)
    data = read_from_csv(path, rework_card)
    if data:
        print('harness already exist')
        exit(-1)
    fault = input('enter Fault Description\n')
    start_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    label_data = {}
    label_data['PROJECT'] = ref_data[0]
    label_data['REFERENCE'] = ref_data[1]
    label_data['OPERATOR'] = operator
    label_data['DATETIME'] = start_time
    label_data['REWORKDATA'] = '{};{};{}'.format(rework_card,
                                                 ref_data[1],
                                                 start_time)
    generate_label(rework_card, 'start', printer, label_data)
    save_to_csv(path, [operator,
                       ref_data[1],
                       ref_data[0],
                       rework_card,
                       fault,
                       start_time,
                       None,
                       None])
    exit(0)
elif option == '2':
    step = 'end_rework'
    filename = get_csv_name(step)
    print(filename)
    qr_code = input('Scan Rework Label Qr Code\n')
    reword_data = qr_code.split(';')
    ref_data = check_ref(reword_data[1])
    if ref_data is None:
        print('Reference Not Exist on Database!!!!')
        exit(-1)
    
    rework_card = reword_data[0]
    path = 'data/data_rework/{}'.format(filename)
    data = read_from_csv(path, rework_card)
    if data:
        print('harness already exist')
        exit(-1)
    fault = input('enter Fault Description\n')
    start_time = datetime.strptime(reword_data[2], "%Y-%m-%d %H:%M:%S")
    end_time = datetime.now()
    rework_time = end_time - start_time
    rework_time = rework_time.total_seconds() / 60
    save_to_csv(path,
                [operator,
                 ref_data[1],
                 ref_data[0],
                 rework_card,
                 fault,
                 start_time.strftime("%Y-%m-%d %H:%M:%S"),
                 end_time.strftime("%Y-%m-%d %H:%M:%S"),
                 round(rework_time, 2)])
    exit(0)

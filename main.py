#!/usr/bin/python3
"""main module"""
from app_logic.csv_handler import get_csv_name
from app_logic.csv_handler import check_ref
from app_logic.csv_handler import read_from_csv
from app_logic.csv_handler import save_to_csv
from app_logic.csv_handler import update_csv
from datetime import datetime

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
    save_to_csv(path, [operator,
                       ref_data[1],
                       ref_data[0],
                       rework_card,
                       fault,
                       start_time,
                       "",""])
    exit(0)
elif option == '2':
    step = 'end_rework'
    

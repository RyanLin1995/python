def make_car(manufacturers ,*car_models ,**selects):
    car_info={}
    car_info['manufacturer'] = manufacturers
    car_info['model'] = car_models

    for key ,value in selects.items():
        car_info[key] = value

    return car_info

car = make_car('honda','outback', 'suv', color = 'red' ,tow_package = 'True')
print(car)




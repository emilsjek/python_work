def make_car(manufacturer, model, **car_info):
    """Create car dictionary"""
    car_info['manufacturer'] = manufacturer
    car_info['model'] = model
    return car_info

sold_car = make_car('ford', 'focus', age='12 years old', colour='red')
print("Car being sold is:")
print(sold_car)
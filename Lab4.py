car_dict= {}
while True:
    make = input("Please enter the make of a car (enter 'done' when finished):")
    if make.lower() == 'done':
        break
    model = input("Please enter the model of a car:")
    car_dict[model] = make
query_model = input("Please enter the query model to query:")
if query_model in car_dict:
    print(f"The make of {query_model} is {car_dict[query_model]}")
else:
    print(f"No make found for the model {query_model}")

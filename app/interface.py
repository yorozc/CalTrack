from services.service import Service

user_service = Service()

user_food = input("Insert food to log: ")
user_calories = float(input("Insert calories: "))
user_food = user_service.create_food(user_food, user_calories)
user_log = user_service.create_log(user_food.id)
# call service to create food obj and store
# use food_id to create log object in service
print(f"Food {user_food.food_name} stored!")
print(f"Log {user_log} has been created")
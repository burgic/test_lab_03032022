# task_decider.py

def get_preferred_option(task_1 , task_2):

    # Scenario 1: Wash Dishes & Cook Dinner
    if task_1.description == "Wash Dishes" and task_2.description == "Cook Dinner":
        return task_1.description
    elif task_1.description == "Cook Dinner" and task_2.description == "Wash Dishes":
        return task_2.description

    # Scenario 2: Cook Dinner & Clean Windows
    elif task_1.description == "Cook Dinner" and task_2.description == "Clean Windows":
        return task_1.description
    elif task_1.description == "Clean Windows" and task_2.description == "Cook Dinner":
        return task_2.description

    # Scenario 3: Clean Windows & Wash Dishes
    elif task_1.description == "Clean Windows" and task_2.description == "Wash Dishes":
        return task_1.description
    elif task_1.description == "Wash Dishes" and task_2.description == "Clean Windows":
        return task_2.description

    else:
        return task_2.description
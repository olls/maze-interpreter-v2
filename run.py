import copy


def create_cars(maze, Car):
    cars = []
    for y, row in enumerate(maze):
        for x, cell in enumerate(row):
            if cell.name == 'start':
                cars.append(Car(0, x, y))

    return cars


def move_cars(maze, cars):
    after = copy.deepcopy(maze)

    for car in cars:

        # Check car's previous direction first.
        d = car.direction
        x, y = dir_to_pos(car, d)
        can_move_dir = check_pos(maze, car, x, y)

        # Check all directions.
        if not can_move_dir:
            for d in ['L', 'R', 'U', 'D']:
                x, y = dir_to_pos(car, d)
                can_move_dir = check_pos(maze, car, x, y)

                if can_move_dir: break

        # If car can move.
        if can_move_dir:
            car.x = x
            car.y = y
            car.direction = d

    return after, cars


def car_actions(maze, cars):
    after = copy.deepcopy(maze)

    for car in cars:
        if maze[car.y][car.y].name == 'wall':
            pass

    return after, cars


def dir_to_pos(car, direction):
    if direction in 'Ll':
        x = car.x - 1
        y = car.y
    elif direction in 'Rr':
        x = car.x + 1
        y = car.y
    elif direction in 'Uu':
        x = car.x
        y = car.y - 1
    elif direction in 'Dd':
        x = car.x
        y = car.y + 1

    return x, y


def check_pos(maze, car, x, y):
    return not maze[y][x].name == 'wall'

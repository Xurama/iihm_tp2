import random
import csv

SIZE_X_MAX = 1000
SIZE_Y_MAX = 800
DIR_NAME = 'generated_exp/'
SPACING = 5
all_density = (30, 60, 90)
all_size = (9, 12, 18)
max_density = max(all_density)
max_size = max(all_size)

def generate_targets(num_targets, max_target_size, min_spacing):
    all_targets = []
    for _ in range(num_targets):
        x = random.randint(0, SIZE_X_MAX)
        y = random.randint(0, SIZE_Y_MAX)
        target = (x, y, max_target_size)
        if not all_targets:
            all_targets.append(target)
        else:
            min_distance = min([(((x - t[0]) ** 2 + (y - t[1]) ** 2) ** 0.5) - max_target_size/2 for t in all_targets])
            if min_distance >= min_spacing:
                all_targets.append(target)
    return all_targets

def save_to_csv(filename, all_targets, density, change_size):
    with open(filename, "w", newline='\n') as f:
        writer = csv.writer(f)
        for target in all_targets[:density]:
            as_list = list(target)
            as_list[2] = change_size
            writer.writerow(as_list)


def create_csv(filename, all_targets, density, change_size):
    save_to_csv(filename, all_targets, density, change_size)


def create_all_files(min_spacing):
    all_targets = generate_targets(max_density, max_size, min_spacing)

    for density in all_density:
        for size in all_size:
            filename = "src_d_" + str(density) + '_s_' + str(size) + '.csv'
            create_csv(DIR_NAME + filename, all_targets, density, size)


if __name__ == '__main__':
    create_all_files(SPACING)

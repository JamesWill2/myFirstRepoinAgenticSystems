def read_numbers(file_name):
    numbers = []
    with open(file_name, "r") as file:
        for line in file:
            line = line.strip()
            if line:
                numbers.append(int(line))
    return numbers


def compute_results(numbers):
    total_count = len(numbers)
    total_sum = sum(numbers)
    average = total_sum / total_count if total_count > 0 else 0
    return total_count, total_sum, average


def log_results(log_file, count, total, avg):
    with open(log_file, "a") as log:
        log.write("File opened successfully\n")
        log.write(f"Read {count} numbers\n")
        log.write(f"Sum: {total}\n")
        log.write(f"Average: {avg}\n")
        log.write("Processing completed\n\n")


def main():
    input_file = "numbers.txt"
    log_file = "results.log"

    numbers = read_numbers(input_file)
    count, total, avg = compute_results(numbers)
    log_results(log_file, count, total, avg)


main()
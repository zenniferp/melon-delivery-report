def print_report(day, file_name):
    print("Day", day)
    the_file = open(file_name) #open Day's file
    for line in the_file: #go through every line in file
        line = line.rstrip() 
        words = line.split('|')

        melon, count, amount = words

        print("Delivered {} {}s for total of ${}".format(
            count, melon, amount))
    the_file.close()

print_report(1, "um-deliveries-20140519.txt")

print_report(2, "um-deliveries-20140520.txt")

print_report(3, "um-deliveries-20140521.txt")


def print_report(file_name):
    the_file = open(file_name) #open Day's file
    for line in the_file: #go through every line in file
        line = line.rstrip()
        words = line.split('|')

        melon = words[0]
        count = words[0]
        amount = words[0]

        print("Delivered {} {}s for total of ${}".format(
            count, melon, amount))
    the_file.close()

print("Day 1") #for day 1 
print_report(file_name = "um-deliveries-20140519.txt")

print("Day 2")
print_report(file_name = "um-deliveries-20140520.txt")

print("Day 3")
print_report(file_name = "um-deliveries-20140521.txt")


write_file = open('example1.txt', 'w')
write_file.write("aaaaa\nbbbbb\ncccccc\nddddd")
write_file.close()


read_file = open('example1.txt', 'r')
print(read_file.read())
read_file.close()

write_file = open('example1.txt', 'a')
write_file.write("\neeeeee\nfffffff")
write_file.close()

read_file = open('example1.txt', 'r')
print(read_file.read())
read_file.close()


print("\nTrick 1:")
write_file2 = open('example2.txt', 'w+')
write_file2.write("aaaaa\nbbbbb\ncccccc\nddddd")
write_file2.seek(0)
print(write_file2.read())
write_file2.close()

print("\nTrick 2:")
write_file3 = open('example2.txt', 'w+')
lines = ["aaa", "bbb", "ccc", "ddd"]
write_file3.writelines(lines)
write_file3.seek(0)
print(write_file3.read())
write_file3.close()


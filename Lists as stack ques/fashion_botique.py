<<<<<<< HEAD
box = [int(clothing) for clothing in input().split()]
rack_capacity = int(input())
num_racks = 0
current_rack = 0
while box:
    if current_rack + box[-1] <= rack_capacity:
        current_rack += box.pop()
    else:
        num_racks += 1
print(num_racks)
=======
box = [int(clothing) for clothing in input().split()]
rack_capacity = int(input())
num_racks = 0
current_rack = 0
while box:
    if current_rack + box[-1] <= rack_capacity:
        current_rack += box.pop()
    else:
        num_racks += 1
print(num_racks)
>>>>>>> 7e8381d627bc725b2be27de4d386243fc039cd29

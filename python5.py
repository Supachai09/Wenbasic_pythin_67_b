# สร้างลิสต์ของเลขจาก 21 ถึง 40
numbers = range(21, 41)

# แยกเลขคี่และเลขคู่
odd_numbers = [num for num in numbers if num % 2 != 0]
even_numbers = [num for num in numbers if num % 2 == 0]

# แสดงผลลัพธ์
print("เลขคี่:", odd_numbers)
print("เลขคู่:", even_numbers)

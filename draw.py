x = input("Enter your name :  ")
def greet(name):
    print("Hello, " + name + "! Welcome to the program.")

def menu():
    print("อยากกินอาหารอะไรดีครับ?")
    print("1. อาหารไทย")
    print("2. อาหารอังกฤษ")
    print("3. อาหารญี่ปุ่น")
    print("4. อาหารจีน")
    choice = input("กรุณาเลือกหมายเลข (1-4): ")
    handle_choice(choice)

def thai_food():
     print("menu อาหารไทย")
     print("1. ผัดไทย")
     print("2. ต้มยำกุ้ง")

def english_food():
     print("menu อาหารอังกฤษ")
     print("1. แฮมเบอร์เกอร์")
     print("2. ฟิชแอนด์ชิพส์")

def japanese_food():
     print("menu อาหารญี่ปุ่น")
     print("1. สูตร")
     print("2. ราเม็ง")
     

def chinese_food():
     print("menu อาหารจีน")
     print("1. ผัดไทย")
     print("2. ต้มยำกุ้ง")

def handle_choice(choice):
     if choice == "1":
          thai_food()
     elif choice == "2":
          english_food()
     elif choice == "3":
          japanese_food()
     elif choice == "4":
          chinese_food()
     else:
          print("ตัวเลือกไม่ถูกต้อง กรุณาเลือกหมายเลข 1-4")
def choose_food():
     food_choice = input("กรุณาเลือกหมายเลขอาหารที่คุณต้องการ: ")
     if food_choice == "1":
          print("คุณเลือกอาหารหมายเลข 1")
     elif food_choice == "2":
          print("คุณเลือกอาหารหมายเลข 2")
     else:
          print("ตัวเลือกไม่ถูกต้อง กรุณาเลือกหมายเลขอาหารที่ถูกต้อง")
def program():
    greet(x)
    menu()
    choose_food()
program()
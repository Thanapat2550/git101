name_friend = "ProGram"
def buit_program_name(name_data):
     i = 0
     name_bd = " "
     while i < len(name_data)-4:
          name_bd += name_data[i]
          i += 1
     return name_bd
def hbd(name):
     print(f"Happy birthday {name} !!")
     print("มีความสุขมากๆนะ ขอให้ได้เกรดดีๆ ไปเที่ยวกับเพื่อนๆ เยอะๆ")

hbd(buit_program_name(name_friend))





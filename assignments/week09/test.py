#โจทย์ 1: เครื่องคำนวณอย่างปลอดภัย
#เขียนโปรแกรมรับตัวเลข 2
#จำนวนและตัวดำเนินการ 1 ตัว ได้แก่ + - *
#/ และแสดงผลลัพธ์
#โปรแกรมต้องจัดการกรณีต่อไปนี้
#    ผู้ใช้กรอกข้อมูลที่ไม่ใช่ตัวเลข
#ValueError
 
#    ผู้ใช้เลือกตัวดำเนินการอื่นนอกเหนือจาก
#    + - * / raise ValueError
#    ผู้ใช้พยายามหารด้วยศูนย์
#ZeroDivisionError
#    โปรแกรมต้องแสดง จบการทำงาน
#เสมอด้วย finally
 
#ตัวอย่างผลลัพธ์ที่คาดหวัง
 
#ตัวเลขที่ 1: 10
#ตัวเลขที่ 2: 0



try:
    num1 = float(input("ตัวเลขที่ 1: "))
    num2 = float(input("ตัวเลขที่ 2: "))
 
    operator = input("เครื่องหมาย (+, -, *, /): ")
 
    result = 0
 
    if operator == "+":
        result = num1 + num2
    elif operator == "-":
        result = num1 - num2
    elif operator == "*":
        result = num1 * num2
    elif operator == "/":
        result = num1 / num2
    else:
        raise ValueError("เครื่องหมาย + - * / เท่านั้น")
 
    print(f"{num1} {operator} {num2} = {result}")
 
except ValueError:
    print("กรุณากรอกตัวเลขหรือเครื่องหมายให้ถูกต้อง")
 
except ZeroDivisionError:
    print("ไม่สามารถหารด้วยศูนย์ได้")
 
finally:
    print("จบการทำงานได้สมบูรณ์")
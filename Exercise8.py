username = input("Username ")
password = input("Password ")

if username=="Nut" and password=="123":
    print("Welcome Nut")
    print("Please Chose Your Food")
    food1 = int(input("ข้าวผัดกล่องละ 50 บาท ต้องการกี่กล่อง(หากไม่ต้องการซื้อพิมพ์ 0 ) "))
    print("--------------------------------------------------------")
    food2 = int(input("ไส้กรอกชิ้นละ 20 บาท ต้องการกี่ชิ้น(หากไม่ต้องการซื้อพิมพ์ 0 ) "))
    print("--------------------------------------------------------")
    food3 = int(input("ขนมปังชิ้นละ 10 บาท ต้องการกี่ชิ้น(หากไม่ต้องการซื้อพิมพ์ 0 ) "))
    print("--------------------------------------------------------")
    food4 = int(input("น้ำเปล่าขวด 10 บาท ต้องการกี่ขวด(หากไม่ต้องการซื้อพิมพ์ 0 ) "))
    print("--------------------------------------------------------")
    checkbill = int(input("ต้องการคิดเงินพิมพ์(1)>> "))
    if checkbill == 1:
        print("ทั้งหมด",(food1*50)+(food2*20)+(food3*10)+(food4*10), "บาท")
        print("--------------------------------------------------------")









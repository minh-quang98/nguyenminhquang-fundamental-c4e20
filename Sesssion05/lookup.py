diction = {
    "ns": "Nói",
    "h": "Giờ",
    "j": "gì",
    "hc": "học",
    "atsm": "ảo tưởng sức mạnh",
}
search = True
while search:
    print("*" * 50)
    for key in diction.keys():
        print(key, end="\t")
    print()
    nhap = input("Từ muốn tra: ")
    key = nhap
    if key in diction:
        print("Nghĩa: ", diction[key])
    else:
        print("Không tìm thấy")
        update = input("Bạn muốn thêm?(Y/N)").upper()
        if update == "Y":
            nghia = input("Nhập ý nghĩa: ")
            diction[nhap] = nghia
            print("Đã cập nhật")
            print("*" * 50)
        else:
            search = False 
        
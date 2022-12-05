import qrcode
import image

qr= qrcode.qrcode(
    version = 15, # 15 means the version of the qr code 
    box_size = 10, # size of the box of the qr code.
    border = 5 # it is the white part of image -- border in all four sides of the background

)

data= "https://www.youtube.com/watch?v=aCk-qE_WQJ4&list=PLbGui_ZYuhijd1hUF2VWiKt8FHNBa7kGb&index=117"

qr.add_data(data)
qr.make(fit =True)
img = qr.make_image(fill = "black", back_color = "white")
img.save("test.png")
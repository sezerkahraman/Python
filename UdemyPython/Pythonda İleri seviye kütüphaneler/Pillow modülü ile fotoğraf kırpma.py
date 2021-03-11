from PIL import Image
image=Image.open("zeynep ve ben.jpg")
degistir=(960,600)
image.thumbnail(degistir)
image.save("zeynepkucuk.jpg")

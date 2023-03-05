# project on qr code generator
# we use python language
# source code

pip install pyqrcode
pip install pypng
import pyqrcode as pyr
import pypng as pyg
print(" Enter any text" )
context = input()
url= pyr.create(context)
print("END")
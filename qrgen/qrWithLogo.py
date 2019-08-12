import pyqrcode
from PIL import Image

# Generate the qr code and save as png
qrobj = pyqrcode.create('https://www.dcpolicycenter.org')
with open('test.png', 'wb') as f:
    qrobj.png(f, scale=100)

# Now open that png image to put the logo
img = Image.open('test.png')

width, height = img.size

# How big the logo we want to put in the qr code png
logo_size = 500

# Open the logo image
logo = Image.open('black-favicon-01.jpg')


# Calculate xmin, ymin, xmax, ymax to put the logo
xmin = ymin = int((width / 2) - (logo_size ))
xmax = ymax = int((width / 2 ) + (logo_size ))

# resize the logo as calculated
logo = logo.resize((xmax - xmin, ymax - ymin))

# put the logo in the qr code
img.paste(logo, (xmin, ymin, xmax, ymax))

img.show()

quality_val = 100
img.save('test.jpg', 'JPEG', quality=quality_val)

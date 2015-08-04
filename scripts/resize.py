import Image, numpy
img = Image.open('../Registry/static/img/blue-marble.png')
premult = numpy.fromstring(img.tostring(), dtype=numpy.uint8)
alphaLayer = premult[3::4] / 255.0
premult[::4] *= alphaLayer
premult[1::4] *= alphaLayer
premult[2::4] *= alphaLayer
img = Image.fromstring("RGBA", img.size, premult.tostring())
img.resize((64,64), Image.ANTIALIAS).save('swordresize.png')


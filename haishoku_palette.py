from haishoku.haishoku import Haishoku



path = "examples\ex1.jpg"



palette = Haishoku.getPalette(path)
dominant = Haishoku.getDominant(path)
Haishoku.showPalette(path)
Haishoku.showDominant(path)
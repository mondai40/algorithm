import math

class QuadrilateralShape:
    def __init__(self, lineA, lineB, lineC, lineD):
        self.lineA = lineA
        self.lineB = lineB
        self.lineC = lineC
        self.lineD = lineD
        self.lineAC = Line(Point(self.lineA.startPoint.x, self.lineA.startPoint.y), Point(self.lineC.startPoint.x, self.lineC.startPoint.y))
        self.lineBD = Line(Point(self.lineB.startPoint.x, self.lineB.startPoint.y), Point(self.lineD.startPoint.x, self.lineD.startPoint.y))
        if not self.isValidCordinate(): raise ValueError("not a quadrilateral: Cordinate Error")
        
        self.degreeBAD = self.getAngle("BAD")
        self.degreeABC = self.getAngle("ABC")
        self.degreeADC = self.getAngle("ADC")
        self.degreeBCD = self.getAngle("BCD")
        self.degreeBAC = self.getAngle("BAC")
        self.degreeACD = self.getAngle("ACD")
        self.degreeACB = self.getAngle("ACB")
        self.degreeCAD = self.getAngle("CAD")
        if not self.isValidDegree(): raise ValueError("not a quadrilateral: Degree Error")

        self.parallelPair = self.getParallelPair(self.degreeBAC, self.degreeACD, self.degreeCAD, self.degreeACB)
        self.shapeType = self.getShapeType()

    def isValidCordinate(self):
        return not (
            self.lineA.getLength() == 0 or self.lineB.getLength() == 0 or self.lineC.getLength() == 0 or self.lineD.getLength() == 0 or
            self.lineAC.getLength() == 0 or self.lineBD.getLength() == 0
        )
    def isValidDegree(self):
        return not (
            self.degreeABC == 180 or self.degreeBCD == 180 or self.degreeADC == 180 or self.degreeBAD == 180 or
            self.degreeABC == 0 or self.degreeBCD == 0 or self.degreeADC == 0 or self.degreeBAD == 0
        )

    def getShapeType(self):
        # abdcadbc: both parallel, abdc: AB//CD, adbc: AD//BC
        if self.parallelPair == "abdcadbc":
            if self.degreeABC == 90:
                if self.lineA.getLength() == self.lineB.getLength():
                    return "square(正方形)"
                else:
                    return "rectangle(長方形)"
            else:
                if self.lineA.getLength() == self.lineB.getLength():
                    return "rhombus(ひし形)"
                else:
                    return "parallelogram(平行四辺形)"
        elif self.parallelPair == "abdc" or self.parallelPair == "adbc": 
            return 'trapezoid(台形)'
        else:
            if (
                (self.lineA.getLength == self.lineD.getLength() and self.lineB.getLength() == self.lineC.getLength()) or
                (self.lineA.getLength() == self.lineB.getLength() and self.lineD.getLength() == self.lineC.getLength())
            ): return "kite(凧)"
            else:
                return "other（その他）"
        
    def getPerimeter(self):
        return self.lineA.getLength() + self.lineB.getLength() + self.lineC.getLength() + self.lineD.getLength()
    
    def getAngle(self, angleString):
        # BAD, ABC, ADC, BCD
        if angleString == "BAD":
            l1 = self.lineBD.getLength()
            l2 = self.lineA.getLength()
            l3 = self.lineD.getLength()
        elif angleString == "ABC":
            l1 = self.lineAC.getLength()
            l2 = self.lineA.getLength()
            l3 = self.lineB.getLength()
        elif angleString == "ADC":
            l1 = self.lineAC.getLength()
            l2 = self.lineC.getLength()
            l3 = self.lineD.getLength()
        elif angleString == "BCD":
            l1 = self.lineBD.getLength()
            l2 = self.lineB.getLength()
            l3 = self.lineC.getLength()
        elif angleString == "BAC":
            l1 = self.lineB.getLength()
            l2 = self.lineA.getLength()
            l3 = self.lineAC.getLength()
        elif angleString == "ACD":
            l1 = self.lineD.getLength()
            l2 = self.lineC.getLength()
            l3 = self.lineAC.getLength()
        elif angleString == "ACB":
            l1 = self.lineA.getLength()
            l2 = self.lineB.getLength()
            l3 = self.lineAC.getLength()
        elif angleString == "CAD":
            l1 = self.lineC.getLength()
            l2 = self.lineD.getLength()
            l3 = self.lineAC.getLength()
        cosValue = round((l2 ** 2 + l3 ** 2 - l1 ** 2) / (2 * l2 * l3), 5)
        return round(math.degrees(math.acos(cosValue)))

    def getParallelPair(self, degreeBAC, degreeACD, degreeCAD, degreeACB):
        # abdcadbc: both parallel, abdc: AB//CD, adbc: AD//BC
        if degreeBAC == degreeACD and degreeCAD == degreeACB: return "abdcadbc"
        elif degreeBAC == degreeACD: return "abdc"
        elif degreeCAD == degreeACB: return "adbc"
        else: return "noparallel"

    def getArea(self):
        if (
            self.shapeType == "square(正方形)" or 
            self.shapeType == "rectangle(長方形)" or 
            self.shapeType == "parallelogram(平行四辺形)"
        ):
            height = round(self.lineB.getLength() * math.sin(math.radians(self.degreeBCD)), 5)
            return self.lineA.getLength() * height
        elif (self.shapeType == "rhombus(ひし形)" or self.shapeType == "kite(凧)"):
            return self.lineAC.getLength() * self.lineBD.getLength() / 2
        elif (self.shapeType == "trapezoid(台形)"):
            if self.parallelPair == "abdc":
                height = round(self.lineB.getLength() * math.sin(math.radians(self.degreeBCD)), 5)
                return ((self.lineA.getLength() + self.lineC.getLength()) * height) / 2 
            elif self.parallelPair == "adbc":
                height = round(self.lineA.getLength() * math.sin(math.radians(self.degreeABC)), 5)
                return ((self.lineB.getLength() + self.lineD.getLength()) * height) / 2 
        else:
            return "others"

    def draw(self):
        if self.degreeBAD != 45 and self.degreeBAD != 90 and self.degreeBAD != 135: print("can't draw this on a screen")

        elif self.shapeType == "square(正方形)" or self.shapeType == "rectangle(長方形)":
            # normal
            if self.lineA.startPoint.y == self.lineB.startPoint.y:
                height = round(self.lineB.getLength())
                width = round(self.lineA.getLength())
                self.draw_square1(height, width)
            # tilt 45, 235
            elif (
                (self.lineA.startPoint.y < self.lineB.startPoint.y and self.lineC.startPoint.y < self.lineB.startPoint.y) or
                (self.lineA.startPoint.y < self.lineD.startPoint.y and self.lineC.startPoint.y < self.lineD.startPoint.y)
            ):
                if self.lineA.getLength() >= self.lineB.getLength():
                    height = round(self.lineA.getLength())
                    width = round(self.lineB.getLength())
                else:
                    height = round(self.lineB.getLength())
                    width = round(self.lineA.getLength())
                self.draw_square2(height, width)          
            # normal
            elif self.lineA.startPoint.y == self.lineD.startPoint.y:
                height = round(self.lineA.getLength())
                width = round(self.lineB.getLength())
                print("　　" + "﹍　" * width + "　")
                for i in range(height):
                    print("｜　" + "　　" * width + "｜　")
                print("　　" + "﹉　" * width + "　")
            # tilt 135, 315
            elif (
                (self.lineA.startPoint.y > self.lineB.startPoint.y and self.lineA.startPoint.y > self.lineD.startPoint.y) or
                (self.lineC.startPoint.y > self.lineB.startPoint.y and self.lineC.startPoint.y > self.lineD.startPoint.y)
            ):
                if self.lineA.getLength() >= self.lineB.getLength():
                    height = round(self.lineA.getLength())
                    width = round(self.lineB.getLength())
                else:
                    height = round(self.lineB.getLength())
                    width = round(self.lineA.getLength())
                self.draw_square3(height, width)
            else:
                print("Something wrong")
        
        elif self.shapeType == "parallelogram(平行四辺形)" or self.shapeType == "rhombus(ひし形)":
            if self.degreeBAD == 45:
                if self.lineA.startPoint.y == self.lineB.startPoint.y or self.lineA.startPoint.y == self.lineD.startPoint.y:
                    height = round(abs(self.lineC.startPoint.y - self.lineA.startPoint.y))
                    if (
                        (self.lineA.startPoint.x < self.lineB.startPoint.x and self.lineA.startPoint.y < self.lineD.startPoint.y) or
                        (self.lineA.startPoint.x > self.lineB.startPoint.x and self.lineA.startPoint.y > self.lineD.startPoint.y)
                    ):
                        width = round(self.lineA.getLength())
                        self.draw_parallelogram1(height, width)
                    elif (                
                        (self.lineA.startPoint.x < self.lineD.startPoint.x and self.lineA.startPoint.y < self.lineB.startPoint.y) or
                        (self.lineA.startPoint.x > self.lineD.startPoint.x and self.lineA.startPoint.y > self.lineB.startPoint.y)
                    ):
                        width = round(self.lineD.getLength())
                        self.draw_parallelogram1(height, width)
                    elif (
                        (self.lineA.startPoint.x < self.lineD.startPoint.x and self.lineA.startPoint.y > self.lineB.startPoint.y) or
                        (self.lineA.startPoint.x > self.lineD.startPoint.x and self.lineA.startPoint.y < self.lineB.startPoint.y)
                    ):
                        width = round(self.lineD.getLength())
                        self.draw_parallelogram1(height, width)

                    elif (                
                        (self.lineA.startPoint.x < self.lineB.startPoint.x and self.lineA.startPoint.y > self.lineD.startPoint.y) or
                        (self.lineA.startPoint.x > self.lineB.startPoint.x and self.lineA.startPoint.y < self.lineD.startPoint.y)
                    ):
                        width = round(self.lineA.getLength())
                        self.draw_parallelogram1(height, width)
                if self.lineA.startPoint.x == self.lineB.startPoint.x or self.lineA.startPoint.x == self.lineD.startPoint.x:
                    height = round(abs(self.lineC.startPoint.x - self.lineA.startPoint.x))
                    if (
                        (self.lineA.startPoint.x < self.lineD.startPoint.x and self.lineA.startPoint.y > self.lineB.startPoint.y) or
                        (self.lineA.startPoint.x > self.lineD.startPoint.x and self.lineA.startPoint.y < self.lineB.startPoint.y)
                    ):
                        width = round(self.lineA.getLength())
                        if height <= width:
                            self.draw_parallelogram3_1(height, width)
                        else:
                            self.draw_parallelogram3_2(height, width)
                            
                    elif (                
                        (self.lineA.startPoint.x < self.lineB.startPoint.x and self.lineA.startPoint.y > self.lineD.startPoint.y) or
                        (self.lineA.startPoint.x > self.lineB.startPoint.x and self.lineA.startPoint.y < self.lineD.startPoint.y)
                    ):
                        width = round(self.lineD.getLength())
                        if height <= width:
                            self.draw_parallelogram3_1(height, width)
                        else:
                            self.draw_parallelogram3_2(height, width)

                    elif (
                        (self.lineA.startPoint.x > self.lineB.startPoint.x and self.lineA.startPoint.y > self.lineB.startPoint.y) or
                        (self.lineA.startPoint.x < self.lineB.startPoint.x and self.lineA.startPoint.y < self.lineB.startPoint.y)
                    ):
                        width = round(self.lineD.getLength())
                        if height <= width:
                            self.draw_parallelogram4_1(height, width)
                        else:
                            self.draw_parallelogram4_2(height, width)
                    elif (                
                        (self.lineA.startPoint.x > self.lineD.startPoint.x and self.lineA.startPoint.y > self.lineB.startPoint.y) or
                        (self.lineA.startPoint.x < self.lineD.startPoint.x and self.lineA.startPoint.y < self.lineB.startPoint.y)
                    ):
                        width = round(self.lineA.getLength())
                        if height <= width:
                            self.draw_parallelogram4_1(height, width)
                        else:
                            self.draw_parallelogram4_2(height, width)
            elif self.degreeBAD == 135:
                if self.lineA.startPoint.y == self.lineB.startPoint.y or self.lineA.startPoint.y == self.lineD.startPoint.y:
                    height = abs(self.lineC.startPoint.y - self.lineA.startPoint.y)
                    if (
                        (self.lineA.startPoint.x < self.lineB.startPoint.x and self.lineA.startPoint.y < self.lineD.startPoint.y) or
                        (self.lineA.startPoint.x > self.lineB.startPoint.x and self.lineA.startPoint.y > self.lineD.startPoint.y)
                    ):
                        width = round(self.lineA.getLength())
                        self.draw_parallelogram2(height, width)
                    elif (        
                        (self.lineA.startPoint.x < self.lineD.startPoint.x and self.lineA.startPoint.y < self.lineB.startPoint.y) or
                        (self.lineA.startPoint.x > self.lineD.startPoint.x and self.lineA.startPoint.y > self.lineB.startPoint.y)
                    ):
                        width = round(self.lineD.getLength())
                        self.draw_parallelogram2(height, width)
                    elif (
                        (self.lineA.startPoint.x < self.lineD.startPoint.x and self.lineA.startPoint.y > self.lineB.startPoint.y) or
                        (self.lineA.startPoint.x > self.lineD.startPoint.x and self.lineA.startPoint.y < self.lineB.startPoint.y)
                    ):
                        width = round(self.lineD.getLength())
                        self.draw_parallelogram1(height, width)
                    elif (
                        (self.lineA.startPoint.x < self.lineB.startPoint.x and self.lineA.startPoint.y > self.lineD.startPoint.y) or
                        (self.lineA.startPoint.x > self.lineB.startPoint.x and self.lineA.startPoint.y < self.lineD.startPoint.y)
                    ):
                        width = round(self.lineA.getLength())
                        self.draw_parallelogram1(height, width)
                if self.lineA.startPoint.x == self.lineB.startPoint.x or self.lineA.startPoint.x == self.lineD.startPoint.x:
                    height = round(abs(self.lineC.startPoint.x - self.lineA.startPoint.x))
                    if (
                        (self.lineA.startPoint.x < self.lineB.startPoint.x and self.lineA.startPoint.y < self.lineD.startPoint.y) or
                        (self.lineA.startPoint.x > self.lineB.startPoint.x and self.lineA.startPoint.y > self.lineD.startPoint.y)
                    ):
                        width = round(self.lineD.getLength())
                        if height <= width:
                            self.draw_parallelogram3_1(height, width)
                        else:
                            self.draw_parallelogram3_2(height, width)
                    elif (
                        (self.lineA.startPoint.x < self.lineD.startPoint.x and self.lineA.startPoint.y < self.lineB.startPoint.y) or
                        (self.lineA.startPoint.x > self.lineD.startPoint.x and self.lineA.startPoint.y > self.lineB.startPoint.y)

                    ):
                        width = round(self.lineA.getLength())
                        if height <= width:
                            self.draw_parallelogram3_1(height, width)
                        else:
                            self.draw_parallelogram3_2(height, width)
                    elif (
                        (self.lineA.startPoint.x < self.lineD.startPoint.x and self.lineA.startPoint.y > self.lineB.startPoint.y) or
                        (self.lineA.startPoint.x > self.lineD.startPoint.x and self.lineA.startPoint.y < self.lineB.startPoint.y)
                    ):
                        width = round(self.lineA.getLength())
                        if height <= width:
                            self.draw_parallelogram4_1(height, width)
                        else:
                            self.draw_parallelogram4_2(height, width)
                    elif (
                        (self.lineA.startPoint.x < self.lineB.startPoint.x and self.lineA.startPoint.y > self.lineD.startPoint.y) or
                        (self.lineA.startPoint.x > self.lineB.startPoint.x and self.lineA.startPoint.y < self.lineD.startPoint.y)
                    ):
                        width = round(self.lineD.getLength())
                        if height <= width:
                            self.draw_parallelogram4_1(height, width)
                        else:
                            self.draw_parallelogram4_2(height, width)

        elif self.shapeType == "trapezoid(台形)":
            if (
                self.degreeBAD != 45 and 
                self.degreeABC != 45 and 
                self.degreeBCD != 45 and 
                self.degreeADC != 45
            ): print("can't draw this on a screen")

            if self.parallelPair == "abdc":
                if self.degreeBAD == 45:
                    if self.degreeABC == 45:
                        if self.lineA.startPoint.y == self.lineB.startPoint.y:
                            height = round(abs(self.lineA.startPoint.y - self.lineC.startPoint.y))
                            longerSide = round(int(self.lineA.getLength()))
                            shorterSide = round(int(self.lineC.getLength()))
                            if self.lineA.startPoint.x < self.lineB.startPoint.x:
                                self.draw_trapezoid1(height, longerSide, shorterSide)
                            if self.lineA.startPoint.x > self.lineB.startPoint.x:
                                self.draw_trapezoid5(height, longerSide, shorterSide)
                        if self.lineA.startPoint.y == self.lineD.startPoint.y:
                            height = round(abs(self.lineA.startPoint.y - self.lineC.startPoint.y))
                            width = round(int(self.lineD.getLength()))
                            if self.lineA.startPoint.y > self.lineB.startPoint.y:
                                self.draw_trapezoid2(height, width)
                            if self.lineA.startPoint.y < self.lineB.startPoint.y:
                                self.draw_trapezoid6(height, width)
                        if self.lineA.startPoint.x == self.lineB.startPoint.x:
                            height = round(int(lineA.getLength()))
                            width = round(abs(self.lineC.startPoint.x - self.lineA.startPoint.x))
                            if self.lineA.startPoint.y > self.lineB.startPoint.y:
                                self.draw_trapezoid3(height, width)
                            if self.lineA.startPoint.y < self.lineB.startPoint.y:
                                self.draw_trapezoid7(height, width)
                        if self.lineA.startPoint.x == self.lineD.startPoint.x:
                            height = round(int(lineD.getLength()))
                            width = round(abs(self.lineC.startPoint.x - self.lineA.startPoint.x))
                            if self.lineA.startPoint.y > self.lineB.startPoint.y:
                                self.draw_trapezoid4(height, width)
                            if self.lineA.startPoint.y < self.lineB.startPoint.y:
                                self.draw_trapezoid8(height, width)
                    elif self.degreeABC == 90:
                        if self.lineA.startPoint.y == self.lineB.startPoint.y:
                            height = round(abs(self.lineA.startPoint.y - self.lineC.startPoint.y))
                            longerSide = round(int(self.lineA.getLength()))
                            shorterSide = round(int(self.lineC.getLength()))
                            if self.lineA.startPoint.x < self.lineB.startPoint.x:
                                self.draw_trapezoid9(height, longerSide, shorterSide)
                            if self.lineA.startPoint.x > self.lineB.startPoint.x:
                                self.draw_trapezoid13(height, longerSide, shorterSide)
                        if self.lineA.startPoint.y == self.lineD.startPoint.y:
                            height = round(abs(self.lineC.startPoint.y - self.lineA.startPoint.y))
                            width = round(int(self.lineD.getLength()))
                            vline = width // 2
                            if self.lineA.startPoint.x < self.lineB.startPoint.x:
                                self.draw_trapezoid10(height, width, vline)
                            if self.lineA.startPoint.x > self.lineB.startPoint.x:
                                self.draw_trapezoid14(height, width, vline)
                        if self.lineA.startPoint.x == self.lineB.startPoint.x:
                            height = round(int(lineA.getLength()))
                            width = round(abs(self.lineC.startPoint.x - self.lineA.startPoint.x))
                            if self.lineA.startPoint.y > self.lineB.startPoint.y:
                                self.draw_trapezoid11(height, width)
                            if self.lineA.startPoint.y < self.lineB.startPoint.y:
                                self.draw_trapezoid15(height, width)
                        if self.lineA.startPoint.x == self.lineD.startPoint.x:
                            height = round(abs(self.lineB.startPoint.x - self.lineA.startPoint.x))
                            width = round(int(lineD.getLength()))
                            vline = width // 2
                            print(height, width, vline)
                            if self.lineA.startPoint.y > self.lineB.startPoint.y:
                                self.draw_trapezoid12(height, width, vline)
                            if self.lineA.startPoint.y < self.lineB.startPoint.y:
                                self.draw_trapezoid16(height, width, vline)
                                
                elif self.degreeBAD == 90:                    
                    if self.degreeABC == 45:
                        if self.lineA.startPoint.y == self.lineB.startPoint.y:
                            height = round(abs(self.lineA.startPoint.y - self.lineC.startPoint.y))
                            longerSide = round(int(self.lineA.getLength()))
                            shorterSide = round(int(self.lineC.getLength()))
                            if (self.lineA.startPoint.x < self.lineC.startPoint.x and self.lineA.startPoint.y < self.lineC.startPoint.y):
                                self.draw_trapezoid17(height, longerSide, shorterSide)
                            elif (self.lineA.startPoint.x > self.lineC.startPoint.x and self.lineA.startPoint.y > self.lineC.startPoint.y):
                                self.draw_trapezoid21(height, longerSide, shorterSide)
                        elif self.lineB.startPoint.x == self.lineC.startPoint.x:
                            height = round(abs(self.lineC.startPoint.x - self.lineA.startPoint.x))
                            width = round(int(self.lineB.getLength()))
                            vline = width // 2
                            if (self.lineA.startPoint.x < self.lineB.startPoint.x and self.lineA.startPoint.y > self.lineB.startPoint.y):
                                self.draw_trapezoid18(height, width, vline)
                            elif (self.lineA.startPoint.x > self.lineB.startPoint.x and self.lineA.startPoint.y < self.lineB.startPoint.y):
                                self.draw_trapezoid22(height, width, vline)
                        elif self.lineA.startPoint.x == self.lineB.startPoint.x:
                            height = int(lineA.getLength())
                            width = int(lineD.getLength())
                            if (self.lineA.startPoint.x < self.lineC.startPoint.x and self.lineA.startPoint.y > self.lineC.startPoint.y):
                                self.draw_trapezoid19(height, width)
                            elif (self.lineA.startPoint.x > self.lineC.startPoint.x and self.lineA.startPoint.y < self.lineC.startPoint.y):
                                self.draw_trapezoid23(height, width)
                        elif self.lineB.startPoint.y == self.lineC.startPoint.y:
                            height = round(abs(self.lineC.startPoint.y - self.lineA.startPoint.y))
                            width = round(int(self.lineB.getLength()))
                            vline = width // 2
                            if (self.lineA.startPoint.x > self.lineB.startPoint.x and self.lineA.startPoint.y > self.lineB.startPoint.y):
                                self.draw_trapezoid20(height, width, vline)
                            elif (self.lineA.startPoint.x < self.lineB.startPoint.x and self.lineA.startPoint.y < self.lineB.startPoint.y):
                                print(height, width, vline)
                                self.draw_trapezoid24(height, width, vline)
                    elif self.degreeABC == 135:
                        if self.lineA.startPoint.y == self.lineB.startPoint.y:
                            height = round(abs(self.lineA.startPoint.y - self.lineC.startPoint.y))
                            longerSide = int(self.lineC.getLength())
                            shorterSide = int(self.lineA.getLength())
                            if self.lineA.startPoint.x < self.lineB.startPoint.x:
                                self.draw_trapezoid13(height, longerSide, shorterSide)
                            if self.lineA.startPoint.x > self.lineB.startPoint.x:
                                self.draw_trapezoid9(height, longerSide, shorterSide)
                        if self.lineB.startPoint.y == self.lineC.startPoint.y:
                            height = round(abs(self.lineC.startPoint.y - self.lineA.startPoint.y))
                            width = round(int(self.lineB.getLength()))
                            vline = width // 2
                            if self.lineA.startPoint.x < self.lineB.startPoint.x:
                                self.draw_trapezoid14(height, width, vline)
                            if self.lineA.startPoint.x > self.lineB.startPoint.x:
                                self.draw_trapezoid10(height, width, vline)
                        if self.lineA.startPoint.x == self.lineB.startPoint.x:
                            height = round(int(lineC.getLength()))
                            width = round(abs(self.lineC.startPoint.x - self.lineA.startPoint.x))
                            if self.lineA.startPoint.y > self.lineB.startPoint.y:
                                self.draw_trapezoid15(height, width)
                            if self.lineA.startPoint.y < self.lineB.startPoint.y:
                                self.draw_trapezoid11(height, width) 
                        if self.lineB.startPoint.x == self.lineC.startPoint.x:
                            height = round(abs(self.lineC.startPoint.x - self.lineD.startPoint.x))
                            width = round(int(lineB.getLength()))
                            vline = width // 2
                            if self.lineA.startPoint.y > self.lineB.startPoint.y:
                                self.draw_trapezoid16(height, width, vline)
                            if self.lineA.startPoint.y < self.lineB.startPoint.y:
                                self.draw_trapezoid12(height, width, vline)
                
                elif self.degreeBAD == 135:
                    if self.degreeABC == 90:
                        if self.lineA.startPoint.y == self.lineB.startPoint.y:
                            height = round(abs(self.lineA.startPoint.y - self.lineC.startPoint.y))
                            longerSide = round(int(self.lineC.getLength()))
                            shorterSide = round(int(self.lineA.getLength()))
                            if (self.lineA.startPoint.x < self.lineB.startPoint.x):
                                self.draw_trapezoid21(height, longerSide, shorterSide)
                            elif (self.lineA.startPoint.x > self.lineB.startPoint.x):
                                self.draw_trapezoid17(height, longerSide, shorterSide)
                        elif self.lineA.startPoint.x == self.lineD.startPoint.x:
                            height = round(abs(self.lineC.startPoint.x - self.lineA.startPoint.x))
                            width = round(int(self.lineD.getLength()))
                            vline = round(abs(self.lineC.startPoint.x - self.lineA.startPoint.x)) // 2
                            print(height, width)
                            if (self.lineA.startPoint.x < self.lineB.startPoint.x and self.lineA.startPoint.y < self.lineD.startPoint.y):
                                self.draw_trapezoid22(height, width, vline)
                            elif (self.lineA.startPoint.x > self.lineB.startPoint.x and self.lineA.startPoint.y < self.lineB.startPoint.y):
                                self.draw_trapezoid18(height, width, vline)
                        elif self.lineA.startPoint.x == self.lineB.startPoint.x:
                            height = int(lineC.getLength())
                            width = int(lineD.getLength())
                            if (self.lineA.startPoint.x < self.lineD.startPoint.x and self.lineA.startPoint.y > self.lineB.startPoint.y):
                                self.draw_trapezoid23(height, width)
                            elif (self.lineA.startPoint.x > self.lineD.startPoint.x and self.lineA.startPoint.y < self.lineB.startPoint.y):
                                self.draw_trapezoid19(height, width)
                        elif self.lineA.startPoint.y == self.lineD.startPoint.y:
                            height = round(abs(self.lineB.startPoint.y - self.lineA.startPoint.y))
                            width = round(int(self.lineD.getLength()))
                            vline = round(abs(self.lineC.startPoint.y - self.lineA.startPoint.y)) // 2
                            print(height, width)
                            if (self.lineA.startPoint.x < self.lineD.startPoint.x and self.lineA.startPoint.y > self.lineB.startPoint.y):
                                self.draw_trapezoid24(height, width, vline)
                            elif (self.lineA.startPoint.x > self.lineD.startPoint.x and self.lineA.startPoint.y < self.lineB.startPoint.y):
                                self.draw_trapezoid20(height, width, vline)
                    elif self.degreeABC == 135:
                        if self.lineA.startPoint.y == self.lineB.startPoint.y:
                            height = round(abs(self.lineA.startPoint.y - self.lineC.startPoint.y))
                            longerSide = round(int(self.lineC.getLength()))
                            shorterSide = round(int(self.lineA.getLength()))
                            if self.lineA.startPoint.x < self.lineB.startPoint.x:
                                self.draw_trapezoid5(height, longerSide, shorterSide)
                            if self.lineA.startPoint.x > self.lineB.startPoint.x:
                                self.draw_trapezoid1(height, longerSide, shorterSide)
                        if self.lineA.startPoint.x == self.lineD.startPoint.x:
                            height = round(abs(self.lineA.startPoint.y - self.lineC.startPoint.y))
                            width = round(int(self.lineB.getLength()))
                            if self.lineA.startPoint.y > self.lineB.startPoint.y:
                                self.draw_trapezoid6(height, width)
                            if self.lineA.startPoint.y < self.lineB.startPoint.y:
                                self.draw_trapezoid2(height, width)
                        if self.lineA.startPoint.x == self.lineB.startPoint.x:
                            height = round(int(lineC.getLength()))
                            width = round(abs(self.lineC.startPoint.x - self.lineA.startPoint.x))
                            if self.lineA.startPoint.y > self.lineB.startPoint.y:
                                self.draw_trapezoid7(height, width)
                            if self.lineA.startPoint.y < self.lineB.startPoint.y:
                                self.draw_trapezoid3(height, width)
                        if self.lineA.startPoint.y == self.lineD.startPoint.y:
                            height = round(int(lineD.getLength()))
                            width = round(abs(self.lineC.startPoint.x - self.lineA.startPoint.x))
                            if self.lineA.startPoint.y > self.lineB.startPoint.y:
                                self.draw_trapezoid8(height, width)
                            if self.lineA.startPoint.y < self.lineB.startPoint.y:
                                self.draw_trapezoid4(height, width)
                    
            if self.parallelPair == "adbc":
                if self.degreeBAD == 45:
                    if self.degreeADC == 45:
                        if self.lineA.startPoint.y == self.lineD.startPoint.y:
                            height = round(abs(self.lineA.startPoint.y - self.lineC.startPoint.y))
                            longerSide = round(int(self.lineD.getLength()))
                            shorterSide = round(int(self.lineB.getLength()))
                            if self.lineA.startPoint.x < self.lineD.startPoint.x:
                                self.draw_trapezoid1(height, longerSide, shorterSide)
                            if self.lineA.startPoint.x > self.lineD.startPoint.x:
                                self.draw_trapezoid5(height, longerSide, shorterSide)
                        if self.lineA.startPoint.y == self.lineB.startPoint.y:
                            height = round(abs(self.lineA.startPoint.y - self.lineC.startPoint.y))
                            width = round(int(self.lineB.getLength()))
                            if self.lineA.startPoint.y > self.lineD.startPoint.y:
                                self.draw_trapezoid2(height, width)
                            if self.lineA.startPoint.y < self.lineD.startPoint.y:
                                self.draw_trapezoid6(height, width)
                        if self.lineA.startPoint.x == self.lineD.startPoint.x:
                            height = round(int(lineD.getLength()))
                            width = round(abs(self.lineC.startPoint.x - self.lineA.startPoint.x))
                            if self.lineA.startPoint.y > self.lineD.startPoint.y:
                                self.draw_trapezoid3(height, width)
                            if self.lineA.startPoint.y < self.lineD.startPoint.y:
                                self.draw_trapezoid7(height, width)
                        if self.lineA.startPoint.x == self.lineB.startPoint.x:
                            height = round(int(lineA.getLength()))
                            width = round(abs(self.lineC.startPoint.x - self.lineA.startPoint.x))
                            if self.lineA.startPoint.y > self.lineD.startPoint.y:
                                self.draw_trapezoid4(height, width)
                            if self.lineA.startPoint.y < self.lineD.startPoint.y:
                                self.draw_trapezoid8(height, width)
                    elif self.degreeADC == 90:
                        if self.lineA.startPoint.y == self.lineD.startPoint.y:
                            height = round(abs(self.lineA.startPoint.y - self.lineC.startPoint.y))
                            longerSide = round(int(self.lineD.getLength()))
                            shorterSide = round(int(self.lineB.getLength()))
                            if self.lineA.startPoint.x < self.lineD.startPoint.x:
                                self.draw_trapezoid9(height, longerSide, shorterSide)
                            if self.lineA.startPoint.x > self.lineD.startPoint.x:
                                self.draw_trapezoid13(height, longerSide, shorterSide)
                        if self.lineA.startPoint.y == self.lineB.startPoint.y:
                            height = round(abs(self.lineC.startPoint.y - self.lineA.startPoint.y))
                            width = round(int(self.lineA.getLength()))
                            vline = width // 2
                            if self.lineA.startPoint.x < self.lineD.startPoint.x:
                                self.draw_trapezoid10(height, width, vline)
                            if self.lineA.startPoint.x > self.lineD.startPoint.x:
                                self.draw_trapezoid14(height, width, vline)
                        if self.lineA.startPoint.x == self.lineD.startPoint.x:
                            height = round(int(lineD.getLength()))
                            width = round(abs(self.lineC.startPoint.x - self.lineA.startPoint.x))
                            if self.lineA.startPoint.y > self.lineD.startPoint.y:
                                self.draw_trapezoid11(height, width)
                            if self.lineA.startPoint.y < self.lineD.startPoint.y:
                                self.draw_trapezoid15(height, width)
                        if self.lineA.startPoint.x == self.lineB.startPoint.x:
                            height = round(abs(self.lineD.startPoint.x - self.lineA.startPoint.x))
                            width = round(int(lineA.getLength()))
                            vline = width // 2
                            print(height, width, vline)
                            if self.lineA.startPoint.y > self.lineB.startPoint.y:
                                self.draw_trapezoid12(height, width, vline)
                            if self.lineA.startPoint.y < self.lineB.startPoint.y:
                                self.draw_trapezoid16(height, width, vline)
                                
                elif self.degreeBAD == 90:                    
                    if self.degreeADC == 45:
                        if self.lineA.startPoint.y == self.lineD.startPoint.y:
                            height = round(abs(self.lineA.startPoint.y - self.lineC.startPoint.y))
                            longerSide = round(int(self.lineD.getLength()))
                            shorterSide = round(int(self.lineB.getLength()))
                            if (self.lineA.startPoint.x < self.lineC.startPoint.x and self.lineA.startPoint.y < self.lineC.startPoint.y):
                                self.draw_trapezoid17(height, longerSide, shorterSide)
                            elif (self.lineA.startPoint.x > self.lineC.startPoint.x and self.lineA.startPoint.y > self.lineC.startPoint.y):
                                self.draw_trapezoid21(height, longerSide, shorterSide)
                        elif self.lineC.startPoint.x == self.lineD.startPoint.x:
                            height = round(abs(self.lineC.startPoint.x - self.lineA.startPoint.x))
                            width = round(int(self.lineC.getLength()))
                            vline = width // 2
                            if (self.lineA.startPoint.x < self.lineD.startPoint.x and self.lineA.startPoint.y > self.lineD.startPoint.y):
                                self.draw_trapezoid18(height, width, vline)
                            elif (self.lineA.startPoint.x > self.lineD.startPoint.x and self.lineA.startPoint.y < self.lineD.startPoint.y):
                                self.draw_trapezoid22(height, width, vline)
                        elif self.lineA.startPoint.x == self.lineD.startPoint.x:
                            height = int(lineD.getLength())
                            width = int(lineA.getLength())
                            if (self.lineA.startPoint.x < self.lineC.startPoint.x and self.lineA.startPoint.y > self.lineC.startPoint.y):
                                self.draw_trapezoid19(height, width)
                            elif (self.lineA.startPoint.x > self.lineC.startPoint.x and self.lineA.startPoint.y < self.lineC.startPoint.y):
                                self.draw_trapezoid23(height, width)
                        elif self.lineC.startPoint.y == self.lineD.startPoint.y:
                            height = round(abs(self.lineC.startPoint.y - self.lineA.startPoint.y))
                            width = round(int(self.lineC.getLength()))
                            vline = width // 2
                            if (self.lineA.startPoint.x > self.lineD.startPoint.x and self.lineA.startPoint.y > self.lineD.startPoint.y):
                                self.draw_trapezoid20(height, width, vline)
                            elif (self.lineA.startPoint.x < self.lineD.startPoint.x and self.lineA.startPoint.y < self.lineD.startPoint.y):
                                self.draw_trapezoid24(height, width, vline)
                    elif self.degreeADC == 135:
                        if self.lineA.startPoint.y == self.lineD.startPoint.y:
                            height = round(abs(self.lineA.startPoint.y - self.lineC.startPoint.y))
                            longerSide = int(self.lineB.getLength())
                            shorterSide = int(self.lineD.getLength())
                            if self.lineA.startPoint.x < self.lineD.startPoint.x:
                                self.draw_trapezoid13(height, longerSide, shorterSide)
                            if self.lineA.startPoint.x > self.lineD.startPoint.x:
                                self.draw_trapezoid9(height, longerSide, shorterSide)
                        if self.lineC.startPoint.y == self.lineD.startPoint.y:
                            height = round(abs(self.lineC.startPoint.y - self.lineA.startPoint.y))
                            width = round(int(self.lineC.getLength()))
                            vline = width // 2
                            if self.lineA.startPoint.x < self.lineD.startPoint.x:
                                self.draw_trapezoid14(height, width, vline)
                            if self.lineA.startPoint.x > self.lineD.startPoint.x:
                                self.draw_trapezoid10(height, width, vline)
                        if self.lineA.startPoint.x == self.lineD.startPoint.x:
                            height = round(int(lineB.getLength()))
                            width = round(abs(self.lineC.startPoint.x - self.lineA.startPoint.x))
                            if self.lineA.startPoint.y > self.lineD.startPoint.y:
                                self.draw_trapezoid15(height, width)
                            if self.lineA.startPoint.y < self.lineD.startPoint.y:
                                self.draw_trapezoid11(height, width) 
                        if self.lineC.startPoint.x == self.lineD.startPoint.x:
                            height = round(abs(self.lineA.startPoint.x - self.lineD.startPoint.x))
                            width = round(int(lineC.getLength()))
                            vline = width // 2
                            if self.lineA.startPoint.y > self.lineD.startPoint.y:
                                self.draw_trapezoid16(height, width, vline)
                            if self.lineA.startPoint.y < self.lineD.startPoint.y:
                                self.draw_trapezoid12(height, width, vline)
                
                elif self.degreeBAD == 135:
                    if self.degreeADC == 90:
                        if self.lineA.startPoint.y == self.lineD.startPoint.y:
                            height = round(abs(self.lineA.startPoint.y - self.lineC.startPoint.y))
                            longerSide = round(int(self.lineB.getLength()))
                            shorterSide = round(int(self.lineD.getLength()))
                            if (self.lineA.startPoint.x < self.lineD.startPoint.x):
                                self.draw_trapezoid21(height, longerSide, shorterSide)
                            elif (self.lineA.startPoint.x > self.lineD.startPoint.x):
                                self.draw_trapezoid17(height, longerSide, shorterSide)
                        elif self.lineA.startPoint.x == self.lineB.startPoint.x:
                            height = round(abs(self.lineC.startPoint.x - self.lineA.startPoint.x))
                            width = round(int(self.lineD.getLength()))
                            vline = width // 2
                            print(height, width, vline)
                            if (self.lineA.startPoint.x < self.lineD.startPoint.x and self.lineA.startPoint.y < self.lineB.startPoint.y):
                                self.draw_trapezoid22(height, width, vline)
                            elif (self.lineA.startPoint.x > self.lineD.startPoint.x and self.lineA.startPoint.y > self.lineB.startPoint.y):
                                self.draw_trapezoid18(height, width, vline)
                        elif self.lineA.startPoint.x == self.lineD.startPoint.x:
                            height = int(lineB.getLength())
                            width = int(lineD.getLength())
                            if (self.lineA.startPoint.x < self.lineB.startPoint.x and self.lineA.startPoint.y > self.lineD.startPoint.y):
                                self.draw_trapezoid23(height, width)
                            elif (self.lineA.startPoint.x > self.lineB.startPoint.x and self.lineA.startPoint.y < self.lineD.startPoint.y):
                                self.draw_trapezoid19(height, width)
                        elif self.lineA.startPoint.y == self.lineB.startPoint.y:
                            height = round(abs(self.lineD.startPoint.y - self.lineA.startPoint.y))
                            width = round(int(self.lineA.getLength()))
                            vline = width // 2
                            if (self.lineA.startPoint.x < self.lineB.startPoint.x and self.lineA.startPoint.y > self.lineD.startPoint.y):
                                self.draw_trapezoid24(height, width, vline)
                            elif (self.lineA.startPoint.x > self.lineB.startPoint.x and self.lineA.startPoint.y < self.lineD.startPoint.y):
                                self.draw_trapezoid20(height, width, vline)
                    elif self.degreeADC == 135:
                        if self.lineA.startPoint.y == self.lineD.startPoint.y:
                            height = round(abs(self.lineA.startPoint.y - self.lineC.startPoint.y))
                            longerSide = round(int(self.lineB.getLength()))
                            shorterSide = round(int(self.lineD.getLength()))
                            if self.lineA.startPoint.x < self.lineD.startPoint.x:
                                self.draw_trapezoid5(height, longerSide, shorterSide)
                            if self.lineA.startPoint.x > self.lineD.startPoint.x:
                                self.draw_trapezoid1(height, longerSide, shorterSide)
                        if self.lineA.startPoint.x == self.lineB.startPoint.x:
                            height = round(abs(self.lineA.startPoint.y - self.lineC.startPoint.y))
                            width = round(int(self.lineA.getLength()))
                            if self.lineA.startPoint.y > self.lineD.startPoint.y:
                                self.draw_trapezoid6(height, width)
                            if self.lineA.startPoint.y < self.lineD.startPoint.y:
                                self.draw_trapezoid2(height, width)
                        if self.lineA.startPoint.x == self.lineD.startPoint.x:
                            height = round(int(lineB.getLength()))
                            width = round(abs(self.lineC.startPoint.x - self.lineA.startPoint.x))
                            if self.lineA.startPoint.y > self.lineD.startPoint.y:
                                self.draw_trapezoid7(height, width)
                            if self.lineA.startPoint.y < self.lineD.startPoint.y:
                                self.draw_trapezoid3(height, width)
                        if self.lineA.startPoint.y == self.lineB.startPoint.y:
                            height = round(abs(self.lineA.startPoint.x - self.lineC.startPoint.x))
                            width = round(int(lineA.getLength()))
                            if self.lineA.startPoint.y > self.lineD.startPoint.y:
                                self.draw_trapezoid8(height, width)
                            if self.lineA.startPoint.y < self.lineD.startPoint.y:
                                print("here", height, width)
                                self.draw_trapezoid4(height, width)
          

    def draw_square1(self, height, width):
        print("　　" + "﹍　" * width + "　")
        for i in range(height):
            print("｜　" + "　　" * width + "｜　")
        print("　　" + "﹉　" * width + "　")
    def draw_square2(self, height, width):
        for i in range(width):
            print("　　" * (width - (i + 1)) + "／　" + "　　" * (i * 2) + "＼　")
        for i in range(height - width):
            print("　　" * i + "＼　" + "　　" * (width + 2) + "＼　")
        for i in range(width):
            print("　　" * (height - width + i) + "＼　" + "　　" * ((width - (i + 1)) * 2) + "／　")
    def draw_square3(self, height, width):
        for i in range(width):
            print("　　" * (height - (i + 1)) + "／　" + "　　" * (i * 2) + "＼　")
        for i in range(height - width):
            print("　　" * (height -  (width + i + 1)) + "／　" + "　　" * (width + 2) + "／　")
        for i in range(width):
            print("　　" * i + "＼　" + "　　" * ((width - (i + 1)) * 2) + "／　")
    
    def draw_parallelogram1(self, height, width):
        print("　　" * height + "﹍　" * width)
        for i in range(height):
            print("　　" * (height - (i + 1)) + "／　" + "　　" * (width - 1) + "／　")
        print("﹉　" * width)
    def draw_parallelogram2(self, height, width):
        print("﹍　" * width)
        for i in range(height):
            print("　　" * i + "＼　" + "　　" * (width - 1) + "＼　")
        print("　　" * height + "﹉　" * width)
    def draw_parallelogram3_1(self, height, width):
        for i in range(width):
            print("｜　" +  "　　" * i + "＼　")
        for i in range(height - width):
            print("｜　" + "　　" * width + "｜　")
        for i in range(width):
            print("　　" * (i + 1) + "＼　" + "　　" * (width - (i + 1)) + "｜　")
    def draw_parallelogram3_2(self, height, width):
        for i in range(width):
            print("｜　" +  "　　" * i + "＼　")
        for i in range(height):
            print("　　" + "　　" * i + "＼　" + "　　" * (width - 1) + "＼　")
        for i in range(width):
            print("　　" + "　　" * (height + i) + "＼　" + "　　" * (width - (i + 1)) + "｜　")
    def draw_parallelogram4_1(self, height, width):
        for i in range(height):
            print("　　" + "　　" * (height - (i + 1)) + "／　" + "　　" * i + "｜　")
        for i in range(width - height):
            print("｜　" + "　　" * height + "｜　")
        for i in range(height):
            print("｜　" + "　　" * (height - (i + 1)) + "／　")
    def draw_parallelogram4_2(self, height, width):
        for i in range(width):
            print("　　" + "　　" * (height - i + 1) + "／　" + "　　" * i + "｜　")
        for i in range(height):
            print("　　" + "　　" * (height - (i + 1)) + "／　" + "　　" * (width - 1) + "／　")
        for i in range(width):
            print("｜　" + "　　" * (width - (i + 1)) + "／　")

    def draw_trapezoid1(self, height, longerSide, shorterSide):
        print("　　" * ((longerSide - shorterSide) // 2) + "﹍　" * shorterSide)
        for i in range(height):
            print("　　" * (height - (i + 1)) + "／　" + "　　" * (shorterSide + i * 2) + "＼　")
        print("﹉　" * longerSide)
    def draw_trapezoid2(self, height, width):
        print("﹍　" * width)
        for i in range(height):
            print("　　" * i + "＼　" + "　　" * (width - 1) + "＼　")
        for i in range(width):
            print("　　" * (height + i) + "＼　" + "　　" * (width - (i + 1)) + "｜　")
    def draw_trapezoid3(self, height, width):
        for i in range(width):
            print("｜　" +  "　　" * i + "＼　")
        for i in range(height - (width * 2)):
            print("｜　" + "　　" * width + "｜　")
        for i in range(width):
            print("｜　" + "　　" * (width - (i + 1)) + "／　")
    def draw_trapezoid4(self, height, width):
        for i in range(width):
            print("　　" * (width * 2 - (i + 1)) + "／　" + "　　" * i + "｜　")
        for i in range(height):
            print("　　" * (height - (i + 1)) + "／　" + "　　" * (width - 1) + "／　")
        print("﹉　" * width)
    def draw_trapezoid5(self, height, longerSide, shorterSide):
        print("﹍　" * longerSide)
        for i in range(height):
            print("　　" * i + "＼　" + "　　" * (longerSide - (i * 2 + 2)) + "／　")
        print("　　" * ((longerSide - shorterSide) // 2) + "﹉　" * shorterSide)
    def draw_trapezoid6(self, height, width):
        for i in range(width):
            print("｜　" +  "　　" * i + "＼　")
        for i in range(height):
            print("　　" * (i + 1) + "＼　" + "　　" * (width - 1) + "＼　")
        print("　　" * (height + 1) + "﹉　" * width)
    def draw_trapezoid7(self, height, width):
        for i in range(width):
            print("　　" * (width - i) + "／　" + "　　" * i + "｜　")
        for i in range(height - (width * 2)):
            print("｜　" + "　　" * width + "｜　")
        for i in range(width):
            print("　　" * (i + 1) + "＼　" + "　　" * (width - (i + 1)) + "｜　")
    def draw_trapezoid8(self, height, width):
        print("　　" * (height + 1) + "﹍　" * width)
        for i in range(height):
            print("　　" * (height - i) + "／　" + "　　" * (width - 1) + "／　")
        for i in range(width):
            print("｜　" + "　　" * (width - (i + 1)) + "／　")
    def draw_trapezoid9(self, height, longerSide, shorterSide):
        print("　　" * (longerSide - shorterSide) + "﹍　" * shorterSide)
        for i in range(height):
            print("　　" * (height - (i + 1)) + "／　" + "　　" * (shorterSide + i) + "｜　")
        print("﹉　" * longerSide)
    def draw_trapezoid10(self, height, width, vline):
        print("﹍　" * width)
        for i in range(height):
            print("　　" * i + "＼　" + "　　" * (width - 1) + "＼　")
        for i in range(vline):
            print("　　" * (width + i) + "＼　" + "　　" * (vline - (i * 2)) + "／　")
    def draw_trapezoid11(self, height, width):
        for i in range(width):
            print("｜　" +  "　　" * i + "＼　")
        for i in range(height - width):
            print("｜　" + "　　" * width + "｜　")
        print("　　" + "﹉　" * width + "　")    
    def draw_trapezoid12(self, height, width, vline):
        for i in range(width):
            print("　　" * ((height) - (i + 1)) + "／　" + "　　" * i + "｜　")
        for i in range(height - width):
            print("　　" * (height - width - (i + 1)) + "／　" + "　　" * (width - 1) + "／　")
        for i in range(vline):
            print("　　" * i + "＼　" + "　　" * (width - (i * 2 + 2)) + "／　")
    def draw_trapezoid13(self, height, longerSide, shorterSide):
        print("　　" + "﹍　" * longerSide)
        for i in range(height):
            print("｜　" + "　　" * (longerSide - (i + 1)) + "／　")
        print("　　" + "﹉　" * shorterSide)
    def draw_trapezoid14(self, height, width, vline):
        for i in range(vline):
            print("　　" * (vline - (i + 1)) + "／　" + "　　" * (i * 2) + "＼　")
        for i in range(height):
            print("　　" * i + "＼　" + "　　" * (width - 1) + "＼　")
        print("　　" * height + "﹉　" * width)
    def draw_trapezoid15(self, height, width):
        print("　　" + "﹍　" * width + "　")
        for i in range(height - width):
            print("｜　" + "　　" * width + "｜　")
        for i in range(width):
            print("　　" + "　　" * i + "＼　" +  "　　" * (width - (i + 1)) + "｜　")
    def draw_trapezoid16(self, height, width, vline):
        for i in range(vline):
            print("　　" + "　　" * ((height - width) + vline - (i + 1)) + "／　" + "　　" * (i * 2) + "＼　")
        for i in range(height - width):
            print("　　" + "　　" * (height - width - (i + 1)) + "／　" + "　　" * (width - 1) + "／　")
        for i in range(width):
            print("｜　" + "　　" * (width - (i + 1)) + "／　")
    def draw_trapezoid17(self, height, longerSide, shorterSide):
        print("　　" + "﹍　" * shorterSide)
        for i in range(height):
            print("｜　" + "　　" * (shorterSide + i) + "＼　")
        print("　　" + "﹉　" * longerSide)
    def draw_trapezoid18(self, height, width, vline):
        for i in range(vline):
            print("　　" * (vline - (i + 1)) + "／　" + "　　" * (i * 2) + "＼　")
        for i in range(height - width):
            print("　　" * i + "＼　" + "　　" * (width - 1) + "＼　")
        for i in range(width):
            print("　　" * (height - width + i) + "＼　" + "　　" * (width - (i + 1)) + "｜　")
    def draw_trapezoid19(self, height, width):
        print("　　" + "﹍　" * width + "　")
        for i in range(height - width):
            print("｜　" + "　　" * width + "｜　")
        for i in range(width):
            print("｜　" + "　　" * (width - (i + 1)) + "／　")
    def draw_trapezoid20(self, height, width, vline):
        for i in range(vline):
            print("　　" * (height + vline - (i + 1)) + "／　" + "　　" * (i * 2) + "＼　")
        for i in range(height):
            print("　　" * (height - (i + 1)) + "／　" + "　　" * (width - 1) + "／　")
        print("﹉　" * width)
    def draw_trapezoid21(self, height, longerSide, shorterSide):
        print("﹍　" * longerSide)
        for i in range(height):
            print("　　" * i + "＼　" + "　　" * (longerSide - (i + 1)) + "｜　")
        print("　　" * (longerSide - shorterSide) + "﹉　" * shorterSide)
    def draw_trapezoid22(self, height, width, vline):
        for i in range(width):
            print("｜　" +  "　　" * i + "＼　")
        for i in range(height - width):
            print("　　" + "　　" * i + "＼　" + "　　" * (width - 1) + "＼　")
        for i in range(vline):
            print("　　" + "　　" * ((height - width) + i) + "＼　" + "　　" * (width - ((i + 1) * 2)) + "／　")
    def draw_trapezoid23(self, height, width):
        for i in range(width):
            print("　　" + "　　" * (width - (i + 1)) + "／　" + "　　" * i + "｜　")
        for i in range(height - width):
            print("｜　" + "　　" * width + "｜　")
        print("　　" + "﹉　" * width + "　")
    def draw_trapezoid24(self, height, width, vline):
        print("　　" * height  + "﹍　" * width)
        for i in range(height):
            print("　　" * (height - (i + 1)) + "／　" + "　　" * (width - 1) + "／　")
        for i in range(vline):
            print("　　" * i + "＼　" + "　　" * (width - ((i + 1) * 2)) + "／　")
    
    

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Line:
    def __init__(self, startPoint, endPoint):
        self.startPoint = startPoint
        self.endPoint = endPoint

    def getLength(self):
        return round(math.sqrt((self.endPoint.x - self.startPoint.x) ** 2 + (self.endPoint.y - self.startPoint.y) ** 2), 5)


def getFigureInfo(lineA, lineB, lineC, lineD):
    print("===============================")
    try:
        qulineadrilaterals = QuadrilateralShape(lineA, lineB, lineC, lineD)
        print(qulineadrilaterals.getShapeType())
        print(f"Perimeter length is {qulineadrilaterals.getPerimeter()}")
        print(f"Degree BAD is {qulineadrilaterals.getAngle('BAD')}")
        print(f"Area is {qulineadrilaterals.getArea()}")
        qulineadrilaterals.draw()
    except ValueError as err:
        print(f"Something wrong: {err}")
    print("===============================")

# 正方形1
lineA = Line(Point(0,0), Point(2,0))
lineB = Line(Point(2,0), Point(2,2))
lineC = Line(Point(2,2), Point(0,2))
lineD = Line(Point(0,2), Point(0,0))
getFigureInfo(lineA, lineB, lineC, lineD)

# 正方形2
lineA = Line(Point(0,0), Point(2,-2))
lineB = Line(Point(2,-2), Point(4,0))
lineC = Line(Point(4,0), Point(2,2))
lineD = Line(Point(2,2), Point(0,0))
getFigureInfo(lineA, lineB, lineC, lineD)

# 長方形1
lineA = Line(Point(0,0), Point(4,0))
lineB = Line(Point(4,0), Point(4,2))
lineC = Line(Point(4,2), Point(0,2))
lineD = Line(Point(0,2), Point(0,0))
getFigureInfo(lineA, lineB, lineC, lineD)

# 長方形2
lineA = Line(Point(0,0), Point(6,-6))
lineB = Line(Point(6,-6), Point(8,-4))
lineC = Line(Point(8,-4), Point(2,2))
lineD = Line(Point(2,2), Point(0,0))
getFigureInfo(lineA, lineB, lineC, lineD)

# 長方形4
lineA = Line(Point(0,0), Point(-6,-6))
lineB = Line(Point(-6,-6), Point(-4,-8))
lineC = Line(Point(-4,-8), Point(2,-2))
lineD = Line(Point(2,-2), Point(0,0))
getFigureInfo(lineA, lineB, lineC, lineD)

# # 平行四辺形1
lineA = Line(Point(0,0), Point(4,0))
lineB = Line(Point(4,0), Point(6,2))
lineC = Line(Point(6,2), Point(2,2))
lineD = Line(Point(2,2), Point(0,0))
getFigureInfo(lineA, lineB, lineC, lineD)

# 平行四辺形2
lineA = Line(Point(0,0), Point(2,-2))
lineB = Line(Point(2,-2), Point(6,-2))
lineC = Line(Point(6,-2), Point(4,0))
lineD = Line(Point(4,0), Point(0,0))
getFigureInfo(lineA, lineB, lineC, lineD)

# 平行四辺形3
lineA = Line(Point(0,0), Point(0,-2))
lineB = Line(Point(0,-2), Point(6,-8))
lineC = Line(Point(6,-8), Point(6,-6))
lineD = Line(Point(6,-6), Point(0,0))
getFigureInfo(lineA, lineB, lineC, lineD)

# 平行四辺形4
lineA = Line(Point(0,0), Point(-6,-6))
lineB = Line(Point(-6,-6), Point(-6,-8))
lineC = Line(Point(-6,-8), Point(0,-2))
lineD = Line(Point(0,-2), Point(0,0))
getFigureInfo(lineA, lineB, lineC, lineD)

lineA = Line(Point(2,0), Point(6,0))
lineB = Line(Point(6,0), Point(4,2))
lineC = Line(Point(4,2), Point(0,2))
lineD = Line(Point(0,2), Point(2,0))
getFigureInfo(lineA, lineB, lineC, lineD)

# 平行四辺形18
lineA = Line(Point(0,0), Point(2,-2))
lineB = Line(Point(2,-2), Point(2,4))
lineC = Line(Point(2,4), Point(0,6))
lineD = Line(Point(0,6), Point(0,0))
getFigureInfo(lineA, lineB, lineC, lineD)

# 平行四辺形19
lineA = Line(Point(0,0), Point(0,-4))
lineB = Line(Point(0,-4), Point(2,-2))
lineC = Line(Point(2,-2), Point(2,2))
lineD = Line(Point(2,2), Point(0,0))
getFigureInfo(lineA, lineB, lineC, lineD)

# 平行四辺形20
lineA = Line(Point(0,0), Point(-2,-2))
lineB = Line(Point(-2,-2), Point(2,-2))
lineC = Line(Point(2,-2), Point(4,0))
lineD = Line(Point(4,0), Point(0,0))
getFigureInfo(lineA, lineB, lineC, lineD)

# 菱形1
lineA = Line(Point(0,0), Point(4,0))
lineB = Line(Point(4,0), Point((2 * math.sqrt(2) + 4),(2 * math.sqrt(2))))
lineC = Line(Point((2 * math.sqrt(2) + 4),(2 * math.sqrt(2))), Point((2 * math.sqrt(2)),(2 * math.sqrt(2))))
lineD = Line(Point((2 * math.sqrt(2)),(2 * math.sqrt(2))), Point(0,0))
getFigureInfo(lineA, lineB, lineC, lineD)

# 台形1
lineA = Line(Point(0,0), Point(6,0))
lineB = Line(Point(6,0), Point(4,2))
lineC = Line(Point(4,2), Point(2,2))
lineD = Line(Point(2,2), Point(0,0))
getFigureInfo(lineA, lineB, lineC, lineD)

# 台形2
lineA = Line(Point(0,0), Point(6,-6))
lineB = Line(Point(6,-6), Point(6,-3))
lineC = Line(Point(6,-3), Point(3,0))
lineD = Line(Point(3,0), Point(0,0))
getFigureInfo(lineA, lineB, lineC, lineD)

# 台形3
lineA = Line(Point(0,0), Point(0,-6))
lineB = Line(Point(0,-6), Point(2,-4))
lineC = Line(Point(2,-4), Point(2,-2))
lineD = Line(Point(2,-2), Point(0,0))
getFigureInfo(lineA, lineB, lineC, lineD)

# 台形4
lineA = Line(Point(0,0), Point(-6,-6))
lineB = Line(Point(-6,-6), Point(-3,-6))
lineC = Line(Point(-3,-6), Point(0,-3))
lineD = Line(Point(0,-3), Point(0,0))
getFigureInfo(lineA, lineB, lineC, lineD)

# 台形9
lineA = Line(Point(0,0), Point(6,0))
lineB = Line(Point(6,0), Point(6,3))
lineC = Line(Point(6,3), Point(3,3))
lineD = Line(Point(3,3), Point(0,0))
getFigureInfo(lineA, lineB, lineC, lineD)

# 台形10
lineA = Line(Point(-8,4), Point(-2,-2))
lineB = Line(Point(-2,-2), Point(0,0))
lineC = Line(Point(0,0), Point(-4,4))
lineD = Line(Point(-4,4), Point(-8,4))
getFigureInfo(lineA, lineB, lineC, lineD)

# 台形11
lineA = Line(Point(0,0), Point(0,-6))
lineB = Line(Point(0,-6), Point(3,-6))
lineC = Line(Point(3,-6), Point(3,-3))
lineD = Line(Point(3,-3), Point(0,0))
getFigureInfo(lineA, lineB, lineC, lineD)

# 台形12
lineA = Line(Point(0,0), Point(-6,-6))
lineB = Line(Point(-6,-6), Point(-3,-9))
lineC = Line(Point(-3,-9), Point(0,-6))
lineD = Line(Point(0,-6), Point(0,0))
getFigureInfo(lineA, lineB, lineC, lineD)

# 台形25
lineA = Line(Point(0,0), Point(4,0))
lineB = Line(Point(4,0), Point(6,2))
lineC = Line(Point(6,2), Point(0,2))
lineD = Line(Point(0,2), Point(0,0))
getFigureInfo(lineA, lineB, lineC, lineD)

# 台形26
lineA = Line(Point(0,0), Point(4,-4))
lineB = Line(Point(4,-4), Point(8,-4))
lineC = Line(Point(8,-4), Point(2,2))
lineD = Line(Point(2,2), Point(0,0))
getFigureInfo(lineA, lineB, lineC, lineD)

# 台形27
lineA = Line(Point(0,0), Point(0,-4))
lineB = Line(Point(0,-4), Point(2,-6))
lineC = Line(Point(2,-6), Point(2,0))
lineD = Line(Point(2,0), Point(0,0))
getFigureInfo(lineA, lineB, lineC, lineD)

# 台形28
lineA = Line(Point(0,0), Point(-4,-4))
lineB = Line(Point(-4,-4), Point(-4,-8))
lineC = Line(Point(-4,-8), Point(2,-2))
lineD = Line(Point(2,-2), Point(0,0))
getFigureInfo(lineA, lineB, lineC, lineD)

# Error
lineA = Line(Point(0,0), Point(-4,-4))
lineB = Line(Point(-4,-4), Point(-4,-4))
lineC = Line(Point(-4,-4), Point(2,-2))
lineD = Line(Point(2,-2), Point(0,0))
getFigureInfo(lineA, lineB, lineC, lineD)

# Error
lineA = Line(Point(0,0), Point(2,0))
lineB = Line(Point(2,0), Point(4,0))
lineC = Line(Point(4,0), Point(6,0))
lineD = Line(Point(6,0), Point(0,0))
getFigureInfo(lineA, lineB, lineC, lineD)

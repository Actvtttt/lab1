from PIL import Image

#Функция для отрисовки пикселя
def drawline(x, y, image):
    if 0 <= int(x) < len(image[0]) and 0 <= int(y) < len(image):
        image[int(y)][int(x)] = (255, 255, 255)

#Алгоритм ЦДА
def CDA(x0, y0, x1, y1, image):
    if(x1 == x0) and (y0 == y1):
        print("Отрезок является выражденным")
        return 0
    else:
        L = int(max(abs(x1 - x0), abs(y1 - y0)))
        dx = (x1 - x0) / L
        dy = (y1 - y0) / L
    
        x = x0 + 0.5
        y = y0 + 0.5
        for i in range(L + 1):
            drawline(x, y, image)
            x += dx
            y += dy

#Алгоритм плавающего Брезенхема
def float_Bresenham(x0, y0, x1, y1, image):
    if(x1 == x0) and (y0 == y1):
        print("Отрезок является выражденным")
        return 0
    else:
        dx = x1 - x0
        dy = y1 - y0
        
        sx = 1 if dx > 0 else -1
        sy = 1 if dy > 0 else -1
        
        dx = abs(dx)
        dy = abs(dy)
        
        if dx > dy:
            err = dx / 2.0
            while x0 != x1:
                drawline(x0, y0, image)
                err -= dy
                if err < 0:
                    y0 += sy
                    err += dx
                x0 += sx
            drawline(x1, y1, image)
        else:
            err = dy / 2.0
            while y0 != y1:
                drawline(x0, y0, image)
                err -= dx
                if err < 0:
                    x0 += sx
                    err += dy
                y0 += sy
            drawline(x1, y1, image)

#Алгоритм целочисленного Брезенхема
def int_Bresenham(x0, y0, x1, y1, image):
    if(x1 == x0) and (y0 == y1):
        print("Отрезок является выражденным")
        return 0
    else:
        dx = x1 - x0
        dy = y1 - y0
        dx1 = abs(dx)
        dy1 = abs(dy)
        px = 2 * dy1 - dx1

        if dy1 <= dx1:
            if dx >= 0:
                x = x0
                y = y0
                x_end = x1
            else:
                x = x1
                y = y1
                x_end = x0
            image[y][x] = (255, 255, 255)  
        
            while x < x_end:
                x += 1
                if px < 0:
                    px += 2 * dy1
                else:
                    if dy >= 0:
                        y += 1
                    else:
                        y -= 1
                    px += 2 * (dy1 - dx1)
                drawline(x, y, image)
        else:
            if dy >= 0:
                x = x0
                y = y0
                y_end = y1
            else:
                x = x1
                y = y1
                y_end = y0
            image[y][x] = (255, 255, 255)  
        
            while (dy >= 0 and y < y_end) or (dy < 0 and y > y_end):
                y += 1 if dy >= 0 else -1
                if px <= 0:
                    px += 2 * dx1
                else:
                    if dx >= 0:
                        x += 1
                    else:
                        x -= 1
                    px += 2 * (dx1 - dy1)
                drawline(x, y, image)

#Размер изображения
width, height = 300, 300
image = [[(0, 0, 0) for _ in range(width)] for _ in range(height)]

CDA(100, 295, 200, 205, image)            #отрезок по ЦДА
float_Bresenham(100, 195, 200, 105, image) #отрезок по алгоритму плавающего Брезенхема
int_Bresenham(100, 95, 200, 5, image)      #отрезок по целочисленному Брезенхему

#Сохранение изображения
img = Image.new('RGB', (width, height))
for y in range(height):
    for x in range(width):
        img.putpixel((x, y), image[y][x])
img.save('output.png')
img.show()

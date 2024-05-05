from circles import Circle
import numpy as np
import regex as re


def bubblesort(r):
    
    Circles = [Circle(x) for x in r]
    for i in range(len(Circles)):
        swapped = False
        
        for j in range(0,len(Circles)-i-1):
            
            if Circles[j] > Circles[j+1]:
                Circles[j], Circles[j+1] = Circles[j+1], Circles[j]
                r[j], r[j+1] = r[j+1], r[j]
                swapped = True
        if swapped == False:
            break
    return r

if __name__ == "__main__":
    r = np.random.uniform(0,100, 100)
    
    bubblesort(r)
    print(bubblesort(r))

    perimeters = {f"r: {x}":"Perimeter: {}".format(Circle(x).perimeter()) for x in r}
    
    for radius,perimeter in perimeters.items():
        print(f"{radius} {perimeter}")
        
    areas = {f"r: {x}":"Area: {}".format(Circle(x).area()) for x in r}
    
    for radius,area in areas.items():
        print(f"{radius} {area}")
    
    for rad in r:
        pattern = r"\d\.\d*"
        state = float(re.findall(pattern,areas[f"r: {rad}"])[0]) > float(re.findall(pattern,perimeters[f"r: {rad}"])[0])
        print(areas[f"r: {rad}"],perimeters[f"r: {rad}"], state)
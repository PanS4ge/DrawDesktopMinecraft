from mcpi.minecraft import Minecraft
mc = Minecraft.create()
from PIL import Image
import time
import json
import pyautogui
import array
import os
import math
import ctypes
import numpy as np

def Screenshot():
    return pyautogui.screenshot()

def getIntFromStr(strn):
    for x in range(999):
        if(str(x) == strn):
            return x

def closest(colors,color):
    colors = np.array(colors)
    color = np.array(color)
    distances = np.sqrt(np.sum((colors-color)**2,axis=1))
    index_of_smallest = np.where(distances==np.amin(distances))
    smallest_distance = colors[index_of_smallest]
    arraytogiveback = []
    for atgb in smallest_distance:
        arraytogiveback.append(atgb)
    arraytogiveback = str(arraytogiveback)
    arraytogiveback = " ".join(arraytogiveback.split())
    arraytogiveback = arraytogiveback.replace("[array([", "")
    arraytogiveback = arraytogiveback.replace("])]", "")
    arraytogiveback = arraytogiveback.replace(",", "")
    arraytogiveback = arraytogiveback.replace("  ", "")
    arraytogiveback = arraytogiveback.split(" ")
    backarray = []
    for fadf in arraytogiveback:
        if(fadf == ''):
            print("")
        else:
            backarray.append(getIntFromStr(fadf))
    return backarray

img = input("Want to print a screenshot? (Y/N)")
if(img == "N"):
    img = input("Please write down location of your image")
scale = input("What scale to do? 1:")

MessageBox = ctypes.windll.user32.MessageBoxW
MessageBox(None, 'Waiting for screenshot', 'Printer', 0)
time.sleep(5)

if(img == "Y"):
    img = Screenshot()
else:
    img = Image.open(img)

width, height = img.size

blockcnt = 0
maxblock = width*height/int(scale)

poz = mc.player.getPos()

xpl = poz.x
ypl = poz.y
zpl = poz.z

MessageBox(None, 'Done, please leave the server for efficency', 'Printer', 0)

path_to_file = __file__
path_to_file = path_to_file.replace(os.path.basename(__file__), "")

with open(path_to_file + 'kolory.json') as f:
    jsoncolors = json.load(f)
    if(3>2):
        if(3>2):
            if(3>2):
                pixels = img.convert('RGBA').load()
                width, height = img.size

                for x in range(0, width, int(scale)):
                    for y in range(0, height, int(scale)):
                        for num in range(len(jsoncolors["colourinhex"])):
                            blockcnt = blockcnt + 1
                            r, g, b, a = pixels[x, y]
                            if([r,g,b,a] in jsoncolors["colourinhex"][num]["rgba"]):

                                print("Placed block at " + str(
                                    math.floor(xpl + (x / getIntFromStr(scale)))) + " " + str(math.floor(ypl)) + " " + str(
                                    math.floor((y / getIntFromStr(scale)) + zpl)) + " // Blocks: (" + str(
                                    blockcnt) + "/" + str(maxblock) + ")")

                                mc.setBlock(math.floor(xpl + (x / getIntFromStr(scale))), math.floor(ypl), math.floor((y / getIntFromStr(scale)) + zpl), jsoncolors["colourinhex"][num]["minecraftblock"]["blockid"], jsoncolors["colourinhex"][num]["minecraftblock"]["variant"])
                            else:
                                allcolors = []
                                for colorsss in range(len(jsoncolors["colourinhex"])):
                                    allcolors.append(jsoncolors["colourinhex"][colorsss]["rgba"])
                                try:
                                    print("Placed block at " + str(
                                        math.floor(xpl + (x / getIntFromStr(scale)))) + " " + str(
                                        math.floor(ypl)) + " " + str(
                                        math.floor((y / getIntFromStr(scale)) + zpl)) + " // Blocks: (" + str(
                                        blockcnt) + "/" + str(maxblock) + ")")
                                    mc.setBlock(math.floor(xpl + (x / getIntFromStr(scale))), math.floor(ypl), math.floor((y / getIntFromStr(scale)) + zpl), jsoncolors["colourinhex"][allcolors.index(closest(allcolors, pixels[x, y]))]["minecraftblock"]["blockid"], jsoncolors["colourinhex"][allcolors.index(closest(allcolors, pixels[x, y]))]["minecraftblock"]["variant"])
                                except ValueError:
                                    print("Error with finding rgba - " + str(r) + " " + str(g) + " " + str(b) + " " + str(a) + "- Array " + str(closest(allcolors, pixels[x, y])))
                                    mc.postToChat("Error with finding rgba - " + str(r) + " " + str(g) + " " + str(b) + " " + str(a) + "- Array " + str(closest(allcolors, pixels[x, y])))
                                    print("Trying to fix...")
                                    mc.postToChat("Trying to fix...")
                                    try:
                                        arr = closest(allcolors, pixels[x, y])
                                        for far in range(len(arr) - 4):
                                            if(arr[far] == ''):
                                                arr.pop(arr.index(far))
                                            else:
                                                temp = arr[far]
                                                arr.pop(arr.index(far))
                                                if(temp in arr):
                                                    mc.postToChat("Fixing...")
                                                else:
                                                    arr.append(temp)

                                            print("Placed block at " + str(
                                                math.floor(xpl + (x / getIntFromStr(scale)))) + " " + str(
                                                math.floor(ypl)) + " " + str(
                                                math.floor((y / getIntFromStr(scale)) + zpl)) + " // Blocks: (" + str(
                                                blockcnt) + "/" + str(maxblock) + ")")
                                            mc.setBlock(math.floor(xpl + (x / getIntFromStr(scale))), math.floor(ypl),
                                                        math.floor((y / getIntFromStr(scale)) + zpl),
                                                        jsoncolors["colourinhex"][
                                                            allcolors.index(arr)][
                                                            "minecraftblock"]["blockid"], jsoncolors["colourinhex"][
                                                            allcolors.index(arr)][
                                                            "minecraftblock"]["variant"])
                                    except:
                                        print("Unable to fix - Array " + str(closest(allcolors, pixels[x, y])) + " -> " + arr)
                                        mc.postToChat("Unable to fix - Array " + str(closest(allcolors, pixels[x, y])) + " -> " + arr)

MessageBox(None, 'You may log back in.', 'Printer', 0)

for xcl in range(math.floor(xpl), math.floor(xpl + width / getIntFromStr(scale))):
    for zcl in range(math.floor(zpl), math.floor(zpl + height / getIntFromStr(scale))):
        mc.setBlock(xcl, ypl + 1, zcl, 0)
        mc.setBlock(xcl, 250, zcl, 20)

MessageBox(None, 'My job is done', 'Printer', 0)

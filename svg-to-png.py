#!/usr/bin/python3
from cairosvg import svg2png
import os
import sys
import re
import wget

try:   
    args = sys.argv[1:]
    file = open(args[0],"rt")
    png_dir = args[1]
    filename = args[2]
    file_content = file.read()
    svg_code = re.findall('.*svg.*',file_content)

except IndexError:
    print("The first argument is missing. Write the name of a file")
    exit
except FileNotFoundError:
    print("File not found.")
    exit
except:
    print("Something unexpected happened: {}".format(str(e)))
    exit
else:
    if not os.path.exists(png_dir):
        os.makedirs(png_dir)

try:
    for code in svg_code:

        pngf = png_dir + '/' + filename + ".png"

        cn = 1
        while os.path.exists(pngf):
            pngf = png_dir + '/' + filename + '-' + str(cn) + ".png"
            cn+=1
        url = re.match(r".+[\]\(](.+\.svg)", code).group(1)
        remote_filename = wget.download(url)
        with open(remote_filename, 'r') as f:
            svg2png(bytestring=f.read(), write_to=pngf)
            file_content = file_content.replace(url,pngf)

except ValueError as e:
    print("Something is wrong in your SVG code: {}".format(str(e)))
    exit
except Exception as e:
    print("Something unexpected happened: {}".format(str(e)))
    exit
else:

    file.close()
    file = open(args[0],"wt")
    file.write(file_content)
    file.close()

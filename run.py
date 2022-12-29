# -*- coding: utf-8 -*-

import sys
import os
import argparse
from canvas import Canvas

if __name__ == "__main__":    
    # Parse command line arguments
    # Want to allow default arguments for each
    parser = argparse.ArgumentParser(
                    prog = 'PaintByNumbers',
                    description = 'Generate paint-by-numbers map from input image')
    # Adding default named/positional args
    parser.add_argument("-path", default="inputs/", type=str, 
                        help='path of the source picture(s). Can be a directory or file.')
    parser.add_argument("-n", default=10, type=int,
                        help="number of colors you want in the canvas (10 to 20)")
    parser.add_argument("--plot", default=True, type=bool,
                        help="optional, boolean to set to True if you want to see some plots. Default True")
    parser.add_argument("--save", "-s", default=True, type=bool,
                        help="optional, boolean to set to True if you want to save results in the ./outputs folder")
    parser.add_argument("--pixel_size", "-x", default=4000, type=int,
                        help="optional, interger, size in pixel of the largest dimension of the output canvas (default 4000)")
    parser.add_argument("--colormap", default=False, type=bool, 
                        help="optional, if True, display colormap used from source image (default True)")
    parser.add_argument("--min-contour-size", default=15, type=int, 
                        help="optional, minimum contour size (width or height) to be plotted (default 15 px)")

    args = parser.parse_args()

    # Create image and plot
    CANVAS = Canvas(args.path, args.n, args.plot, args.save, args.pixel_size, args.min_contour_size)

    CANVAS.generate()

    if args.colormap:
        CANVAS.display_colormap()
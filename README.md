# paint-by-numbers
A quick Python tool to transform any picture in a paint-by-number canvas, using [`opencv`](https://pypi.org/project/opencv-python/)

# How it works
1) Picture is resized, denoised and cleaned using morphomat  
2) K-mean algorithm to detect the k-colors summarizing the best the picture  
3) Transformation of the picture to match these colors  
4) Contour detection and drawing of contours on new canvas  
5) Add label of each shape on the canvas  
6) Creation of the colormap for the user


### Execution:
run `python run.py [path] [nb_color] [plot] [save] [pixel_size]` with:

  **path**: path of the source picture  
  **nb_color** : number of colors you want in the canvas (10 to 20)  
  **plot**: optional, boolean to set to True if you want to see some plots. Default False  
  **save**: optional, boolean to set to True if you want to save results in the `./outputs` folder. Default True  
  **pixel_size**: optional, interger, size in pixel of the largest dimension of the output canvas (default 4000)

### Result:

#### De Chirico, Place d'Italie, 1922
![alt text](https://github.com/Haha89/paint-by-number/blob/master/inputs/chirico.jpg "De Chirico, Place d'Italie, 1922")
#### Expected result (20 colors)
![alt text](https://github.com/Haha89/paint-by-number/blob/master/outputs/chirico-result.png "Expected result")
#### Canvas
![alt text](https://github.com/Haha89/paint-by-number/blob/master/outputs/chirico-canvas.png "Canvas")
#### Colormap
![alt text](https://github.com/Haha89/paint-by-number/blob/master/outputs/chirico-colormap.png "Colormap")

### Next Steps:

- Better positioning of the label in each region
- Better contour filtering to remove small regions


# Display Image Tabs

This is a convenience Python package to display image tabs in a Jupyter notebook.

![](img/screenshot-tab-images.png)

## 1 - Install

From terminal

```bash
pip install notebook_image_tabs
```


## 2 - User Guide

See the [demo notebook](https://nbviewer.jupyter.org/github/oscar6echo/notebook-image-tabs/blob/master/demo_image_tabs.ipynb).

The data must be input as follows

```Python
data = [
    # list of
    # name, image as path
    ['london', 'img/london.jpg'],
    # name, image as url
    ['paris', 'http://path/to/an/image.png'],
    # name, image as base64 string
    ['tokyo', '/9j/4AAQSkZJRgABAQAAAQAB...etc'],
]
```

The layout params are as follows

```Python
# all params are CSS variables
# default values below
dic_param = {
    # title
    'titleText': None, # above tabs in bold font
    # dimensions
    'width': 960, # width in pixel
    'height': 500, # height in pixel
    'widthIframe': None, # automatically calculated - should not require manual tampering
    'heightIframe': None, # automatically calculated - may require manual tampering if word wrap
    # border around tab and image container
    'borderPx': 0, # border in pixel
    'borderColor': 'gray', # border color
    # tab is div on top of image container
    'tabBackgroundColor': 'white', # backgroud-color
    # one button for each data item
    'buttonMargin': 5, # margin in pixel
    'buttonPaddingVert': 12, # padding vertical in px
    'buttonPaddingHori': 7, # padding horizontal in px
    'buttonBorderColor': 'black', # border color
    # one image in image container displayed if button is active
    'imageWidthPerCent': 99, # width in %
    # image container and tab width
    'width': None, # div will default to 100%
    # image container height
    'height': None, # div will size automatically
    # button selected at start 0-indexed
    'selection': 0,
    # button colors base / hover / active
    'buttonColorBase': '#eeeeee',
    'buttonColorHover': '#dddddd',
    'buttonColorActive': '#bdbdbd',
}
```

To display the image tabs

```Python
# create object in iframe
t = ImageTabs(data=data, params=dic_param)

# create object in main page
t = ImageTabs(data=data, params=dic_param, iframe=False)

# display
t.show()
```

### 2.1 - IFrame

Why the `iframe` option ?

+ To make the package compatible with [JupyterLab](https://github.com/jupyterlab/jupyterlab) which disables javascript injection.

+ Note that even in the classical notebook there is no downside in using the iframe option - except possibly a bit more tampering with the iframe dimensions. 


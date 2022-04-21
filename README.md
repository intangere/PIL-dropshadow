# PIL-dropshadow
Add a drop shadow or glow affect to an image using PIL.  

The image must have an alpha layer for this to work (transparent background).  

Usage:
```
from shadow import dropShadow
new_image = dropShadow(image, shadow=(234,100,100,255), background=(0,0,0,255), radius=4)
```

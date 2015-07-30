Parsing photos from Instagram and VK by geographic coordinates.

Default Settings:

```
#!python

INSTAGRAM_ACCESS_TOKEN = 'YOUR_INSTAGRAM_TOKEN'
DISTANCE = '100'
TIME_INCREMENT = 60*60*24
```

If you want to parse instagram, you should set **INSTAGRAM_ACCESS_TOKE**. Without access_token program parses VK only.

All results saves to HTML file.

Example:


```
#!

python photobygeo.py 55.740701 37.609161 1400619600 1400792400
```


The console log:

![1.png](https://bitbucket.org/repo/KerG5L/images/3709769959-1.png)

The console help:

![2.png](https://bitbucket.org/repo/KerG5L/images/2817277897-2.png)

The result looks like this:

![screenshot2.png](https://bitbucket.org/repo/KerG5L/images/3473396433-screenshot2.png)
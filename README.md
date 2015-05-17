Parsing photos from Instagram and VK by geographic coordinates.

Default Settings:

```
#!python

LOCATION_LATITUDE = '55.740701'
LOCATION_LONGITUDE = '37.609161'
DISTANCE = '100'
MIN_TIMESTAMP = 1400619600
MAX_TIMESTAMP = 1400792400
DATE_INCREMENT = 60*60*24
INSTAGRAM_ACCESS_TOKEN = 'YOUR_INSTAGRAM_TOKEN'
```

If you want to parse instagram, you should set **INSTAGRAM_ACCESS_TOKE**. Without access_token program parses VK only.

All results saves to HTML file.

The console log:

![screenshot.png](https://bitbucket.org/repo/KerG5L/images/417140315-screenshot.png)

The result looks like this:

![screenshot2.png](https://bitbucket.org/repo/KerG5L/images/3473396433-screenshot2.png)
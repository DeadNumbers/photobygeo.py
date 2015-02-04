Parsing photos from Instagram and VK by geographic coordinates.

Default Settings:

```
#!python

location_latitude = '55.740701' 
location_longitude = '37.609161'
distance = '100'
min_timestamp = 1400619600
max_timestamp = 1400792400
date_increment = 60*60*3 # every 3 hours
instagram_access_token = 'YOUR_INSTAGRAM_TOKEN'
```

If you want to parse instagram, you should set **instagram_access_token**. Without access_token program parses VK only.

All results saves to HTML file.

The console log:

![screenshot.png](https://bitbucket.org/repo/KerG5L/images/417140315-screenshot.png)

The result looks like this:

![screenshot2.png](https://bitbucket.org/repo/KerG5L/images/3473396433-screenshot2.png)
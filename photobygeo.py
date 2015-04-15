"""
Author: 	Betepok
Version:	1.01
Date:		15.04.2015
Twitter:	http://twitter.com/BetepO_ok

"""

from datetime import datetime
from requests import get as getResponse


LOCATION_LATITUDE = '55.740701'
LOCATION_LONGITUDE = '37.609161'
DISTANCE = '100'
MIN_TIMESTAMP = 1400619600
MAX_TIMESTAMP = 1400792400
DATE_INCREMENT = 60*60*24
INSTAGRAM_ACCESS_TOKEN = 'YOUR_INSTAGRAM_TOKEN'


def getInstagram(latitude, longitude, distance, minTimestamp, maxTimestamp):
	params = {
		'lat': latitude,
		'lng': longitude,
		'distance': distance,
		'min_timestamp': str(minTimestamp),
		'max_timestamp': str(maxTimestamp),
		'access_token': INSTAGRAM_ACCESS_TOKEN
	}
	return getResponse("https://api.instagram.com/v1/media/search", \
		params=params, verify=True).json()


def getVK(latitude, longitude, distance, minTimestamp, maxTimestamp):
	params = {
		'lat': latitude,
		'long': longitude,
		'count': '100',
		'radius': distance,
		'start_time': minTimestamp,
		'end_time': maxTimestamp,
	}
	return getResponse("https://api.vk.com/method/photos.search", \
		params=params, verify=True).json()


def convertTSToDate(timestamp):
	return datetime.fromtimestamp(timestamp).strftime('%Y-%m-%d %H:%M:%S') + ' UTC'


def parseInstagram(latitude, longitude, distance, minTimestamp, maxTimestamp, dateIncrement):
	if INSTAGRAM_ACCESS_TOKEN == 'YOUR_INSTAGRAM_TOKEN':
		print 'You should add your instagram access token'
		return
	print 'Starting parse instagram..'
	print 'GEO:', latitude, longitude
	print 'TIME: from', convertTSToDate(minTimestamp), 'to', convertTSToDate(maxTimestamp)
	fileDescriptor = open('instagram_' + latitude + longitude + '.html', 'w')
	fileDescriptor.write('<html>')
	localMinTimestamp = minTimestamp
	while (1):
		if ( localMinTimestamp >= maxTimestamp ):
			break
		localMaxTimestamp = localMinTimestamp + dateIncrement
		if ( localMaxTimestamp > maxTimestamp ):
			localMaxTimestamp = maxTimestamp
		print convertTSToDate(localMinTimestamp), '-', convertTSToDate(localMaxTimestamp)
		responseJSON = getInstagram(latitude, longitude, distance, localMinTimestamp, localMaxTimestamp)
		for fieldJSON in responseJSON['data']:
			fileDescriptor.write('<br>')
			fileDescriptor.write('<img src=' + fieldJSON['images']['standard_resolution']['url'] + '><br>')
			fileDescriptor.write(convertTSToDate(int(fieldJSON['created_time'])) + '<br>')
			fileDescriptor.write(fieldJSON['link'] + '<br>')
			fileDescriptor.write('<br>')
		localMinTimestamp = localMaxTimestamp
	fileDescriptor.write('</html>')
	fileDescriptor.close()


def parseVK(latitude, longitude, distance, minTimestamp, maxTimestamp, dateIncrement):
	print 'Starting parse vkontakte..'
	print 'GEO:', latitude, longitude
	print 'TIME: from', convertTSToDate(minTimestamp), 'to', convertTSToDate(maxTimestamp)
	fileDescriptor = open('vk_' + latitude + longitude + '.html', 'w')
	fileDescriptor.write('<html>')
	localMinTimestamp = minTimestamp
	while (1):
		if (localMinTimestamp >= maxTimestamp):
			break
		localMaxTimestamp = localMinTimestamp + dateIncrement
		if (localMaxTimestamp > maxTimestamp):
			localMaxTimestamp = maxTimestamp
		print convertTSToDate(localMinTimestamp), '-', convertTSToDate(localMaxTimestamp)
		responseJSON = getVK(latitude, longitude, distance, localMinTimestamp, localMaxTimestamp)
		for fieldJSON in responseJSON['response']:
			if type(fieldJSON) is int:
				continue
			fileDescriptor.write('<br>')
			fileDescriptor.write('<img src=' + fieldJSON['src_big'] + '><br>')
			fileDescriptor.write(convertTSToDate(int(fieldJSON['created'])) + '<br>')
			fileDescriptor.write('http://vk.com/id' + str(fieldJSON['owner_id']) + '<br>')
			fileDescriptor.write('<br>')
		localMinTimestamp = localMaxTimestamp
	fileDescriptor.write('</html>')
	fileDescriptor.close()


parseInstagram(LOCATION_LATITUDE, LOCATION_LONGITUDE, DISTANCE, MIN_TIMESTAMP, MAX_TIMESTAMP, DATE_INCREMENT)
parseVK(LOCATION_LATITUDE, LOCATION_LONGITUDE, DISTANCE, MIN_TIMESTAMP, MAX_TIMESTAMP, DATE_INCREMENT)

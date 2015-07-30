"""
Author: 	Betepok
Version:	1.2.01
Date:		30.07.2015
Twitter:	https://twitter.com/BetepO_ok
Bitbucket:	https://bitbucket.org/BetepokNoname

"""

VERSION = '1.2.01 (30.07.2015)'
AUTHOR = 'Betepok (https://twitter.com/BetepO_ok)'

from datetime import datetime
from requests import get as getResponse
from argparse import ArgumentParser, RawDescriptionHelpFormatter
from textwrap import dedent


INSTAGRAM_ACCESS_TOKEN = 'YOUR_INSTAGRAM_TOKEN'
DISTANCE = '100'
TIME_INCREMENT = 60*60*24


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
	print 'Parsing instagram..'
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
	print 'Parsing vkontakte..'
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


def main():
	global INSTAGRAM_ACCESS_TOKEN
	global DISTANCE
	global TIME_INCREMENT
	global VERSION
	global AUTHOR
	INFO = dedent('''
	-------- example --------

	python photobygeo.py 55.740701 37.609161 1400619600 1400792400

	-------- about ----------

	Parsing photos from Instagram and VK by geographic coordinates.
	Version: %s
	Author: %s

	-------- arguments ------
	''' % (VERSION, AUTHOR))
	parser = ArgumentParser(description=INFO,
		formatter_class=RawDescriptionHelpFormatter)
	parser.add_argument("latitude", type=str,
		help="Geographic latitude")
	parser.add_argument("longitude", type=str,
		help="Geographic longitude")
	parser.add_argument("min_timestamp", type=int,
		help="Start the search from this timestamp")
	parser.add_argument("max_timestamp", type=int,
		help="Finish the search in this timestamp")
	parser.add_argument("-d", "--distance", action="store",
		help="Distance for search (meters). Default: %s" % DISTANCE)
	parser.add_argument("-i", "--increment", action="store",
		help="Time increment for search (seconds). Default: %d" % TIME_INCREMENT)
	args = parser.parse_args()
	if args.distance:
		DISTANCE = args.distance
	if args.increment:
		TIME_INCREMENT = args.increment
	print 'GEO:', args.latitude, args.longitude
	print 'TIME: from', convertTSToDate(args.min_timestamp), 'to', convertTSToDate(args.max_timestamp)
	print 'DISTANCE: %s' % DISTANCE
	print 'TIME INCREMENT: %d' % TIME_INCREMENT
	parseInstagram(args.latitude, 
		args.longitude, 
		DISTANCE, 
		args.min_timestamp, 
		args.max_timestamp, 
		TIME_INCREMENT)
	parseVK(args.latitude, 
		args.longitude, 
		DISTANCE, 
		args.min_timestamp, 
		args.max_timestamp, 
		TIME_INCREMENT)


if __name__ == "__main__":
    main()

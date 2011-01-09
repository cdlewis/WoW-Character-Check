from argparse import ArgumentParser
from urllib import urlopen
from itertools import product

# Handle command line arguments
parser = ArgumentParser( description="Attempts to find free character names of a given length")
parser.add_argument( "server", metavar="s", help="server to check character names against" )
parser.add_argument( "--length", metavar="l", default=2, help="name length (default is 2)" )
arguments = parser.parse_args()

# WoW Armory search URL
url = "http://us.battle.net/wow/en/character/%s/%s/simple"

# Strings found on the results page that we can use to determine the status of a character
result_types = { "@ %s - Game - World of Warcraft" % arguments.server: False,
				 "<!-- character : low-level -->" : False,
				 "<!-- character : not-found -->" : True }

print "Checking %s for free character names of size %s" % ( arguments.server, str( arguments.length ) )

for i in product( map( chr, range( 97, 123 ) ), repeat=arguments.length ):

	combination = ''.join( i ) # Letters are a tuple, turn into a string

	page = urlopen( url % ( arguments.server, combination ) ).read() # Search the armory

	for key in result_types:
		if key in page and result_types[ key ]:
			print combination 
			break

from gamera.core import *
from gamera.toolkits.st_gall_lyric_extraction import find_lyrics

init_gamera()

img = load_image("/Users/nickesterer/Desktop/Untitled.png")

onebit = img.to_onebit()

ccs = onebit.cc_analysis()

print "Number of ccs before", len(ccs)

func = find_lyrics.remove_ccs_intersected_by_lines()

lines = [(1,x * 100) for x in xrange(20)]

newccs = func(ccs, lines)

print "Number of ccs after", len(newccs)

import pdb; pdb.set_trace()

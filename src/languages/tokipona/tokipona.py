"""
    This file is part of reserbot.

    reserbot is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    reserbot is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with reserbot.  If not, see <http://www.gnu.org/licenses/>.

    Copyright 2010 neuromancer
"""
import os, sys

# corpus

extra_words = ["."]
path = os.path.join("src","languages","tokipona","raw_data")
corpus = map( lambda ls: filter((lambda l: l<>'\n'),ls), open(os.path.join(path,'corpus.txt'),'r').readlines())
corpus = corpus + extra_words

def preprocess_word(word):
    if not (word in extra_words):
            return (word+" ")
    return word

    
# syllables

extra_syllables = [" ", "."]    
syllables = [
	    "a-",	"e-",	"i-",	"o-",	"u",
            "ka-",	"ke-",	"ki-",	"ko-",	"ku-",
            "sa-",	"se-",	"si-",	"so-",	"su-", 
	    "ta-",	"te-",		"to-",	"tu-",
	    "na-",	"ne-",	"ni-",	"no-",	"nu-",
	    "pa-",	"pe-",	"pi-",	"po-",	"pu-",
	    "ma-",	"me-",	"mi-",	"mo-",	"mu-",
	    "ja-",	"je-",		"jo-",
	    "jan-",	"wan-",	"lin-",	"sin-",	"kon-",
	    "ten-",	"mon-",	"tan-",	"ken-",
	    "la-",	"le-",	"li-",	"lo-",	"lu-",
	    "wa-",	"we-",	"wi-",
	    "len-",	"wen-", "sin-",	"pin-",	"lon-",
	    "pan-",	"kin-",	"pen-",	"nan-",	"mun-",
	    "an-",	"in-",	"en-",	"un-",	"es-",
           ]

syllables = syllables + extra_syllables
syllables =  sorted(syllables, key = len, reverse = True)

def preprocess_syllable(syllable):
    if not (syllable in extra_syllables):
            return (syllable+"-")
    return syllable           

# letters

extra_letters = " .-"
letters       = "abcdefghijklmnopqrstuvwxyz" 
letters       = letters + extra_letters

# syllabification

def silabizar(w,ss):
    wo = w
    r = []
    while (w<>""):
        f = False
        for s in ss:
            if (s in  w[0:len(s)]):
                f = True
                r.append(s)
                w = w[len(s):]
                break
        if (not f):
            print "Silabizacion fallida en "+w+" ("+wo+") !"
            assert(False)
    return r 

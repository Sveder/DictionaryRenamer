import android
droid = android.Android()

t = {u"\u05d0" : u"a", u"\u05d1" : u"b", u"\u05d2" : u"g", u"\u05d3" : u"d", u"\u05d4" : u"h", 
u"\u05d5" : u"o", u"\u05d6" : u"z", u"\u05d7" : u"ch", u"\u05d8" : u"t", u"\u05d9" : u"y", 
u"\u05da" : u"k", u"\u05db" : u"k", u"\u05dc" : u"l", u"\u05dd" : u"m", u"\u05de" : u"m", 
u"\u05df" : u"n", u"\u05e0" : u"n", u"\u05e1" : u"s", u"\u05e2" : u"a", u"\u05e3" : u"f", 
u"\u05e4" : u"f", u"\u05e5" : u"tz", u"\u05e6" : u"tz", u"\u05e7" : u"k", u"\u05e8" : u"r", u"\u05e9" : u"sh", 
u"\u05ea" : u"t", u"\u20aa" : u"NIS", u"\u2029" : u"|" }

res = droid.smsGetMessages(False, u"inbox", None)
for i in res.result:
    msg = i["body"]
    trans = u""
    for c in msg:
        if c in t:
            trans += t[c]
        else:
            trans += c
    trans = trans.encode("ascii", "replace")
    print i[u"address"], u":", trans
	
	
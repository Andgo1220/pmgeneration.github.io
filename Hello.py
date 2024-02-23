import perlin
from pydub import AudioSegment
from pydub.playback import play

def Sound(seedHI):
        
    p = perlin.Perlin(int(seedHI)).one_octave

    s = ""
        
    l = (abs(p(5))+2)*10
    
    y = 100

    for x in range (0,l):
        s = s + str(p(x)) + ', '
        s = s + str(p(y+2)) + ', '
        ++y

    print('l=' + str(l))
    print('Perlin = ' + s)
    return s + 'l=' + str(l) + ". Seed=" + str(seedHI)

from kivy.core.audio import SoundLoader

sound = SoundLoader.load('teste.mp3')
print('-------', sound)
if sound:
    print("Sound found at %s" % sound.source)
    print("Sound is %.3f seconds" % sound.length)
    sound.play()
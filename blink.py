from gpiozero import LED, PWMLED, TonalBuzzer
from gpiozero.tones import Tone
from signal import pause
from time import sleep
import anvil.server
anvil.server.connect("YOUR API KEY")
red = LED(17)
blue = PWMLED(27)
b = TonalBuzzer(22)

@anvil.server.callable
def red_toggle():
    red.toggle()

@anvil.server.callable
def red_blink():
    red.blink(0.5,0.5)

@anvil.server.callable
def blue_brightness(brightness):
    blue.value = brightness

@anvil.server.callable
def music():
    b.play(Tone("C4"))
    sleep(0.2)
    b.play(Tone("C4"))
    sleep(0.2)
    b.play(Tone("G4"))
    sleep(0.2)
    b.play(Tone("G4"))
    sleep(0.8)
    b.play(Tone("A4"))
    sleep(0.2)
    b.play(Tone("A4"))
    sleep(0.2)
    b.play(Tone("G4"))
    sleep(0.2)
    b.stop()




pause()
anvil.server.wait_forever()

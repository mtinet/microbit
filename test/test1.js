// A, B, A+B 버튼을 누르면 라디오 신호를 보내고 자신과 라디오를 받은 보드에 미리 정해진 색깔을 나오게 함

let item: neopixel.Strip = null
radio.onDataPacketReceived( ({ receivedNumber }) =>  {
    if (receivedNumber == 1) {
        item.showColor(neopixel.colors(NeoPixelColors.Red))
    }
    if (receivedNumber == 2) {
        item.showColor(neopixel.colors(NeoPixelColors.Green))
    }
    if (receivedNumber == 3) {
        item.showColor(neopixel.colors(NeoPixelColors.Blue))
    }
})
input.onButtonPressed(Button.A, () => {
    radio.sendNumber(1)
    item.showColor(neopixel.colors(NeoPixelColors.Red))
})
input.onButtonPressed(Button.B, () => {
    radio.sendNumber(2)
    item.showColor(neopixel.colors(NeoPixelColors.Green))
})
input.onButtonPressed(Button.AB, () => {
    item.showColor(neopixel.colors(NeoPixelColors.Blue))
    radio.sendNumber(3)
})
radio.setGroup(1)
item = neopixel.create(DigitalPin.P0, 10, NeoPixelMode.RGB)
item.setBrightness(1000)
item.setPixelColor(0, neopixel.colors(NeoPixelColors.Red))

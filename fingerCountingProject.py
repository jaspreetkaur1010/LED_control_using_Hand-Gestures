import pyfirmata

comport = 'COM3'
board = pyfirmata.Arduino(comport)

led_1 = board.get_pin('d:13:o')
led_2 = board.get_pin('d:12:o')
led_3 = board.get_pin('d:11:o')
led_4 = board.get_pin('d:10:o')
led_5 = board.get_pin('d:9:o')
led_6 = board.get_pin('d:6:o')
led_7 = board.get_pin('d:7:o')
led_8 = board.get_pin('d:3:o')
led_9 = board.get_pin('d:4:o')
# led_10 = board.get_pin('d:1:o')

def led(total):
    if total == 0:
        led_1.write(0)
        led_2.write(0)
        led_3.write(0)
        led_4.write(0)
        led_5.write(0)
        led_6.write(0)
        led_7.write(0)
        led_8.write(0)
        led_9.write(0)
        # led_10.write(0)
    elif total == 1:
        led_1.write(1)
        led_2.write(0)
        led_3.write(0)
        led_4.write(0)
        led_5.write(0)
        led_6.write(0)
        led_7.write(0)
        led_8.write(0)
        led_9.write(0)
        # led_10.write(0)
    elif total == 2:
        led_1.write(1)
        led_2.write(1)
        led_3.write(0)
        led_4.write(0)
        led_5.write(0)
        led_6.write(0)
        led_7.write(0)
        led_8.write(0)
        led_9.write(0)
        # led_10.write(0)
    elif total == 3:
        led_1.write(1)
        led_2.write(1)
        led_3.write(1)
        led_4.write(0)
        led_5.write(0)
        led_6.write(0)
        led_7.write(0)
        led_8.write(0)
        led_9.write(0)
        # led_10.write(0)
    elif total == 4:
        led_1.write(1)
        led_2.write(1)
        led_3.write(1)
        led_4.write(1)
        led_5.write(0)
        led_6.write(0)
        led_7.write(0)
        led_8.write(0)
        led_9.write(0)
        # led_10.write(0)
    elif total == 5:
        led_1.write(1)
        led_2.write(1)
        led_3.write(1)
        led_4.write(1)
        led_5.write(1)
        led_6.write(0)
        led_7.write(0)
        led_8.write(0)
        led_9.write(0)
        # led_10.write(0)
    elif total == 6:
        led_1.write(1)
        led_2.write(1)
        led_3.write(1)
        led_4.write(1)
        led_5.write(1)
        led_6.write(1)
        led_7.write(0)
        led_8.write(0)
        led_9.write(0)
        # led_10.write(0)
    elif total == 7:
        led_1.write(1)
        led_2.write(1)
        led_3.write(1)
        led_4.write(1)
        led_5.write(1)
        led_6.write(1)
        led_7.write(1)
        led_8.write(0)
        led_9.write(0)
        # led_10.write(0)
    elif total == 8:
        led_1.write(1)
        led_2.write(1)
        led_3.write(1)
        led_4.write(1)
        led_5.write(1)
        led_6.write(1)
        led_7.write(1)
        led_8.write(1)
        led_9.write(0)
        # led_10.write(0)
    elif total == 9:
        led_1.write(1)
        led_2.write(1)
        led_3.write(1)
        led_4.write(1)
        led_5.write(1)
        led_6.write(1)
        led_7.write(1)
        led_8.write(1)
        led_9.write(1)
        # led_10.write(0)
    # elif total == 10:
    #     led_1.write(1)
    #     led_2.write(1)
    #     led_3.write(1)
    #     led_4.write(1)
    #     led_5.write(1)
    #     led_6.write(1)
    #     led_7.write(1)
    #     led_8.write(1)
    #     led_9.write(1)
    #     led_10.write(1)

# Example usage:
# led(5)  # Turns on 5 LEDs
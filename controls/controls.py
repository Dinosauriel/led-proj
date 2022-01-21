import os
import select

# event interface:
# https://www.kernel.org/doc/html/latest/input/input.html#event-interface

# event codes:
# https://www.kernel.org/doc/html/latest/input/event-codes.html#input-event-codes
# https://github.com/torvalds/linux/blob/master/include/uapi/linux/input-event-codes.h

class XboxController():
    EV_KEY = 0x01

    EV_VALUE_KEYPRESS = 0x1
    EV_VALUE_KEYRELEASE = 0x0

    XBOX_A = 0x130
    XBOX_B = 0x131
    XBOX_Y = 0x134
    XBOX_X = 0x133

    XBOX_HOME = 0x13c

    def __init__(self) -> None:
        self.path = "/dev/input/event0"
        self.fd = os.open(self.path, os.O_RDONLY | os.O_NONBLOCK)

    def poll_buttons(self):
        buttons = {
            self.XBOX_A: False,
            self.XBOX_B: False,
            self.XBOX_Y: False,
            self.XBOX_X: False,

            self.XBOX_HOME: False
        }

        while True:
            ready, _, _ = select.select([self.fd], [], [], 0)
            if not ready:
                break
            buf = os.read(self.fd, 16)

            # sec = int.from_bytes(buf[:4], "little")
            e_type = int.from_bytes(buf[8:10], "little")
            e_code = int.from_bytes(buf[10:12], "little")
            e_value = int.from_bytes(buf[12:], "little")

            if e_type == self.EV_KEY:
                if e_value == self.EV_VALUE_KEYPRESS:
                    buttons[e_code] = True
                    # print(f"type: {e_type:08x}, code: {e_code:04x}, value: {e_value:04x}")
        return buttons

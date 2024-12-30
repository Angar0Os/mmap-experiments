import mmap
import time

filename = "hello.txt"

with open(filename, "r+b") as f:
    mm = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ)
    try:
        while True:
            mm.seek(0)
            data = mm.readline().decode().strip()
            print(data)
            time.sleep(1)
    except KeyboardInterrupt:
        print("Stopped reading.")
    finally:
        mm.close()
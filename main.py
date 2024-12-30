import mmap
import time

filename = "hello.txt"
initial_size = 1024

with open(filename, "wb") as f:
    f.write(b"0" + b" " * (initial_size - 1))

with open(filename, "r+b") as f:
    # Memory-map the file
    mm = mmap.mmap(f.fileno(), initial_size)
    i = 0
    try:
        while True:
            mm.seek(0)
            mm.write(f"{i}\n".encode())
            mm.flush()
            i += 1
            time.sleep(1)
    except KeyboardInterrupt:
        print("Stopped incrementing.")
    finally:
        mm.close()()
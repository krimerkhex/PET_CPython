import ctypes
import platform


def monotonic():
    if platform.system() == 'Windows':
        kernel32 = ctypes.windll.kernel32
        return kernel32.GetTickCount() / 1000.0
    elif platform.system() == 'Linux':
        libc = ctypes.CDLL('libc.so.6')
        timespec = ctypes.Structure('timespec',
                                    ('tv_sec', ctypes.c_long),
                                    ('tv_nsec', ctypes.c_long))
        ts = timespec()
        libc.clock_gettime(1, ctypes.byref(ts))
        return ts.tv_sec + ts.tv_nsec / 1e9
    elif platform.system() == 'Darwin':
        libc = ctypes.CDLL('libSystem.dylib')
        timespec = ctypes.Structure('timespec',
                                    ('tv_sec', ctypes.c_long),
                                    ('tv_nsec', ctypes.c_long))
        ts = timespec()
        libc.clock_gettime(5, ctypes.byref(ts))
        return ts.tv_sec + ts.tv_nsec / 1e9
    else:
        raise NotImplementedError("Unsupported platform")


if __name__ == "__main__":
    print(monotonic())

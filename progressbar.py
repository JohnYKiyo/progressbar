import sys, time
from IPython.display import display
from IPython.display import clear_output
class progbar:
    def __init__(self, period=100, bars=32,clear_display=True):
        self._period  = period
        self.bars     = bars
        self.active   = True
        self.start    = time.time()
        self.clear_disp = clear_display

    def dispose(self):
        if self.active:
            self.active = False
            self.update(self._period)
            sys.stdout.write("\n")

    def __del__(self):
        self.dispose()

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        self.dispose()

    def period(self):
        return self._period

    def update(self, tick,info=''):
        if self.clear_disp:
            clear_output()
        rate = tick / self._period

        # progress rate
        str = "{0:7d}% ".format(int(rate*100))

        # progress bar
        bar_prog = int(rate * self.bars)
        str += "|"
        str += "#" * (            bar_prog)
        str += "-" * (self.bars - bar_prog)
        str += "|"

        # calc end
        elapsed = time.time() - self.start
        predict = (elapsed * (1 - rate) / rate) if not rate == 0.0 else 0
        s = int(predict)
        m, s = divmod(s, 60)
        h, m = divmod(m, 60)
        d, h = divmod(h, 24)
        str += " {day}day{hour:3d}:{minute:02d}:{sec:02d}".format(day=d,hour=h,minute=m,sec=s)
#         sys.stdout.write("\r {}".format(str))
#         sys.stdout.flush()
        display("{0} {1}\n".format(str,info))

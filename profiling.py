import cProfile
import pstats
import time
from pprof import cpu
from line_profiler_pycharm import profile
# from memory_profiler import profile


# simple decorator for save profile stats to file
def profile_to_file(func):
    """Decorator for run function profile"""

    def wrapper(*args, **kwargs):
        profile_filename = f"Temp/{func.__name__}.prof"
        profiler = cProfile.Profile()
        result = profiler.runcall(func, *args, **kwargs)
        profiler.dump_stats(profile_filename)
        return result

    return wrapper


# @cpu
@profile
def pause_05():
    time.sleep(0.5)


# @cpu
@profile
def pause_02():
    time.sleep(0.2)


# @cpu
@profile
def main():
    for _ in range(10):
        pause_02()
    for _ in range(5):
        pause_05()
    count = 1000000
    while count > 0:
        count -= 1
    print('done!')


if __name__ == '__main__':
    #    cpu.auto_report()
    main()

# =================== Get stats with cProfile =================================

# Get basic stats:
# python -m cProfile -s time profiling.py
#
#    300 function calls (299 primitive calls) in 5.430 seconds
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#        15    4.507    0.300    4.507    0.300 {built-in method time.sleep}
#         1    0.923    0.923    5.430    5.430 profiling.py:26(main)
#        10    0.000    0.000    2.004    0.200 profiling.py:22(pause_02)
#         1    0.000    0.000    0.000    0.000 {built-in method marshal.loads}
#         5    0.000    0.000    2.503    0.501 profiling.py:18(pause_05)
#
# All time = 5.43 sec.
# 4.5 sec - for time.sleep form both functions
# 0.923 for loop in main func
# 2.004 for pause_02 func
# 2.503 for pause_05 func
#


# =========================== Save stats to file and open them ==========================
# save:
# python -m cProfile -o Temp/profiling.prof profiling.py
#
# save using decorator:
# Use @profile_to_file decorator and use it over profiled function

# open:
# import pstats
# p = pstats.Stats('Temp/profiling.prof')
# p.sort_stats('calls').print_stats()

# open in runsnakerun (draws picture with functions inside each other - didn't like)
# sudo apt install python3-wxgtk4.0
# pip install SquareMap RunSnakeRun    - did not work
# sudo apt install runsnakerun
# runsnake Temp/profiling.prof

# open in pyprof2calltree (looks much better, then runsnakerun) shows calls from functions in convenient way
# pip install pyprof2calltree
# pyprof2calltree -i Temp/profiling.prof -k

# ============================= profile each line of code ===================================
# pip install line_profiler
#
# write @profile decorators over functions to profile and run:
# kernprof -v -l profiling.py
#
# Function: pause_05 at line 17
#
# Line #      Hits         Time  Per Hit   % Time  Line Contents
# ==============================================================
#     17                                           @profile
#     18                                           def pause_05():
#     19         5    2502243.0 500448.6    100.0      time.sleep(0.5)
#
# Total time: 17.8443 s
# File: profiling.py
# Function: main at line 25
#
# Line #      Hits         Time  Per Hit   % Time  Line Contents
# ==============================================================
#     25                                           @profile
#     26                                           def main():
#     27        11         96.0      8.7      0.0      for _ in range(10):
#     28        10    2004316.0 200431.6     11.2          pause_02()
#     29         6         44.0      7.3      0.0      for _ in range(5):
#     30         5    2502455.0 500491.0     14.0          pause_05()
#     31         1          1.0      1.0      0.0      count = 10000000
#     32  10000001    6604277.0      0.7     37.0      while count > 0:
#     33  10000000    6733050.0      0.7     37.7          count -= 1
#     34         1         93.0     93.0      0.0      print('done!')
#

# ============= using pprof
# using pprof - working decoratros, better look, html won't open in snap (copy to mozilla)
# pip install pprof
#
# from pprof import cpu
# Add @cpu decorators to profiled functions
# Add cpu.auto_report() command to execution code
# file:///tmp/cpu_profile.html - won't open in snap, reopen it in firefox

# ============= Pycharm plugin
#
# the best way to profile, shows concurrency diagram, can work as cProfile and as line profiler
#
# settings -> install plugin (Line Profiler)
# install helper to project: pip install line-profiler-pycharm
# decorate functions with @profile
# top right buttons: profiler, line profiler or concurrency diagram


# ======================== memory profiling =================================
# pip install psutil memory_profiler
#
# from memory_profiler import profile
# decorate functions with @profile
# python -m memory_profiler profiling.py or just run code
# there are methods to save and plot data (mprof), there are features for multithreading
# https://coderzcolumn.com/tutorials/python/how-to-profile-memory-usage-in-python-using-memory-profiler


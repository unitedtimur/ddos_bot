# Import modules
import os
import sys
import argparse

# Go to current dir
from lib.Impulse.tools.method import AttackMethod

os.chdir(os.path.dirname(os.path.realpath(__file__)))


def api_flood(number, time, threads) -> AttackMethod:
    return AttackMethod(duration = time, name = "SMS", threads = threads, target = number)

threads_ddos = dict()
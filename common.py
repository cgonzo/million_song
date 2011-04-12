#!/usr/bin/python

import unittest
import sys
import re

def ununicode(v):
  """
  If we're given a unicode object,
  encodes as utf-8.  Leaves strings alone.
  """
  if isinstance(v, unicode):
    return v.encode("utf-8")
  return v

def emit(key, value):
  """
  Emits a key->value pair in tab-delimited form.  Key and value should be strings.
  """
  key = ununicode(key)
  value = ununicode(value)
  out = sys.stdout

  out.write(key)
  out.write("\t")
  out.write(value)
  out.write("\n")

def run_map(map, input):
  """Calls map() for each input value."""
  for line in input:
    line = line.rstrip()
    for key, value in map(line):
      emit(key, value)

def run_reduce(reduce, input):
  """Gathers reduce() data in memory, and calls reduce()."""
  prev_key = None
  values = []
  for line in input:
    key, value = re.split("\t", line, 1)
    value = value.rstrip()
    if prev_key == key:
      values.append(value)
    else:
      if prev_key is not None:
        for k, v in reduce(prev_key, values):
          emit(k, v)
      prev_key = key
      values = [ value ]

  if prev_key is not None:
    for k, v in reduce(prev_key, values):
      emit(k, v)

def main(map, reduce):
  """Runs map or reduce code, per arguments."""
  if len(sys.argv) not in (2, 3) or sys.argv[1] not in ("map", "reduce", "test"):
    print "Usage: %s <map|reduce|test> [inputfile]" % sys.argv[0]
    sys.exit(1)
  if sys.argv[1] == "map":
    if len(sys.argv) == 3:
      run_map(map, file(sys.argv[2]))
    else:
      run_map(map, sys.stdin)
  elif sys.argv[1] == "reduce":
    if len(sys.argv) == 3:
      run_reduce(reduce, file(sys.argv[2]))
    else:
      run_reduce(reduce, sys.stdin)
  elif sys.argv[1] == "test":
    sys.argv.pop(1)
    unittest.main()
  else:
    assert False

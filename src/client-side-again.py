#!/usr/bin/env python3

"""
Aiming to solve 'client-side-again'

Need to pull in the arrary resort function
"""

_0x5a46 = [
	'37115}',
	'_again_3',
	'this',
	'Password Verified',
	'Incorrect password',
	'getElementById',
	'value',
	'substring',
	'picoCTF{',
	'not_this'
]

def _0x4b5b()






text = """
  if (checkpass["substring"](0, split * 2) == "picoCTF{") {
    if (checkpass["substring"](7, 9) == "{n") {
      if (checkpass["substring"](split * 2, split * 2 * 2) == "not_this") {
        if (checkpass["substring"](3, 6) == "oCT") {
          if (checkpass["substring"](split * 3 * 2, split * 4 * 2) == "55670}") {
            if (checkpass["substring"](6, 11) == "F{not") {
                if (checkpass["substring"](12, 16) == "this") {
              if (checkpass["substring"](split * 2 * 2, split * 3 * 2) == "_again_0") {
"""

flag = [None] * 32
split = 4
for line in text.split("\n"):
    line = line.strip()
    if line == "": 
        continue
    line = line.replace('if (checkpass["substring"](', 'flag[').replace(', ', ":").replace(') == ', '] = ').replace(') {', '')
    exec(line)

print "".join(flag)
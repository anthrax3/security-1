import os
import shutil

path = '.'

wordlists = []
# r=root, d=directories, f = files
for r, d, f in os.walk(path):
  for file in f:
    if file.endswith('.txt'):
      wordlists.append(os.path.join(r, file))

for wordlist in wordlists:
  if os.path.basename(wordlist) in [
    'wordlist_birthday.txt',
    'wordlist_birthday_extended.txt',
    'wordlist_birthday_dmy.txt',
    'wordlist_birthday_dmy_extended.txt',
  ]:
    continue
  message = '\nSanitizing ' + os.path.basename(wordlist)
  if os.path.basename(wordlist).endswith('_unordered.txt'):
    message += ' (Unordered wordlist)'
  print(message)
  wordlist_sanitized = wordlist + '.tmp'
  lines = []
  tmpfile = open(wordlist_sanitized, "w")
  for line in open(wordlist, "r"):
    if line.strip() != '' and line.strip() + '\n' not in lines:
      lines.append(line.strip() + '\n')
  if wordlist.endswith('_unordered.txt'):
    tmpfile.writelines(lines)
  else:
    tmpfile.writelines(sorted(lines))
  tmpfile.close()
  shutil.copy(wordlist_sanitized, wordlist)
  os.remove(wordlist_sanitized)

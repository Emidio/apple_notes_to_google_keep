# Import a directory of text files as Google Keep notes.
# Text file name is used for the title of the note.

import gkeepapi, os, codecs

username = 'your@google.email.here' # insert your Google username (email) here
master_token = 'aas_et/your-master-token-here' # insert your master token here

keep = gkeepapi.Keep()
success = keep.authenticate(username,master_token)
dir_path = os.path.dirname(os.path.realpath(__file__))
for fn in os.listdir(dir_path):
	if os.path.isfile(fn) and fn.endswith('.txt'):
		with codecs.open(fn, 'r', encoding='utf-8', errors='ignore') as mf:
			data=mf.read()
			keep.createNote(fn.replace('.txt',''), data)
			keep.sync();


#!/usr/bin/python

import sys, os, shutil

def main():
	if len(sys.argv) != 3:
		print("Usage: pic_import_org <source directory> <destination directory>")
		exit(1)

	src = sys.argv[1]
	dest = sys.argv[2]

	srcBad = not os.path.isdir(src)
	destBad = not os.path.isdir(dest)

	if srcBad:
		print("Source directory '%s' does not exist." % src)
	if destBad:
		print("Destination directory '%s' does not exist." % dest)
	if srcBad or destBad:
		exit(1)

	srcFiles = os.listdir(src)
	
	destDirs = dict()

	for f in srcFiles:
		lastDash = f.rindex("-")
		prefix = f[:lastDash-1].strip()
		if prefix in destDirs:
			destDirs[prefix].append(f)
		else:
			destDirs[prefix] = [f]
		
	#print(destDirs.keys())
	#exit(0)
	
	for d in destDirs.keys():
		dir = os.path.join(dest, d)
		print("Creating directory '%s" % dir)
		os.makedirs(dir)

		files = destDirs[d]
		for f in files:
			lastDash = f.rindex("-");
			dst = f[lastDash+1:].strip()
			print("  Copying %s to %s" % (dst, d))
			cpSrc = os.path.join(src, f)
			cpDest = os.path.join(dir, dst)
			print("copy source '%s' copy dest '%s'" % (cpSrc, cpDest))
			shutil.copy(cpSrc, cpDest)

if __name__ == "__main__":
	main()
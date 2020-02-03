import re, os, sys, glob
import subprocess, shlex
import csv
from subprocess import STDOUT, check_output
import ntpath

folder = 'Assignment 2_a_/'
custom_input = b"56 58 1 33\n"
# _required_files = ['encode.txt', 'log.txt', 'decode.txt']
_required_files = []
required_files = [os.path.join(folder, f) for f in _required_files]

# pat_rolls = r"(18ME10055)|(18ME10070)|(18ME30009)|(18ME30024)|(18ME30039)|(18ME30054)|(18MF10014)|(18MF10029)|(18MF3IM10)|(18MI10008)|(18MI10023)|(18MI10038)"
# pat_rolls = r"(18MF3IM10)|(18MI10008)|(18MI10023)|(18MI10038)"
# pat_rolls = r"[0-9]{2}[A-Z]{2}.{5}"
pat_rolls = r"shivam.lahoti|sreeya.chilupuri|shree.harsha.kodi|rahul.choudhary|bhargavi.adusumilli|dedipya.yalam|shivani.soren|badri.visaal.avvaru|rahul.nath|soham.zade"
# pat_rolls = r"sreeya.chilupuri"

flist = os.listdir(folder)
# print(flist)
for i, fx in enumerate(flist):
	if not os.path.isdir(os.path.join(folder, fx)):
		if fx in _required_files:
			continue
		matched = False
		m_all = list(re.finditer(pat_rolls, fx, re.MULTILINE | re.IGNORECASE))

		if len(m_all) > 0:
			for m in m_all:
				matched = True
				l, r = m.span()
				roll = fx[l:r]
				rest_fname = fx[r:]
			print(fx)

		if not matched:
			os.system(f'rm "{folder}{fx}"')

		if matched:
			new_folder = f'"{folder}{roll}/"'.upper()
			old_path = f'"{folder}{fx}"'
			mkdir_cmd = f'mkdir -p {new_folder}'
			mv_cmd = f'mv {old_path} "{folder}{roll.upper()}/{roll.upper() + rest_fname}"'
			#exe_path = f'\"{folder}{fx}\"'

			# print(old_path)
			# print(new_folder)
			print(mkdir_cmd)
			print(mv_cmd)
			os.system(mkdir_cmd)
			os.system(mv_cmd)
			for eff in required_files:
				os.system(f'cp {eff} \"{folder}{roll.upper()}\"')

	print(f"Count {i}", end='\r')		

## Compile and execute
flist = os.listdir(folder)
# flist = list(map(lambda x: re.sub('[()]', '', x), pat_rolls.split('|')))

results = {}
def dict_to_csv(D, fname):
	fields = []
	for roll, d in D.items():
		for k in d:
			fields.append(k)

	fields = list(set(fields))
	try:
		fields.remove("Roll")
		fields.remove("Name")
	except ValueError:
		pass

	fields = ["Roll", "Name"] + fields
	with open(fname, 'w') as fh:
		csvh = csv.writer(fh)
		csvh.writerow(fields)
		for roll, d in D.items():
			csvh.writerow([d[f] if f in d else 'NA' for f in fields])
				

f_devnull = open(os.devnull,"w")
f_md = open(f'{folder.replace("/", "")}.md'.replace(" ", ""), "w")
marks_all = []
for fx in flist:
	print()
	print(f"===================    ROLL : {fx}   =======================")
	print()
	f_md.write(f"## ROLL: {fx}\n")
	roll_folder = os.path.join(folder, fx)
	if os.path.isdir(roll_folder):
		result = {}
		result['Roll'] = fx
		# flag = input(f'Check {fx}? [y]yes,s(skip):')
		# if flag=='s':
		# 	continue
		for src_fx in glob.glob(roll_folder + '/*.c'):
			#src_path = os.path.join(roll_folder, src_fx)
			src_path = src_fx
			print(f'SRC: {src_path}')
			with open(src_path) as src_code:
				f_md.write(f"### {src_path}\n")
				f_md.write("```C++\n")
				f_md.write(src_code.read())
				f_md.write("\n```\n")
			# exe_path = re.sub(r'[ ]+', '_', exe_path)
			Px = re.search(r"(.+)\.c$", src_path).group(1)
			_exe_path = re.search(r".+\.c(pp)?$", src_path, re.IGNORECASE).group()
			l_exe_path = re.sub(r'\.c(pp)?', '.out', _exe_path)
			#print(src_path, exe_path, Px)
			exe_path = os.path.join(l_exe_path)
			print(f'EXE: {exe_path}')
			# p = subprocess.Popen(shlex.split(f"gcc -lm \"{src_path}\" -o {exe_path}"), stdout=f_devnull, stderr=f_devnull)
			if '.cpp' in src_path:
				p = subprocess.Popen(shlex.split(f'g++ "{src_path}" -lm -o "{exe_path}"'), stdout=sys.stdout, stderr=f_devnull)
			else:
				p = subprocess.Popen(shlex.split(f'gcc "{src_path}" -lm -o "{exe_path}"'), stdout=sys.stdout, stderr=f_devnull)
			err_code = p.wait()
			if err_code != 0:
				result[f'{Px}.compile'] = 'Failed'
				print('FAILED')
			else:
				result[f'{Px}.compile'] = 'Success'
				print('SUCCESS')

				# p = subprocess.Popen(shlex.split(f"./{exe_path}"), stdout=sys.stdout, stderr=f_devnull)
				# run_err_code = p.wait()
				# if run_err_code == 0:
				# 	result[f'{Px}.run'] = 'Success'
				# else:
				# 	result[f'{Px}.run'] = 'Failed'

				# wd = os.getcwd()
				# os.chdir(roll_folder)

				# try:
				# 	output = check_output([f"./{ntpath.basename(l_exe_path)}"], stderr=STDOUT, timeout=10, cwd=roll_folder)
				# 	result[f'{Px}.run'] = 'Success'
				# 	# print(output.decode())
				# except subprocess.CalledProcessError as e:
				# 	if e.returncode == -11:
				# 		result[f'{Px}.run'] = 'Segfault'
				# 	else:
				# 		result[f'{Px}.run'] = 'Failed'
				# 	print(e)
				# except subprocess.TimeoutExpired as e:
				# 	print(e)
				# 	result[f'{Px}.run'] = 'Inf.Loop'
				# except UnicodeDecodeError as e:
				# 	print(e)

				p = subprocess.run([f'./{l_exe_path}'], stdout=subprocess.PIPE, input=custom_input)
				if p.stdout is not None:
					print("\nOUTPUT:")
					print(p.stdout.decode(u'utf-8'))
				if p.stderr is not None:
					print("\nERROR:")
					print(p.stderr.decode(u'utf-8'))
				# while(1):
				# 	p = subprocess.Popen(['xterm', '-hold', '-e', f'"./{l_exe_path}"'], stdin=subprocess.PIPE)
					# if custom_input is not None:
					# 	p.stdin.write(custom_input)
					# 	p.communicate()
					# flag = input('Repeat Test y,[n]:')
					# if flag != 'y':
					# 	break
				
				# p.wait()
				# p = subprocess.Popen(shlex.split(f"./{exe_path}"), stdout=sys.stdout, stderr=sys.stderr, shell=True)
				# err_code = p.wait()
				# print(f'Enter Marks: {exe_path}')
				# score = input()
				# marks_all.append(f"{fx},{exe_path},{int(score)}")
		
		results[fx] = result
		# flag = input('Continue? [y]yes,e(exit):')
		# if flag=='e':
		# 	break
f_devnull.close()
f_md.close()
dict_to_csv(results, 'A5.csv')
# grade_fh = open(folder.replace("/", "") + '.csv', 'w')
# grade_csv = csv.writer(grade_fh)
# grade_csv.writerow([
# 	"Roll",
# 	"Name", 
# 	"",
# 	])

# import datetime
# dt = datetime.datetime.now()
# outf = f"{dt.date()}-{dt.hour}-{dt.minute}-{dt.second}.csv"
# with open(outf, 'w') as fw:
# 	for r in marks_all:
# 		fw.write(r + '\n')


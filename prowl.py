#Importing Libs##########
from bs4 import BeautifulSoup
import urllib2
from itertools import izip
import string
#########################

URLS = []
EMAILS = []

target = open("output.txt", 'w')
q=0
global fill

#Menu####################
while True:
	print (30 * '-')
	print ("   M A I N - M E N U")
	print (30 * '-')
	print ("1. Grab Linkedin Data")
	print ("2. Email Enumeration")
	print ("3. Username Enumeration")
	print (30 * '-')
	 
	## Get input ###
	choice = raw_input('Enter your choice [1-3] : ')
	 
	### Convert string to int type ##
	choice = int(choice)
	 
	### Take action as per selected menu-option ###
	if choice == 1:
		#Defining Search Variables
		link = raw_input("Enter Base Linkedin Profile: ")
		Org = raw_input("What company are you searching for?: ")

		##########################

		print "---------------------------------------"
		print "Searching for " + Org
		print "----------------------------------------"

		def greppage(link, Org, URLS):

			x=1
			
			#Setting User Agent#######
			header = {'User-Agent': 'Mozilla/5.0'} #Needed to prevent 403 error on Wikipedia
			##########################
				#Making HTTP req##########
		        req = urllib2.Request(link,headers=header)
		        page = urllib2.urlopen(req)
		        soup = BeautifulSoup(page, "lxml")
		        ##########################
			name = soup.select("div.insights-browse-map > ul > li > h4 > a")
			company = soup.select("div.insights-browse-map > ul > li > p.browse-map-title")

			#YOU CAN READD 
			
			while x == 1: 
				global PRINT
				PRINT = []
				list1 = []
				list2 = []
				list3 = []
				global sdf


				for i in name:
					list1.append(i.getText())	
					list3.append(i['href'])
						
				for c in company: 
					list2.append(c.getText() + ",")

				for item in izip(list1, list2, list3):
					#print item
					if Org in item[1]:	
						if item[2] not in URLS:
							#print item[0]+ "	" + item[1]+ "	" +item[2]
							URLS.append(item[2])
							EMAILS.append(item[0])
							pre=(item[0]+ "	" + item[1]+ "	" +item[2])
							sdf = filter(lambda x: x in string.printable, pre)
							PRINT.append(sdf)			
				x+=1

		greppage(link, Org, URLS)

		for iturl in URLS:
			greppage(iturl, Org, URLS)
			for full in PRINT:
				q+=1
				s = str(q) + ": " + full
				print s
				target.write(s + "\n")
			#print URLS        

	elif choice == 2:
		emailhost = raw_input("What is the organisations hostname?: ")

		print (30 * '-')
		print ("1: firstname + lastname@" + emailhost)
		print ("2: firstname + . + lastname@" + emailhost)
		print ("3: lastname + firstname@" + emailhost)
		print ("4: lastname + . + firstname@" + emailhost)
		print ("5: firstname - firstletter + lastname@" + emailhost)
		print ("6: lastname + firstname - firstletter@" + emailhost)
		print ("7: lastname - firstletter + firstname@" + emailhost)
		print ("8: firstname + lastname - lastletter@" + emailhost)

		print (30 * '-')
		 
		## Get input ###
		choice = raw_input('Enter your choice : ')
		 
		### Convert string to int type ##
		choice = str(choice)
		 
		### Take action as per selected menu-option ###
		if choice == "1":
		        for i in EMAILS:
	        		prefix = i.split()
	        		print prefix[0]+prefix[1]+emailhost
		elif choice == "2":
		        print "firstname+.+lastname@" + emailhost
		        for i in EMAILS:
		        	prefix = i.split()
		        	print prefix[0]+ "." + prefix[1]+emailhost
		elif choice == "3":
		        print "lastname+firstname@" + emailhost
			for i in EMAILS:
		        	prefix = i.split()
		        	print prefix[1]+prefix[0]+emailhost
		elif choice == "4":
		        print "lastname+.+firstname@" + emailhost
		        for i in EMAILS:
		        	prefix = i.split()
		        	print prefix[1]+ "." + prefix[0]+emailhost
		elif choice == "5":
		        print "firstname-firstletter+lastname@" + emailhost
		        for i in EMAILS:
		        	prefix = i.split()
		        	print prefix[0][0]+ "." + prefix[1]+emailhost
		elif choice == "6":
		        print "lastname+.+firstname-firstletter@" + emailhost
		        for i in EMAILS:
		        	prefix = i.split()
		        	print prefix[1]+ "." + prefix[0][0]+emailhost
		elif choice == "7":
		        print "lastname-firstletter+firstname@" + emailhost
		        for i in EMAILS:
		        	prefix = i.split()
		        	print prefix[1][0]+ "." + prefix[0]+emailhost
		elif choice == "8":
		        print "firstname+.+lastname-firstletter@" + emailhost
		        for i in EMAILS:
		        	prefix = i.split()
		        	print prefix[0]+ "." + prefix[1][0]+emailhost

		else:    ## default ##
		        print ("Invalid number. Try again...")
	elif choice == 3:
	        print ("Rebooting the server...")
	else:    ## default ##
	        print ("Invalid number. Try again...")
	###########################




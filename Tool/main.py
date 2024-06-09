import argparse
from includes import act,file,check
from units import banner,network

parser=argparse.ArgumentParser()
parser.add_argument("-u","--url",help="Enter the url (without parameter to check)" )
parser.add_argument("-i","--input",help="Enter input file name")
parser.add_argument("-up","--urlp",help="Enter the url (with parameter to check)")
args=parser.parse_args()

def main():
    if args.urlp:
        banner.banner()
        redirect_url = "https://github.com/Prasathappy"
        act.Open_redirect(args.urlp,redirect_url)

    if args.input:
        banner.banner()
        file.reader(args.input)
    
    if args.url:
        banner.banner()
        redirect_url = "https://github.com/Prasathapp"
        if check.Open_Redirect(args.url, redirect_url):
            print(f"The URL {args.url} is vulnerable to an open redirect attack.")
        else:
            print(f"The URL {args.url} is not vulnerable to an open redirect attack.")
            

if __name__ == "__main__":
    if network.net():
        main()
    else:
        print("\ncheck internet")

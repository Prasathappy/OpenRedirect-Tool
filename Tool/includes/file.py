from includes import act
def reader(input):
    try:
        redirect_url = "https://github.com/Prasathappy"
        with open(input,'r') as file:
            for line in file:
                act.Open_Redirect(line.strip(),redirect_url)
    except FileNotFoundError:
        print("File not found. check the file paath and name.")

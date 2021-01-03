import random
import string

winext = "dada"
windom = "dadad"


def generate_email(email_amount, mail=None, min=5, max=20):
    extensions = ['com', 'net', 'org', 'gov']
    domains = ['gmail', 'yahoo', 'comcast', 'verizon',
               'charter', 'hotmail', 'outlook', 'frontier', 'web']

    winext = extensions[random.randint(0, len(extensions)-1)]
    windom = domains[random.randint(0, len(domains)-1)]

    acclen = random.randint(min, max)

    global winacc

    #if winacc == None:
        #winacc = ''.join(random.choice(string.ascii_lowercase + string.digits + string.ascii_uppercase)
        #                 for _ in range(acclen))
    f = open('email.txt')
    first_line = f.readline()
    mail = first_line
    email_amount + 1
        #global winacc
    winacc = "" + mail + "+" + str(n)
    #else:
        #print("Error whilst generating mail")

    finale = winacc + "@" + windom + "." + winext
    print(finale)
    return finale
#from random_username.generate import generate_username
import random
import string

def generate_password(stringLength=8):
    lettersAndDigits = string.ascii_letters + string.digits
    return ''.join((random.choice(lettersAndDigits) for i in range(stringLength)))


def generate_email(mail=None, min=5, max=20):
    extensions = ['com', 'net', 'org', 'gov']
    domains = ['gmail', 'yahoo', 'comcast', 'verizon',
               'charter', 'hotmail', 'outlook', 'frontier', 'web']

    f = open('email.txt')
    lines = f.readlines()


    #winext = extensions[random.randint(0, len(extensions)-1)]
    #windom = domains[random.randint(0, len(domains)-1)]
    #windom = lines[1]
    #winext = lines[2]
    domain = lines[1]

    #acclen = random.randint(min, max)

    email_n = open('temp_mail.txt', 'r')
    line = email_n.readline()
    print('LINE:' + line)
    current_mails = int(line)
    
    #f = open('email.txt')
    #first_line = f.readline()
    mail = lines[0]
    
    winacc = "" + mail + "+" + str(current_mails)
  

    finale = winacc + "@" + domain#windom + "." + winext
    print(finale)
    current_mails += 1
    print('CURRENT MAILS:' + str(current_mails))
    line = str(current_mails)
    email_n = open('temp_mail.txt', 'w')
    email_n.writelines(line)
    return finale


def generate_sentence():
    nouns = ("puppy", "car", "rabbit", "girl", "monkey", "dog", "cat", "cow", "sheep", "rabbit",
             "duck", "hen", "horse", "pig", "turkey", "chicken", "donkey", "goat", "guinea pig", "llama")
    verbs = ("runs", "hits", "jumps", "drives", "barfs", "demands", "breeds", "hopes",
             "tops", "sounds", "rests", "shoots", "costs", "writes", "tastes", "supplies")
    adv = ("crazily.", "dutifully.", "foolishly.", "merrily.", "occasionally.",
           "nervously.", "rigidly.", "instantly.", "innocently.", "warmly.", "beautifully.", "simply.", "reassuringly.")
    adj = ("adorable", "clueless", "dirty", "odd", "stupid", "private", "fanatical",
           "pleasant", "common", "dead", "rude", "political", "sable", "colossal", "therapeutic", "maniacal", "lonley", "nutty", "light", "snotty", "calm", "vivacious")

    l = [nouns, verbs, adj, adv]
    sentence = " ".join([random.choice(i) for i in l])
    return sentence


class DiscordAccount():
    token = None
    email = None
    username = generate_sentence()
    password = None

    def __init__(self):
        pass

    def generate_random_credentials(self):
        self.username = generate_sentence()
        self.email = generate_email()
        self.password = generate_password(10)
        self.welcome_message = generate_sentence()
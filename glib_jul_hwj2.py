# task 1
import re
def find_pattern(text):
    return re.findall(r'R[b]+r', text)

# task 2
import re
def valid_card(card_number):
    return bool(re.match(r'^\d{4}-\d{4}-\d{4}-\d{4}$', card_number))

# task 3
import re
def valid_email(email):
    pattern = r'^[A-Za-z0-9]+[A-Za-z0-9_-]*@[A-Za-z0-9]+\.[A-Za-z]{2,}$'
    return re.match(pattern, email) and '--' not in email

# task 4
import re
def valid_login(login):
    pattern = r'^[A-Za-z0-9]{2,10}$'
    return re.match(pattern, login) is not None
"""Happy new month guys!💯❤️

My Heart fill message to you! 💌

Get on your IDE and enjoy the fun! 😊"""

class Months:
    def get_month(self, user_input):
        months = {'1':'January',
                  '2':'February',
                  '3':'March',
                  '4':'April',
                  '5':'May',
                  '6':'June',
                  '7':'July',
                  '8':'August',
                  '9':'September',
                  '10':'October',
                  '11':'November',
                  '12':'December'}
   
    
        for key in months.keys():
            if user_input == key:
                return f"""Welcome to {months.get(user_input)}! 🌹
You are an amazing programmer, keep coding.✌️💯♥️"""


month = Months()
message = month.get_month(input('Choose month 1-12'))
print(message)

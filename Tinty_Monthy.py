"""Happy new month guys!💯❤️

My Heart fill message to you! 💌

Get on your IDE and enjoy the fun! 😊"""

class Months:

    def get_month(self, number):

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

                  '12':'December'

                      }

        for key in months():

            if key == number:

                return f"""Welcome to {months[key]}! 🌹

You are an amazing programmer, keep coding✌️💯♥️

Kindly follow my IG @mikkystechs...I've got some free packages for you on my bio."""

         

month = Months

output = month.get_month(input('Choose month 1-12: '))

print(output)

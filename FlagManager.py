from constants import PAGE_STEP
import math

class FlagManager(object):
    def __init__(self):
        self.list_of_flags = ['Afghanistan', 'Albania', 'Algeria', 'Andorra', 'Angola', 'Antigua-Barbuda', 'Argentina', 'Armenia', 'Australia', 'Austria', 'Azerbaijan', 'Bahamas', 'Bahrain', 'Bangladesh', 'Barbados', 'Belarus', 'Belgium', 'Belize', 'Benin', 'Bhutan', 'Bolivia', 'Bosnia and Herzegovina', 'Botswana', 'Brazil', 'Brunei', 'Bulgaria', 'Burkina Faso', 'Burundi', 'Cambodia', 'Cameroon', 'Canada', 'Cape-Verde-Islands', 'Central-African-Republic', 'Chad', 'Chile', 'China', 'Colombia', 'Comorro-Islands', 'Congo', 'Costa-Rica', 'Croatia', 'Cuba', 'Cyprus', 'Czech Republic', 'Denmark', 'Djibouti', 'Dominica', 'Dominican-Republic', 'DR Congo', 'East Timor', 'Ecuador', 'Egypt', 'El-Salvador', 'Equatorial-Guinea', 'Eritrea', 'Estonia', 'Ethiopia', 'F.S. Micronesia', 'Fiji', 'Finland', 'France', 'Gabon', 'Gambia', 'Georgia', 'Germany', 'Ghana', 'Greece', 'Grenada', 'Guatemala', 'Guinea', 'Guinea-Bissau', 'Guyana', 'Haiti', 'Honduras', 'Hungary', 'Iceland', 'India', 'Indonesia', 'Iran', 'Iraq', 'Ireland', 'Israel', 'Italy', 'Jamaica', 'Japan', 'Jordan', 'Kazakhstan', 'Kenya', 'Kiribati', 'Kuwait', 'Kyrgyzstan', 'Laos', 'Latvia', 'Lebanon', 'Lesotho', 'Liberia', 'Libya', 'Liechtenstein', 'Lithuania', 'Luxembourg', 'Madagascar', 'Malawi', 'Malaysia', 'Maldive-Islands', 'Mali', 'Malta', 'Marshall Islands', 'Mauritania', 'Mauritius', 'Mexico', 'Moldova', 'Monaco', 'Mongolia', 'Montenegro', 'Morocco', 'Mozambique', 'Myanmar', 'Namibia', 'Nauru', 'Nepal', 'Netherlands', 'New-Zealand', 'Nicaragua', 'Niger', 'Nigeria', 'North-Korea', 'North Macedonia', 'Norway', 'Oman', 'Pakistan', 'Palau', 'Palestine', 'Panama', 'Papua-New-Guinea', 'Parguay', 'Peru', 'Philippines', 'Poland', 'Portugal', 'Qatar', 'Romania', 'Russia', 'Rwanda', 'Saint-Kitts-Nevis', 'Saint-Lucia', 'Saint Vincent and the Grenadines', 'Samoa', 'San-Marino', 'Sao-Tome', 'Saudi-Arabia', 'Senegal', 'Serbia', 'Seychelles', 'Sierra-Leone', 'Singapore', 'Slovakia', 'Slovenia', 'Soloman-Islands', 'Somalia', 'South-Africa', 'South-Korea', 'South Sudan', 'Spain', 'Sri-Lanka', 'Sudan', 'Surinam', 'Sweden', 'Switzerland', 'Syria', 'Tajikistan', 'Tanzania', 'Thailand', 'Togo', 'Tonga', 'Trinidad-Tobago', 'Tunisia', 'Turkey', 'Turkmenistan', 'Tuvalu', 'Uganda', 'Ukraine', 'United Arab Emirates', 'United Kingdom', 'United States', 'Uruguay', 'Uzbekistan', 'Vanuatu', 'Vatican-City', 'Venezuela', 'Vietnam', 'Yemen', 'Zambia', 'Zimbabwe', 'Taiwan', 'Kosovo', 'Northern Cyprus', 'Western Sahara']

    def get_current_flags_page(self, page):
        if((page*PAGE_STEP)>=len(self.list_of_flags)):
            return self.list_of_flags[((page - 1) * PAGE_STEP):(len(self.list_of_flags)-1)]
        return self.list_of_flags[((page-1)*PAGE_STEP):(page*PAGE_STEP)]

    def get_possible_pages_number(self):
        return math.ceil((len(self.list_of_flags)*1.0/PAGE_STEP))

    def get_next_question(self, number):
        if number == 1:
            return "Question 1"
        elif number == 2:
            return "Question 2"
        elif number == 3:
            return "Question 3"
        elif number == 4:
            return "Question 4"
        elif number == 5:
            return "Question 5"
        elif number == 6:
            return "Question 6"
        elif number == 7:
            return "Question 7"
        elif number == 8:
            return "Question 8"
        elif number == 9:
            return "Question 9"
        else:
            return "END"


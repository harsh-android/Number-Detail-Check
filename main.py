import phonenumbers
from test import number

# Get Country Name
from phonenumbers import geocoder
ch_number = phonenumbers.parse(number , "CH")
print(geocoder.description_for_number(ch_number,"en"))

# Get Provider Name
from phonenumbers import carrier
service_number = phonenumbers.parse(number , "RO")
print(carrier.name_for_number(service_number, "en"))

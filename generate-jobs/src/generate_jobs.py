import requests
import json

INDEED_REQUEST = 'http://api.indeed.com/ads/apisearch?publisher=3922021424492903&v=2&format=json&co=ca&q=software&limit=100'
GEOCODE_REQUEST = 'https://maps.googleapis.com/maps/api/geocode/json?key=AIzaSyD1EiOv9PGqo-At2h6d8icLYkXRmktEQSs'
CITIES = ['Toronto', 'Vancouver', 'Calgary', 'Edmonton', 'Ottawa', 'Winnipeg', 'Hamilton', 'Regina', 'Halifax']


"""
download virtualenv, enable it
pip install requests
"""

# clean the json output pulled from indeed.com in the format of
# 		{
# 			"jobtitle": "Manual QA Analyst",
# 			"company": "Sensibill Inc.",
# 			"city": "Toronto",
# 			"state": "ON",
# 			"country": "CA",
# 			"date": "Wed, 11 Jan 2017 19:46:48 GMT",
# 			"snippet": "Strong understanding of the <b>software</b> development lifecycle and Quality Assurance methodologies. Sensibill is lighting up the FinTech industry with mobile...",
# 			"url": "http://ca.indeed.com/viewjob?jk=d4db0ea48df42a9e&qd=KEq_hGa0y5uPZdwnEcYeLdAg0ySErqMqt7VKtCVXqFc13IcQriasRiJZSXao_VXhxx8maxP9dOomzJMbZZe-eU3YYs_aCfgMYjO9kdVJgEMkt0LCVy_rQinuMfW47e_m&indpubnum=3922021424492903&atk=1b71bf9f8agkk94v",
# 			"jobkey": "d4db0ea48df42a9e",
# 		}
def clean_json(raw_json):

	# print(type(raw_json))

	# decoded_json = json.loads(raw_json)
	
	output = []

	for job_entry in raw_json['results']:
		job_entry_json = {}

		job_entry_json['jobtitle'] = job_entry['jobtitle']
		job_entry_json['company'] = job_entry['company']
		job_entry_json['city'] = job_entry['city']
		job_entry_json['state'] = job_entry['state']
		job_entry_json['country'] = job_entry['country']
		job_entry_json['date'] = job_entry['date']
		job_entry_json['snippet'] = job_entry['snippet']
		job_entry_json['url'] = job_entry['url']
		job_entry_json['jobkey'] = job_entry['jobkey']

		output.append(job_entry_json)

	print(json.dumps(output))
	return json.dumps(output)

def encode_url(company_name):
	result = ''
	for char in company_name:
		if char == ' ':
			result += '%20'
		elif char == "'":
			result += '%27'
		else:
			result += char
	return result

def in_city(address_components, city):
	for component in address_components:
		if component['long_name'] == city:
			return True
	return False


if __name__ == "__main__":

	for city in CITIES:

		file = open("cities/" + city + ".csv", "w")
		company_list = []

		indeed_resp = requests.get(INDEED_REQUEST + '&l=' + city)
		
		for posting in indeed_resp.json()['results']:

			print posting['company'] + ', ' + city
			company_name = encode_url(posting['company'])
			geocode_resp = requests.get(GEOCODE_REQUEST + '&address=' + company_name)
			json = geocode_resp.json()['results']

			if json:
				location = json[0]['geometry']['location']

				lat = location['lat']
				lng = location['lng']

				# check if googe maps returns something that's in toronto
				if in_city(json[0]['address_components'], city):

					# do not add duplicates
					if posting['company'] not in company_list:
						company_list.append(posting['company'])

						try:
							file.write('{}, {}, {}\n'.format(posting['company'], lat, lng))
						except UnicodeEncodeError:
							pass






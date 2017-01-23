import requests
import json

"""
download virtualenv, enable it
pip install requests
"""

url = 'http://api.indeed.com/ads/apisearch?publisher=3922021424492903&v=2&format=json&co=ca&q=software&l=Toronto%2C+ON&limit=100'
resp = requests.get(url)

# print(resp.json())

# print(resp.status_code)
# print(resp.json())


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

	output = []
	output_company_names = []

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

		output_company_names.append(job_entry['company'])
		output.append(job_entry_json)

	print(output_company_names)
	return (output_company_names)

	# print(output)
	# return (output)

#GLASSDOOR FEATURE HERE


jobs_wo_ratings = clean_json(resp.json())

# This function cannot work since glassdoor does not allow scripts to webscrape
# def get_company_rating(company_name, city):
# 	# url = 'http://api.glassdoor.com/api/api.htm?v=1&format=json&t.p=118106&t.k=ezeTgVMCN6k&ip=138.51.177.121&useragent=&action=employers&q=' + company_name + '&l=' + city
# 	url = 'http://api.glassdoor.com/api/api.htm?v=1&format=json&t.p=118106&t.k=ezeTgVMCN6k&ip=138.51.177.121&useragent=Mozilla/%2F4.0&action=employers&q=IBM%20Interactive%20Experience&l=toronto'

# 	print(url)
# 	resp = requests.get(url)
	
# 	print(resp)
# 	return (resp.json())
	

# get_company_rating('IBM%20Interactive%20Experience', 'Toronto')

#def add_ratings(jobs_wo_ratings):
	
#	for job in jobs_wo_ratings:
		
#		job['overall_rating'] = #insert the glassdoor rating var	








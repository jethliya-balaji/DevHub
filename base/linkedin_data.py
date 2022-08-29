from linkedin_api import Linkedin
from django.conf import settings

api = Linkedin(settings.LINKEDIN_EMAIL, settings.LINKEDIN_PASSWORD)

def get_required_education_details(full_data):
    all_required_education_data = []
    for i in full_data['education']:
        ed_dic = {}
        try:
            ed_dic.update({'Name of Degree':i['degreeName']})
        except KeyError:
            pass
        try:
            ed_dic.update({'Field of Study':i['fieldOfStudy']})
        except KeyError:
            pass
        try:
            ed_dic.update({'Name of school/university':i['schoolName']})
        except KeyError:
            pass
        try:
            ed_dic.update({'Date': f"{i['timePeriod']['startDate']['year']} - {i['timePeriod']['endDate']['year']}"})
        except KeyError:
            pass
        all_required_education_data.append(ed_dic)
    return all_required_education_data

def get_reqired_experience_details(full_data):
    all_required_experience_data = []
    for i in full_data['experience']:
        exp_dic = {}
        try:
            exp_dic.update({'Name of Company':i['companyName']})
        except KeyError:
            pass
        try:
            exp_dic.update({'Job Description':i['description']})
        except KeyError:
            pass
        try:
            exp_dic.update({'Worked As/Title':i['title']})
        except KeyError:
            pass
        try:
            exp_dic.update({'Date': f"{i['timePeriod']['startDate']['year']} - {i['timePeriod']['endDate']['year']}"})
        except KeyError:
            exp_dic.update({'Date': f"{i['timePeriod']['startDate']['year']} - Current"})
        all_required_experience_data.append(exp_dic)
    return all_required_experience_data

def get_linkedin_data(username:str):
    profile_data = api.get_profile(username)
    required_profile_data_list = {'firstName', 'lastName', 'headline', 'summary', 'industryName', 'geoCountryName', 'education', 'skills', 'experience'}
    required_profile_data = {key : profile_data[key] for key in profile_data.keys() & required_profile_data_list}
    
    try:
        linkedinName = f"{required_profile_data['firstName']} {required_profile_data['lastName']}"
    except Exception:
        linkedinName = ''
    try:
        linkedinHeadline = f"{required_profile_data['headline']}"
    except Exception:
        linkedinHeadline = ''
    try:
        linkedinIndustryName = f"{required_profile_data['industryName']}"
    except Exception:
        linkedinIndustryName = ''
    try:
        linkedinSummary = f"{required_profile_data['summary']}"
    except Exception:
        linkedinSummary = ''
    try:
        linkedinGeoCountryName = f"{required_profile_data['geoCountryName']}"
    except Exception:
        linkedinGeoCountryName = ''
    try:
        linkedinEducation = get_required_education_details(required_profile_data)
    except Exception:
        linkedinEducation = ''
    try:
        linkedinExperience = get_reqired_experience_details(required_profile_data)
    except Exception:
        linkedinExperience = ''


    return linkedinName, linkedinHeadline, linkedinIndustryName, linkedinSummary, linkedinGeoCountryName, linkedinEducation, linkedinExperience

# firstName > lastName > headline > summary > industryName  > geoCountryName
# education > fieldOfStudy > degreeName > schoolName > timePeriod
# skills > name
# experience > companyName > description > title > timePeriod
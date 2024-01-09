import requests

class GetPrograms:
    def get_programs(self):
        URL = "http://data.cityofnewyork.us/resource/uvks-tn5n.json"
        response = requests.get(URL)
        if response.status_code == 200:
            return response.json()  # Parse JSON only if the response is successful
        else:
            print("Failed to fetch data:", response.status_code)
            return []  # Return an empty list if the request fails

    def program_school(self):
        programs_list = []
        programs = self.get_programs()  # Get JSON data
        for program in programs:
            if isinstance(program, dict):  # Check if 'program' is a dictionary
                agency = program.get("agency")
                if agency:
                    programs_list.append(agency)  # Add 'agency' to the list

        return programs_list
      
# programs = GetPrograms().get_programs()
# print(programs)

programs = GetPrograms()
programs_schools = programs.program_school()

for school in set(programs_schools):
    print(school)

# import requests
# import json

# class GetPrograms:

#   def get_programs(self):
#     URL = "http://data.cityofnewyork.us/resource/uvks-tn5n.json"

#     response = requests.get(URL)
#     return response.content
  
#   def program_school(self):
#     # we use the JSON library to parse the API response into nicely formatted JSON
#       programs_list = []
#       programs = json.loads(self.get_programs())
#       for program in programs:
#             programs_list.append(program["agency"])

#       return programs_list

# programs = GetPrograms()
# programs_schools = programs.program_school()

# for school in set(programs_schools):
#     print(school)

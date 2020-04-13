import requests
from prettytable import PrettyTable
#one may have to 'pip install prettytable'

class Bart():
    """ class for bart related objects/functions"""
    def print_etd(self,api,params):
        """Function to return a etd table"""
        try:
            #access api and check for errors
            response = requests.get(api,params)
            if response.status_code != 200:
                return "Couldnt connect-1"

            #process the response data
            l1=[]
            for temp_1 in response.json()['root']['station'][0]['etd']:
                 for temp_2 in temp_1['estimate']:
                     if temp_2['minutes'] == 'Leaving':
                        temp_2['minutes'] = 0
                     l1 += [([int(temp_2['minutes']), [temp_1['destination']]])]

            #create a pretty table for op display
            op_table=PrettyTable([response.json()['root']['station'][0]['name'], response.json()['root']['time']])
            for x in sorted(l1)[:10]:
                op_table.add_row([str(x[0]) + ' min', x[1]])

            return op_table

        except Exception as e:
            return "Error: " + str(e)
            
       

if __name__ == "__main__":
    #fetch or define values
    api = 'http://api.bart.gov/api/etd.aspx'
    params = {'cmd':'etd','orig':'mont','key':'MW9S-E7SL-26DU-VV8V','json':'y'}
    op = Bart().print_etd(api,params)
    print(op)

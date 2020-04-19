#sncf_api_calls/sncf_api.py
#main packages
import pandas as pd
import requests

class sncf_api:
    """
    summary:
        A class of methods that grabs data from the sncf api and returns a clipped version as either a
        dict or a pandas dataframe
        
    Parameters:
        The class can be called with a rail line code or not.
        
    Usage:
        objectclass = sncf(xxxxxx) -- xxxxxx = codeline
        db = objectclass.method() or objectclass.method()

    Methods: [Method name] -- [Returns] -- [Usage]
        test() -- prints all self.veriables -- Check if class had been properly imported
        
        check_site() -- True / False -- Check if API is up
        
        list_construction_site() -- dict -- Lists construction sites for given line
        
        convert_to_pandas_db() -- pandas DataFrame -- Convert dict to pandas DataFrame
        
        list_line_status() -- dict -- Lists all lines by status
        
        list_line_type() -- dict -- Lists all lines by type
    """    
    
    
    def __init__(self, line = ''):
        
        #define veriables used in API call
        self.url_base = 'https://data.sncf.com/' #url base for sncf data
        self.code_line = line #sncf line each have a code, can be used to search through them
        self.db_json = 0
        self.enable = 0 #if set to 0, functions will not run
        if self.code_line == '':
            print('Not adding argument will make methods request whole databasses')
               
    def test(self):
        """
        Summary:
            Method used to check if class has been called and variables are printable. 
            Can be used anytime time print variables.
            
        Usage: 
            objectclass.test()
        Returns: [type] -- [description]
            print(url_base) -- base url used in class
            print(code_line) -- Line code used by class
            print(db_json) -- dict used by methods to pass data
            print(enable) -- bool used to enable methods    
        """        
        try:
            print('Class can run and methode is reachable, printing all variables')
            print(self.url_base)
            print(self.code_line)
            print(self.db_json)
            print(self.enable)
            return True
        except AttributeError:
            return False
    
    def check_site(self):
        """
        Summary:
            Method used to check api status
        Usage:
            objectclass.check_site()
        Returns: [type] -- [description]
            bool -- True / False depending if api is up. Updates self.enable
        """        
        try:
            req = requests.get(self.url_base)

        # On connection error, return False.
        except requests.exceptions.ConnectionError:
            return False
        # Connection was successful, return True on 200 code, else return False.
        else:
            if req.status_code == 200:
                self.enable = 1
                #print(self.enable)
                return True
            return False
  
    def list_construction_site(self):
        """
        Summary:
            Grabs constructions sites for given line. Will return whole database if no line is called.
            
        Usage:
            db = objectclass.list_construction_site()
        
        Returns: [type] -- [description]
            object -- dict of construction site for given line
            
        """        
        self.check_site()
        if self.enable == 1:
            try:
                url_sncf_1 = 'https://data.sncf.com/api/records/1.0/search/?dataset=liste-des-chantiers&rows=0&facet=code_ligne&refine.code_ligne='
                r_base = requests.get(url_sncf_1+str(self.code_line)) #get how many hits
                r_base = r_base.json()
                if r_base['nhits'] == 0:
                    print('No worksites on line')
                    self.db_json = 0
                    return self.db_json
                r_base = r_base['nhits'] #isolate hits for download
                url_sncf_2 = 'https://data.sncf.com/api/records/1.0/search/?dataset=liste-des-chantiers&rows='+str(r_base)+'&facet=code_ligne&refine.code_ligne='+str(self.code_line)
                self.db_json = requests.get(url_sncf_2)
                self.db_json = self.db_json.json()
            
                return self.db_json
            except requests.exceptions.RequestException:
                pass 
            
        print('Api not up or internet down')
        self.db_json = 0
        return False
    
    def convert_to_pandas_db(self):
        """
        Summary:
            Grabs data from prior method and returns a pandas dataframe
            
        Usage:
            Call method that need to be returned as pandas dataframe:
                objectclass.list_construction_site()
            Call method without arguments:
                db_pandas = objectclass.convert_to_pandas_db()
        
        Returns: [type] -- [description]
            object -- pandas dataframe
            
        """
        
        if self.db_json == 0:
            print('Function cant run because db = 0 and convert_to_pandas_db needs a .json object')
            return False

        try:
            self.db_json = self.db_json['records']
            n = 0
            df_sncf = pd.DataFrame.from_dict(self.db_json[0]['fields'])
            for _ in self.db_json:
                try:
                    n = n+1
                    df_sncf = df_sncf.append(self.db_json[n]['fields'],ignore_index=True,sort=False)
                except (IndexError, ValueError):
                    n = n+1
            return df_sncf
        except ValueError:
            print('db_json not in right format')
            return 0
        
    def list_line_status(self):
        """
        Summary:
            Grabs lines by status
        
        Usage:
            db = objectclass.list_line_status()
        
        Returns: [type] -- [description]
            object -- dict of lines by status
        """        
        self.check_site()
        if self.enable == 1:
            try:
                url_sncf_1 = 'https://data.sncf.com/api/records/1.0/search/?dataset=lignes-par-statut&rows=0&facet=statut'
                r_base = requests.get(url_sncf_1) #get how many hits
                r_base = r_base.json()
                if r_base['nhits'] == 0:
                    print('Error with API')
                    self.db_json = 0
                    return self.db_json
                r_base = r_base['nhits'] #isolate hits for download
                url_sncf_2 = 'https://data.sncf.com/api/records/1.0/search/?dataset=lignes-par-statut&rows='+str(r_base)
                self.db_json = requests.get(url_sncf_2)
                self.db_json = self.db_json.json()
            
                return self.db_json
            except requests.exceptions.RequestException:
                pass
        
        print('Api not up or internet down')
        self.db_json = 0
        return self.db_json
        
    def list_line_type(self):
        """
        Summary:
            Grabs lines by type. Can max out the api calls, data can be clipped
        
        Usage:
            db = objectclass.list_line_type()
        
        Returns: [type] -- [description]
            object -- dict of lines by type
        """
        print('This function maxes out the API, so not all hits can be called')
        self.check_site()
        if self.enable == 1:
            try:
                url_sncf_1 = 'https://data.sncf.com/api/records/1.0/search/?dataset=lignes-par-type&rows=0&facet=type_ligne'
                r_base = requests.get(url_sncf_1) #get how many hits
                r_base = r_base.json()
                if r_base['nhits'] == 0:
                    print('Error with API')
                    self.db_json = 0
                    return self.db_json
                r_base = r_base['nhits'] #isolate hits for download
                url_sncf_2 = 'https://data.sncf.com/api/records/1.0/search/?dataset=lignes-par-type&rows='+str(r_base)
                self.db_json = requests.get(url_sncf_2)
                self.db_json = self.db_json.json()
            
                return self.db_json
            except requests.exceptions.RequestException:
                pass
        
        print('Api not up or internet down')
        self.db_json = 0
        return self.db_json
          
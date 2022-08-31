import pandas as pd
import numpy as np
import requests


class ViV():
    def __init__(self,name,bio,age,status,pref_start,pref_end,pref_sex,pref_stat) -> None:
        self.name = name
        self.age = age
        self.bio = bio
        self.status = status
        self.pref_start = pref_start
        self.pref_end = pref_end
        self.pref_sex = pref_sex
        self.pref_stat = pref_stat

    def predict_model(self,disp_all = False):

        url = 'https://viv7-wi4xtxynwq-de.a.run.app/new user bio'

        params = {'name':self.name,
                  'bio':self.bio,
                  'age':self.age,
                  'status':self.status,
                  'pref_age_start':self.pref_start,
                  'pref_age_end':self.pref_end,
                  'pref_sex':self.pref_sex,
                  'pref_status':self.pref_stat,
                  'format':'json'}

        response = requests.get(url, params=params).json()
        self.data = pd.DataFrame(response).set_axis(['Dominant_Topics',
                                                    'Topic_Percentage',
                                                    'Keywords',
                                                    'Profile',
                                                    'Age',
                                                    'Status',
                                                    'Sex',
                                                    'Location'
                                                    ], axis ='columns')
        self.data['Sex'] = self.data['Sex'].map({1:'Male',2:'Female'})
        self.data['Status'] = self.data['Status'].apply(lambda x: x.capitalize())
        if disp_all:
            return self.data
        return self.data[['Profile', 'Age', 'Location', 'Sex', 'Dominant_Topics']]


if __name__ == '__main__':
    viv1 = ViV('apple',"hi mizuki i like to workout and dance like a cowboy grinding at the club. i want some baddie girls", 20, 'single', 18, 30, 'female', 'single')
    results = viv1.predict_model()
    print(results)

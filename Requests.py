# <copyright company="Bicedeep, Inc.">
# Copyright (c) 2016-2018 All Rights Reserved
# </copyright>

import requests

headers = {
        "Authorization" : "Bearer 4j4PzSsSHz4KRJdjDJRt7SpL-Rj-E5tKhiLYmHnvBOW0RO8bshfjpTyt7Yz6urQ_EVp01hiA1mGUbYkzLDmRev2dKo6ud17NCWh8y7K2739V_VN3gxiqhkbLIusBTSNLDmQXza2xWHxvH-y1mfLxqQyl3EsNtY84qdIl5iT1M7IogwenWr3JHr1662gq-fUAu2sGrMUyui477lTS8SLzj-RYbYuGDLomrYVS3nivPvsmClBA7HQ90rb4TO7xeymkzdNZ5r0ZETu4P18dEKL3aiyhTmgNcMFbWpME7BJi3oo"
    }

baseUrl = "http://localhost:4509"

def getAuthToken():
    tokenHeaders = {
        "Content-Type": "application/x-www-form-urlencoded",
        "Accept": "application/json"
    }
    url = baseUrl + '/api/tokenapi/Token'
    body = {
        "grant_type" : "password",
        "username" : "",
        "password" : ""
    }
    resp = requests.get(url, data=body, headers=tokenHeaders)
    print(resp.content)

def getFileList():
    url = baseUrl + '/api/fileapi/GetFileList'
    resp = requests.get(url, headers=headers)
    print(resp.content)

def uploadAFile(filepath):
    url = baseUrl + '/api/fileapi/UploadAFile'
    files = {'upload_file': open(filepath, 'rb')}
    r = requests.post(url, files=files, headers=headers)
    print(r.content)

def deleteAFile():
    url = baseUrl + '/api/fileapi/DeleteAFile?filename=Adult_Tobacco_Consumption_In_The_U.S.__2000-Present_11.csv'
    r = requests.get(url, headers=headers)
    print(r.content)

def requestReport():
    url = baseUrl + '/api/reportapi/RequestReport'
    body = {
        "fileName" : "Adult_Tobacco_Consumption_In_The_U.S.__2000-Present_11.csv",
        "selectedHeaders" : [ "Data Value Unit", "Total", "Domestic Per Capita" ]
    }
    r = requests.post(url, json=body, headers=headers)
    print(r.content)

#report values are empty if the report is not completed.
def getReport():
    url = baseUrl + '/api/reportapi/GetReport?filename=Adult_Tobacco_Consumption_In_The_U.S.__2000-Present_11.csv'
    r = requests.get(url, headers=headers)
    print(r.content)

def createModel():
    url = baseUrl + '/api/modelapi/CreateModel?modelid=Adult_Tobacco_Consumption_In_The_U.S.__2000-Present_11.csv.00001'
    r = requests.get(url, headers=headers)
    print(r.content)

def createQuery():
    url = baseUrl + '/api/queryapi/CreateQuery?modelid=HR_comma_sep-11.csv.00001'
    body = {"queried_part": "left",
            "result_type": "number",
            "query_using": [{"part": "satisfaction_level", "value": "0.25"},
                            {"part": "number_project", "value": "6"},
                            {"part": "time_spend_company", "value": "2"}]}
    r = requests.post(url, json=body, headers=headers)
    print(r.content)

def getQueryResult():
    url = baseUrl + '/api/queryapi/GetQueryResult?queryId=HR_comma_sep-11.csv.00001.000003'
    r = requests.get(url, headers=headers)
    print(r.content)

def main():
    #getAuthToken()
    #getFileList()
    #deleteAFile()
    #requestReport()
    #getReport()
    #createModel()
    #createQuery()
    getQueryResult()
    #uploadAFile('E:\Data\Adult_Tobacco_Consumption_In_The_U.S.__2000-Present_11.csv')


if  __name__ =='__main__':main()
# <copyright company="Bicedeep, Inc.">
# Copyright (c) 2016-2018 All Rights Reserved
# </copyright>

import requests

# Authorization headers are valid for 24 hours.
headers = {
        "Authorization" : "Bearer EiBjuyO-JPGLw_ZrKsZqhBSKRScOY00hN6hv14IY-0C9QeGWbAZkFTwgTuCBu0cPLWs_up4tkvJrEBFsIeYv7IUVjGM7g_23ZK_ql3YE7rOseSDqO8LCFCzslxzipzL1mHkZKIGEqJ6q6A1GkOcvwBxan_YsLAZWzg9vR6YhS3QjvQ0UrAR5LS2jLR1S85ceDv7sIcFOzFQIftsO35gvp3NUHrHF9g-FziyazRgblYTEgfyS4cUjwSpO49cpZJ-4jf0_tUcO4-4_b6RybRzJ8P8z_-Rs5tVrlbl7KysDaLQ"
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

#report values are empty if the report is not completed. You will get an email when the report is ready
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

# You will get an email when the query file is filled
def submitAQueryFile(filepath):
    url = baseUrl + '/api/queryapi/SubmitAQueryFile?modelid=HR_comma_sep-11.csv.00001'
    files = {'upload_file': open(filepath, 'rb')}
    r = requests.post(url, files=files, headers=headers)
    print(r.status_code)
    print(r.content)

# it gets the unchanged query file before the completion email,
def downloadAQueryFile(filename):
    url = baseUrl + '/api/queryapi/DownloadAQueryFile?filename=' + filename
    r = requests.get(url, headers=headers)
    f = open(filename, 'w')
    f.write(r.text)
    f.close()

def main():
    #getAuthToken()
    #getFileList()
    #uploadAFile('E:\Data\Adult_Tobacco_Consumption_In_The_U.S.__2000-Present_11.csv')
    #deleteAFile()
    #requestReport()
    #getReport()
    #createModel()
    #createQuery()
    #getQueryResult()
    #submitAQueryFile('E:\Data\human-resources-analytics\HR_comma_sep-11-queries1.csv')
    #downloadAQueryFile('HR_comma_sep-11-queries1.csv')

if  __name__ =='__main__':main()
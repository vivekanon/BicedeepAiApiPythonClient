# <copyright company="Bicedeep, Inc.">
# Copyright (c) 2016-2018 All Rights Reserved
# </copyright>

import requests

# Authorization headers are valid for 24 hours.
headers = {
        "Authorization" : "Bearer AQYRLLAXlz7hTtlu-RR4yXe75pslyb0zVwPVJNh4w7ToyZht8cLm1FRvok7SKXyAQJ3o_YBZ35X8t9ybg0lczvhQjOKQG1Lu6-j7f-Vjn7RZak4-hV_x9nyGHDJeG-wgDzl5Xyxqtb9QzDotMiJBeeaIhPNA9QCMeleRX_QXhwpwHm9hZFFi54nRTasj1RkOIG909nuRyBjg7yA3ksSb2PdPImMWkPOkwt_JSBtiP_0y6XbUIv9Tw9LM7Zh0dUj52VRl6K4KUOF5LpyXy0IUSv9jlAz0VHr8OaOYo-pgXMykz1YCH6dRlIJm2hwXS2MT"
    }

baseUrl = "https://bicedeepai.com"

def getAuthToken(username, password):
    tokenHeaders = {
        "Content-Type": "application/x-www-form-urlencoded",
        "Accept": "application/json"
    }
    url = baseUrl + '/api/tokenapi/Token'
    body = {
        "grant_type" : "password",
        "username" : username,
        "password" : password
    }
    resp = requests.get(url, data=body, headers=tokenHeaders)
    print(resp.content)

def getFileList(nextpagetoken, prefix):
    url = baseUrl + '/api/fileapi/GetFileList?nextpagetoken=' + nextpagetoken +'&prefix=' + prefix
    resp = requests.get(url, headers=headers)
    print(resp.content)

def uploadAFile(filepath):
    url = baseUrl + '/api/fileapi/UploadAFile'
    files = {'upload_file': open(filepath, 'rb')}
    r = requests.post(url, files=files, headers=headers)
    print(r.content)

def deleteAFile(filename):
    url = baseUrl + '/api/fileapi/DeleteAFile?filename=' + filename
    r = requests.get(url, headers=headers)
    print(r.content)

def requestReport(requestBody):
    url = baseUrl + '/api/reportapi/RequestReport'
    r = requests.post(url, json=requestBody, headers=headers)
    print(r.content)

#report values are empty if the report is not completed. You will get an email when the report is ready
def getReport(filename):
    url = baseUrl + '/api/reportapi/GetReport?filename=' + filename
    r = requests.get(url, headers=headers)
    print(r.content)

def createModel(modelId):
    url = baseUrl + '/api/modelapi/CreateModel?modelid=' + modelId
    r = requests.get(url, headers=headers)
    print(r.content)

def createQuery(modelid, requestBody):
    url = baseUrl + '/api/queryapi/CreateQuery?modelid=' + modelid
    r = requests.post(url, json=requestBody, headers=headers)
    print(r.content)

def getQueryResult(queryId):
    url = baseUrl + '/api/queryapi/GetQueryResult?queryId=' + queryId
    r = requests.get(url, headers=headers)
    print(r.content)

# You will get an email when the query file is filled
def submitAQueryFile(filepath, modelId):
    url = baseUrl + '/api/queryapi/SubmitAQueryFile?modelid=' + modelId
    files = {'upload_file': open(filepath, 'rb')}
    r = requests.post(url, files=files, headers=headers)
    print(r.status_code)
    print(r.content)

# it gets the unchanged query file before the completion email,
def downloadAQueryFile(filename):
    url = baseUrl + '/api/queryapi/DownloadAQueryFile?filename=' + filename
    r = requests.get(url, headers=headers)
    if r.status_code == 200:
        f = open(filename, 'w')
        f.write(r.text)
        f.close()

def main():

    #getAuthToken('', '')
    #getFileList('', '')
    #uploadAFile('E:\Data\human-resources-analytics\HR_comma_sep-20.csv')
    #deleteAFile('HR_comma_sep-20.csv')

    requestReportBody = {
        "fileName": "HR_comma_sep-20.csv",
        "selectedHeaders": ["last_evaluation", "sales", "left"]
    }

    #requestReport(requestReportBody)
    #getReport("HR_comma_sep-20.csv")
    #createModel("HR_comma_sep-20.csv.00003")


    createQueryBody = {"queried_part": "left",
                       "result_type": "number",
                       "query_using": [{"part": "satisfaction_level", "value": "0.4"},
                                       {"part": "last_evaluation", "value": "6"},
                                       {"part": "number_project", "value": "3"},
                                       {"part": "time_spend_company", "value": "2"},
                                       {"part": "promotion_last_5years", "value": "0"},
                                       {"part": "sales", "value": "sales"}]}

    #createQuery("HR_comma_sep-20.csv.00003", createQueryBody)
    #getQueryResult("HR_comma_sep-20.csv.00003.000001")
    #submitAQueryFile('E:\Data\human-resources-analytics\HR_comma_sep-20-queries4.csv', "HR_comma_sep-20.csv.00003")
    #downloadAQueryFile('HR_comma_sep-20-queries2.csv')

if  __name__ =='__main__':main()
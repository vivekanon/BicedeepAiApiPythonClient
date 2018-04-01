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
    resp = requests.post(url, data=body, headers=tokenHeaders)
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

#docker only method, not available on live API
def downloadAFile(filename):
    url = baseUrl + '/api/fileapi/DownloadAFile?filename=' + filename
    r = requests.get(url, headers=headers)
    if r.status_code == 200:
        f = open(filename, 'w')
        f.write(r.text)
        f.close()

#docker only method, not available on live API
def downloadModelFile(modelFileName):
    url = baseUrl + '/api/fileapi/DownloadModelFile?modelFileName=' + modelFileName
    r = requests.get(url, headers=headers)
    if r.status_code == 200:
        f = open(modelFileName, 'wb')
        f.write(r.content)
        f.close()

def transferDataFile(sourceFilePath):
    url = baseUrl + '/api/fileapi/TransferDataFile?sourceFilePath=' + sourceFilePath
    r = requests.get(url, headers=headers)
    print(r.content)

def renameFile(oldName, newName):
    url = baseUrl + '/api/fileapi/RenameFile?oldFileName=' + oldName + '&newFileName=' + newName
    r = requests.get(url, headers=headers)
    print(r.content)

def deleteAFile(filename):
    url = baseUrl + '/api/fileapi/DeleteAFile?filename=' + filename
    r = requests.get(url, headers=headers)
    print(r.content)

def requestReport(requestBody):
    url = baseUrl + '/api/reportapi/RequestReport'
    r = requests.post(url, json=requestBody, headers=headers)
    print(r.content)

def getStatus(filename):
    url = baseUrl + '/api/reportapi/GetStatus?filename=' + filename
    r = requests.get(url, headers=headers)
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
    # only at live api not docker
    #getAuthToken('', '')

    #getFileList('', '')
    #uploadAFile('C:/Users/Downloads/Iris-try1.csv')

    # only at docker not live api
    #downloadAFile('Iris-try1.csv')

    # only at docker not live api
    #downloadModelFile('Iris-try1.csv.00001.h5')

    # only at docker not live api
    #downloadModelFile('Iris-try1.csv.00001.h5.json')

    # only at live api not docker
    #transferDataFile('datafiles/Adult_Tobacco_Consumption_In_The_U.S.__2000-Present_copied.csv')

    #renameFile('Iris-try1.csv', 'Iris-try2.csv')
    #deleteAFile('Iris-try2.csv')

    requestReportBody = {
        "fileName": "Iris-try1.csv",
        "selectedHeaders": ["Species"]
    }

    #requestReport(requestReportBody)
    #getStatus('Iris-try1(1).csv')
    #getReport('Iris-try1.csv')

    #only at live api not docker
    #createModel("HR_comma_sep-20.csv.00003")


    createQueryBody = {"queried_part": "Species",
                       "result_type": "string",
                       "query_using": [{"part": "SepalLengthCm", "value": "5.4"},
                                       {"part": "PetalLengthCm", "value": "0.6"},
                                       {"part": "PetalWidthCm", "value": "0.2"}]}

    #createQuery("Iris-try1.csv.00001", createQueryBody)
    #getQueryResult("Iris-try1.csv.00001.000002")
    #submitAQueryFile('C:/Users/Downloads/Iris-try1-q2.csv', "Iris-try1.csv.00001")
    #downloadAQueryFile('Iris-try1-q2.csv')

if  __name__ =='__main__':main()
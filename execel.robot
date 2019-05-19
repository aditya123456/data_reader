*** Settings ***
Library    ../../libs/apis/CSVLibrary.py
Library    ../../libs/apis/EXCELLibray.py
Library    RequestsLibrary

*** Test Cases ***
API Demo Post Request
   ${all_values}=  datareader   sample.xlsx   Y
   log  ${all_values}
   ${json_request}=  put values in json  ${all_values}[0][email1]
   log  ${json_request}
   :FOR   ${INDEX}  IN   @{all_values}
   \  LOG  ${INDEX}
   \  ${json_request}=  put values in json  ${INDEX}[email1]
   \  log  ${json_request}
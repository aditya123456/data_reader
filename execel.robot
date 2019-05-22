*** Settings ***
Library    EXCELLibray.py
Library    RequestsLibrary

*** Test Cases ***
API Demo Post Request
   ${all_values}=  datareader   sample.xlsx   Y
   log  ${all_values}
   :FOR   ${INDEX}  IN   @{all_values}
   \  LOG  ${INDEX}
   \  ${json_request}=  put values in json with json file  sample.json  ${INDEX}
   \  log  ${json_request}
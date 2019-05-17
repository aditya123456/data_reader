*** Settings ***
Library    ../../libs/apis/CSVLibrary.py
Library    ../../libs/apis/EXCELLibray.py
Library    RequestsLibrary

*** Test Cases ***
API Demo Post Request
   ${all_values}=  READ EXCEL USING XLRD   sample.xlsx  Y
   log  ${all_values}
   :FOR   ${INDEX}  IN   @{all_values}
   \  LOG  ${INDEX}
   \  ${json_request}=  put values in json  ${INDEX}[firstName]  ${INDEX}[lastName]  ${INDEX}[Value1]  ${INDEX}[Value2]
   \  log  ${json_request}
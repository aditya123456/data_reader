from xlrd import open_workbook
import json

class EXCELLibray(object):

    def Datareader(self, file_name,  FLAG):
        filter_list =[]
        book = open_workbook(file_name)
        sheet = book.sheet_by_index(0)

        # read header values into the list
        keys = [sheet.cell(0, col_index).value for col_index in range(sheet.ncols)]
        print (keys)

        dict_list = []
        for row_index in range(1, sheet.nrows):
            d = {keys[col_index]: sheet.cell(row_index, col_index).value for col_index in range(sheet.ncols)}
            dict_list.append(d)
        print ("before flag")
        print (dict_list)
        for i in dict_list:
            if i['executionFlag'] == FLAG:
                filter_list.append(i)
        print ("after flag")
        # print (filter_list)
        header_dict = {}
        for i in filter_list:
            for key, value in i.items():
                if key.startswith('Header_'):
                    if type(value) is float:
                        header_dict.update({key.split('_')[1]: int(value)})
                    else:
                        header_dict.update({key.split('_')[1]: str(value)})
                    i['Header'] = header_dict
        print (filter_list)
        return filter_list

    def generate_header(self, header):
        print (json.dumps(header))
        return json.dumps(header)

    def put_values_in_json_without_data_json_file(self, file_name, index):
        json_res=''
        try:
            json_res = json.loads(open(file_name).read())
        except:
            print ("file does not exist")

        def json_recursive_update(json_res):
            json_res = json_res
            if type(json_res) is dict:
                for json_key ,json_value in json_res.items():
                    if type(json_value) is dict:
                        json_recursive_update(json_value)
                    elif type(json_value) is list:
                        for i in json_value:
                            json_recursive_update(i)
                    else:
                        for excel_key,excel_value in index.items():
                            if excel_key == json_value:
                                if type(excel_value) is float:
                                    json_res[json_key] = int(excel_value)
                                elif(excel_value in ['True', 'False', 'TRUE', 'FALSE']):
                                    json_res[json_key] = bool(excel_value)
                                else:
                                    json_res[json_key] = str(excel_value)
            elif(type(json_res) is list):
                 for i in json_res:
                     json_recursive_update(i)
        json_recursive_update(json_res)
        print (json.dumps(json_res))
        return json.dumps(json_res)



if __name__ == '__main__':
    x = EXCELLibray()
    x.Datareader('sample.xlsx', 'Y')
    x.put_values_in_json_without_data_json_file('sample_json_with_multiple_node.json', {"firstName":"aditya", "city":"Pune","intvalue1":3})

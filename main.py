from json import loads, dumps
import logging

logging.basicConfig(filename='./app.log', filemode='w',level=logging.DEBUG, format='%(asctime)s | %(name)s | %(levelname)s | %(message)s')
logger = logging.getLogger()

def recursion_fun(data):
    try:
        # replace string function
        def replace_fun(name):
            s1 = name.replace("+type","+size@5+type")
            return s1

        # object type is dict
        if isinstance(data, dict):
            # empty outpput dict
            output_data = {}
            for key,value in data.items():
                # call replace function
                new_key = replace_fun(key)
                # check value type is string or dict
                # if dict then call recursion function
                # else call replace string function
                if type(value) == str and "+type" in value:
                    new_value = replace_fun(value)
                    output_data[new_key] = new_value
                else:
                    value = recursion_fun(value)
                    output_data[new_key] = value
            return output_data

        # object type is list
        if isinstance(data, list):
            new_list = []
            for value in data:
                new_list.append(replace_fun(value))
            return new_list

        return data

    except KeyError as key_error:
        logger.error({"Error":"The following key is not found {}".format(str(key_error))})
    except ValueError as value_error:
        logger.error({"Error":"Value Error {}".format(str(value_error))})
    except Exception as e:
        logger.error({"Error":"Exception {}".format(str(e))})


# open input file
with open("./test.json") as json_file:
    input_data = loads(json_file.read())
    logger.info("Open test.json file.")

# create output file
with open("./output.json","w") as file:
    file.write(dumps(recursion_fun(input_data), indent=4))
    logger.info("data updated in output.json file")
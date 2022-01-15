from json import loads, dumps
import logging

logging.basicConfig(filename='./app.log', filemode='w',level=logging.DEBUG, format='%(asctime)s | %(name)s | %(levelname)s | %(message)s')
logger = logging.getLogger()

try:
    # open input file
    with open("./test.json") as json_file:
        data = loads(json_file.read())
        logger.info("Open test.json file.")

    # empty outpput dict
    output_data = {}
    for key,values in data.items():
        # replace +type work from key
        new_key = key.replace("+type","+size@5+type")
        logger.debug("old key: {} and new_key : {}".format(key, new_key))
        # new_key update on output_data
        output_data[new_key] = {}
        for val in values:
            item = data[key][val]
            # check type of item
            if type(item) == str:
                new_value = item.replace("+type","+size@5+type")
                output_data[new_key][val] = new_value
                logger.debug("old value: {} and new_value : {}".format(val, new_value))
            else:
                new_value_list = []
                for x in item:
                    new_value = x.replace("+type","+size@5+type")
                    new_value_list.append(new_value)
                    logger.debug("old value: {} and new_value : {}".format(val, new_value))
                output_data[new_key][val] = new_value_list

    logger.debug("Result : {}".format(output_data))
    # create output json file and write
    with open("./output.json","w") as file:
        file.write(dumps(output_data, indent=4))
        logger.info("data updated in output.json file")

except KeyError as key_error:
    logger.error({"Error":"The following key is not found {}".format(str(key_error))})
except ValueError as value_error:
    logger.error({"Error":"Value Error {}".format(str(value_error))})
except Exception as e:
    logger.error({"Error":"Exception {}".format(str(e))})

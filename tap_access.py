import matplotlib.pyplot as plt
import pandas as pd
import requests
import json
import io

def _get_request(query: str, format: str = "json") -> list:
    """
    Handles all requests to the TAP database.

    :param query: String query in SQL-type.
    :param format: Not implemented. Do not use.
    :return: Returned data from TAP database as list.
    """
    http_query = "https://exoplanetarchive.ipac.caltech.edu/TAP/sync?query=" + query.replace(" ", "%20").replace("+", "%20") + "&format=" + format
    data = requests.get(http_query)
    if data.ok:
        return json.loads(data.text)
    else:
        print(data.reason)
        return []
        

def get_available_tables() -> list:
    # get all available tables that can be queried
    #return _get_request("https://exoplanetarchive.ipac.caltech.edu/TAP/sync?query=select+*+from+TAP_SCHEMA.tables")
    return _get_request("select schema_name,table_name,description from TAP_SCHEMA.tables")

def get_table_information(table_name: str) -> list:
    return _get_request("select * from TAP_SCHEMA.columns where table_name like %27" + table_name +"%27")
    

def get_planetary_data(query: str):
    data = _get_request(query)

    return pd.DataFrame.from_dict(data) if data else []
    
    # code from here is never run
    # plt.xlabel("dec")
    # plt.ylabel("ra")
    # plt.plot(df["dec"], df["ra"], ".")
    # plt.plot(x_points, y_points)
    # plt.show()

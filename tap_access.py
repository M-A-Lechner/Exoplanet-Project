import matplotlib.pyplot as plt
import pandas as pd
import requests
import json
import io

def get_available_tables():
    # get all available tables that can be queried
    tables_res = requests.get("https://exoplanetarchive.ipac.caltech.edu/TAP/sync?query=select+schema_name,table_name+from+TAP_SCHEMA.tables&format=json")
    if tables_res.ok:
        poss_tables = json.loads(tables_res.text)
        return poss_tables
    else:
        print(tables_res.reason)
        return []

def get_planetary_data(query: str, format: str = "json"):
    http_query = query.replace(" ", "+")
    #req = requests.get("https://exoplanetarchive.ipac.caltech.edu/TAP/sync?query=select+top+1000+ra,dec+from+ps&format=json")
    req = requests.get("https://exoplanetarchive.ipac.caltech.edu/TAP/sync?query=" + http_query + "&format=" + format)

    if req.ok:
        df = pd.read_json(io.StringIO(req.text))
        #print(df)
        return df

        plt.xlabel("dec")
        plt.ylabel("ra")
        plt.plot(df["dec"], df["ra"], ".")
        #plt.plot(x_points, y_points)
        plt.show()
    else:
        print(req.reason)
        return None
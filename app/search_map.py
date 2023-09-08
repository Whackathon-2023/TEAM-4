import os
import openai
import json

openai.api_type = "azure"
openai.api_base = "https://whackazureopenai4.openai.azure.com/"
openai.api_version = "2023-07-01-preview"
openai.api_key = "f06743f3d6024b488a38022f476ea726"

ship_data = {"ports": [
        {
            "Country": "Jordan",
            "Function": "Unknown",
            "LOCODE": "JO AQJ",
            "Name": "Al Aqabah",
            "NameWoDiac": "Al Aqabah",
            "Status": "AI",
            "lat": 29.516667,
            "long": 35.0,
            "outflows": 6340518,
            "Vessels Visited": []
        },
        {
            "Country": "Indonesia",
            "Function": "Unknown",
            "LOCODE": "ID BXT",
            "Name": "Bontang Lng Terminal",
            "NameWoDiac": "Bontang Lng Terminal",
            "Status": "AI",
            "lat": 0.1,
            "long": 117.483333,
            "outflows": 6783296,
            "Vessels Visited": []
        },
        {
            "Country": "Russia",
            "Function": "Unknown",
            "LOCODE": "RU NVS",
            "Name": "Novorossiysk",
            "NameWoDiac": "Novorossiysk",
            "Status": "AI",
            "lat": 44.716667,
            "long": 37.783333,
            "outflows": 7891578,
            "Vessels Visited": [
                "ISLAND EXPRESS",
                "TAHO AFRICA",
                "MITERA"
            ]
        },
        {
            "Country": "United States",
            "Function": "Unknown",
            "LOCODE": "US PWM",
            "Name": "Portland",
            "NameWoDiac": "Portland",
            "Status": "AI",
            "lat": 43.666667,
            "long": -70.25,
            "outflows": 7353495,
            "Vessels Visited": [
                "ISLAND EXPRESS",
                "APL MEXICO CITY",
                "TAHO AFRICA",
                "MITERA"
            ]
        },
        {
            "Country": "Bahrain",
            "Function": "Unknown",
            "LOCODE": "BH SIT",
            "Name": "Sitrah",
            "NameWoDiac": "Sitrah",
            "Status": "AI",
            "lat": 26.166667,
            "long": 50.666667,
            "outflows": 1436192,
            "Vessels Visited": []
        },
        {
            "Country": "Qatar",
            "Function": "1----6--",
            "LOCODE": "QAMES",
            "Name": "Mesaieed",
            "NameWoDiac": "Mesaieed",
            "Status": "RQ",
            "lat": 25.633333333333333,
            "long": 51.916666666666664,
            "outflows": 87230.0,
            "Vessels Visited": [
                "COSCO GENOA",
                "MSC LIDIA",
                "APL MEXICO CITY",
                "HMPNGS GILBERT TOROPO"
            ]
        },
        {
            "Country": "Saudi Arabia",
            "Function": "Unknown",
            "LOCODE": "Unknown",
            "Name": "Al Jubail",
            "NameWoDiac": "Al Jubail",
            "Status": "AI",
            "lat": 27.933333,
            "long": 35.25,
            "outflows": 400071,
            "Vessels Visited": [
                "YU PENG"
            ]
        },
        {
            "Country": "United States",
            "Function": "Unknown",
            "LOCODE": "Unknown",
            "Name": "Donaldsonville",
            "NameWoDiac": "Donaldsonville",
            "Status": "AI",
            "lat": 40.533333,
            "long": -74.25,
            "outflows": 789083,
            "Vessels Visited": [
                "COSCO GENOA",
                "MSC LIDIA"
            ]
        },
        {
            "Country": "Trinidad and Tobago",
            "Function": "Unknown",
            "LOCODE": "Unknown",
            "Name": "Port Lisas",
            "NameWoDiac": "Port Lisas",
            "Status": "AI",
            "lat": 10.2,
            "long": -61.7,
            "outflows": 1262443,
            "Vessels Visited": [
                "YU PENG",
                "APL MEXICO CITY"
            ]
        },
        {
            "Country": "Saudi Arabia",
            "Function": "Unknown",
            "LOCODE": "Unknown",
            "Name": "Ras Al Khair",
            "NameWoDiac": "Ras Al Khair",
            "Status": "AI",
            "lat": 27.933333,
            "long": 35.25,
            "outflows": 7409830,
            "Vessels Visited": [
                "YU PENG",
                "PALAWAN",
                "CAPE PILLAR",
                "HMPNGS GILBERT TOROPO"
            ]
        },
        {
            "Country": "Malaysia",
            "Function": "Unknown",
            "LOCODE": "Unknown",
            "Name": "Sipitang",
            "NameWoDiac": "Sipitang",
            "Status": "AI",
            "lat": 4.566667,
            "long": 103.466667,
            "outflows": 3928316,
            "Vessels Visited": [
                "PALAWAN",
                "CAPE PILLAR",
                "HMPNGS GILBERT TOROPO"
            ]
        }
    ]
}

example =  { "ports": [{
        "Country": "",
        "Function": "",
        "LOCODE": "",
        "Name": "",
        "NameWoDiac": "",
        "Status": "",
        "lat": 0,
        "long": 0,
        "outflows": 0
    }
]}

def query_map_ai(query):
    response = openai.ChatCompletion.create(
    engine="team4",
    messages = [{"role":"system","content":"You are an AI that returns ports that fit certain criteria, you can ONLY return valid JSON with values enclosed in double quotes in this format: " + str(example)}, {"role": "user", "content": query + ", answer this question using the following vessel JSON: " + str(ship_data)}],
    temperature=0.7,
    max_tokens=1500,
    top_p=0.95,
    frequency_penalty=0,
    presence_penalty=0,
    stop=None)


    out = response['choices'][0]['message']['content'].replace('\'', '\"')
    print(out)
    return json.loads(out)
import os
import openai

openai.api_type = "azure"
openai.api_base = "https://whackazureopenai4.openai.azure.com/"
openai.api_version = "2023-07-01-preview"
openai.api_key = "f06743f3d6024b488a38022f476ea726"

ship_data = {
    "vessels": [
        {
            "Vessel Name": "COSCO GENOA",
            "Ports Visited": [
                {
                    "Port Name": "Mesaieed",
                    "Product Type": "Urea",
                    "Quantity": 4500,
                    "FOB Price per Unit in AUD": 300
                },
                {
                    "Port Name": "Donaldsonville",
                    "Product Type": "UAN",
                    "Quantity": 3200,
                    "FOB Price per Unit in AUD": 350
                },
                {
                    "Port Name": "Aqaba",
                    "Product Type": "MOP",
                    "Quantity": 2800,
                    "FOB Price per Unit in AUD": 280
                }
            ]
        },
        {
            "Vessel Name": "YU PENG",
            "Ports Visited": [
                {
                    "Port Name": "Al Jubail",
                    "Product Type": "Urea",
                    "Quantity": 4700,
                    "FOB Price per Unit in AUD": 300
                },
                {
                    "Port Name": "Port Lisas",
                    "Product Type": "UAN",
                    "Quantity": 3500,
                    "FOB Price per Unit in AUD": 350
                },
                {
                    "Port Name": "Ras Al Khair",
                    "Product Type": "MAP",
                    "Quantity": 3100,
                    "FOB Price per Unit in AUD": 280
                }
            ]
        },
        {
            "Vessel Name": "ISLAND EXPRESS",
            "Ports Visited": [
                {
                    "Port Name": "Bontang",
                    "Product Type": "Urea",
                    "Quantity": 4900,
                    "FOB Price per Unit in AUD": 300
                },
                {
                    "Port Name": "Novorossiysk",
                    "Product Type": "UAN",
                    "Quantity": 3400,
                    "FOB Price per Unit in AUD": 350
                },
                {
                    "Port Name": "Portland",
                    "Product Type": "MOP",
                    "Quantity": 2900,
                    "FOB Price per Unit in AUD": 280
                }
            ]
        },
        {
            "Vessel Name": "PALAWAN",
            "Ports Visited": [
                {
                    "Port Name": "Sitra",
                    "Product Type": "Urea",
                    "Quantity": 4600,
                    "FOB Price per Unit in AUD": 300
                },
                {
                    "Port Name": "Sipitang",
                    "Product Type": "UAN",
                    "Quantity": 3300,
                    "FOB Price per Unit in AUD": 350
                },
                {
                    "Port Name": "Ras Al Khair",
                    "Product Type": "MAP",
                    "Quantity": 2900,
                    "FOB Price per Unit in AUD": 280
                }
            ]
        },
        {
            "Vessel Name": "CAPE PILLAR",
            "Ports Visited": [
                {
                    "Port Name": "Sipitang",
                    "Product Type": "Urea",
                    "Quantity": 4800,
                    "FOB Price per Unit in AUD": 300
                },
                {
                    "Port Name": "Aqaba",
                    "Product Type": "UAN",
                    "Quantity": 3200,
                    "FOB Price per Unit in AUD": 350
                },
                {
                    "Port Name": "Ras Al Khair",
                    "Product Type": "MAP",
                    "Quantity": 2700,
                    "FOB Price per Unit in AUD": 280
                }
            ]
        },
        {
            "Vessel Name": "MSC LIDIA",
            "Ports Visited": [
                {
                    "Port Name": "Mesaieed",
                    "Product Type": "Urea",
                    "Quantity": 4700,
                    "FOB Price per Unit in AUD": 300
                },
                {
                    "Port Name": "Donaldsonville",
                    "Product Type": "UAN",
                    "Quantity": 3400,
                    "FOB Price per Unit in AUD": 350
                },
                {
                    "Port Name": "Aqaba",
                    "Product Type": "MOP",
                    "Quantity": 2800,
                    "FOB Price per Unit in AUD": 280
                }
            ]
        },
        {
            "Vessel Name": "APL MEXICO CITY",
            "Ports Visited": [
                {
                    "Port Name": "Mesaieed",
                    "Product Type": "Urea",
                    "Quantity": 4600,
                    "FOB Price per Unit in AUD": 300
                },
                {
                    "Port Name": "Port Lisas",
                    "Product Type": "UAN",
                    "Quantity": 3300,
                    "FOB Price per Unit in AUD": 350
                },
                {
                    "Port Name": "Portland",
                    "Product Type": "MOP",
                    "Quantity": 2900,
                    "FOB Price per Unit in AUD": 280
                }
            ]
        },
        {
            "Vessel Name": "TAHO AFRICA",
            "Ports Visited": [
                {
                    "Port Name": "Sitra",
                    "Product Type": "Urea",
                    "Quantity": 4800,
                    "FOB Price per Unit in AUD": 300
                },
                {
                    "Port Name": "Novorossiysk",
                    "Product Type": "UAN",
                    "Quantity": 3200,
                    "FOB Price per Unit in AUD": 350
                },
                {
                    "Port Name": "Portland",
                    "Product Type": "MOP",
                    "Quantity": 2700,
                    "FOB Price per Unit in AUD": 280
                }
            ]
        },
        {
            "Vessel Name": "HMPNGS GILBERT TOROPO",
            "Ports Visited": [
                {
                    "Port Name": "Mesaieed",
                    "Product Type": "Urea",
                    "Quantity": 4600,
                    "FOB Price per Unit in AUD": 300
                },
                {
                    "Port Name": "Sipitang",
                    "Product Type": "UAN",
                    "Quantity": 3300,
                    "FOB Price per Unit in AUD": 350
                },
                {
                    "Port Name": "Ras Al Khair",
                    "Product Type": "MAP",
                    "Quantity": 2900,
                    "FOB Price per Unit in AUD": 280
                }
            ]
        },
        {
            "Vessel Name": "MITERA",
            "Ports Visited": [
                {
                    "Port Name": "Bontang",
                    "Product Type": "Urea",
                    "Quantity": 4800,
                    "FOB Price per Unit in AUD": 300
                },
                {
                    "Port Name": "Novorossiysk",
                    "Product Type": "UAN",
                    "Quantity": 3200,
                    "FOB Price per Unit in AUD": 350
                },
                {
                    "Port Name": "Portland",
                    "Product Type": "MOP",
                    "Quantity": 2700,
                    "FOB Price per Unit in AUD": 280
                }
            ]
        }
    ]
}

def query_ai(query):
    response = openai.ChatCompletion.create(
    engine="team4",
    messages = [{"role":"system","content":"You are an AI assistant that helps people find information."}, {"role": "user", "content": query + " answer this question using the following vessel JSON: " + str(ship_data)}],
    temperature=0.7,
    max_tokens=1000,
    top_p=0.95,
    frequency_penalty=0,
    presence_penalty=0,
    stop=None)

    out = response['choices'][0]['message']['content'].replace("JSON", "database")
    out = out.replace("\n", "<br>")
    return out
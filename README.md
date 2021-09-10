# Synth Relational Data Generator

Using [Synth](https://getsynth.com) to generated relational data for SQL environment testing.


## Setup

Setup and execution

### 1. Get Synth 

Download executable from [here](https://www.getsynth.com/docs/getting_started/installation) and place it into your project folder

### 2. Generate 

execute the generator 

```bash
./synth generate snowflake > exports/data.json
```

## Sample Export

```json
{
  "episode": [
    {
      "enc_idn": 100000000,
      "lob": {
        "id": "21",
        "lob": "FHO",
        "lob_desc": "FIMC Healthy Options",
        "program": "MEDICAID"
      },
      "member_id": 100000
    },
    {
      "enc_idn": 100000001,
      "lob": {
        "id": "12",
        "lob": "MAPD",
        "lob_desc": "MEDICARE PHARMACY PART D",
        "program": "MEDICARE"
      },
      "member_id": 100001
    },
    {
      "enc_idn": 100000002,
      "lob": {
        "id": "21",
        "lob": "FHO",
        "lob_desc": "FIMC Healthy Options",
        "program": "MEDICAID"
      },
      "member_id": 100000
    },
    {
      "enc_idn": 100000003,
      "lob": {
        "id": "3",
        "lob": "CHIP",
        "lob_desc": "WASHINGTON APPLE HEALTH",
        "program": "MEDICAID"
      },
      "member_id": 100001
    },
    {
      "enc_idn": 100000004,
      "lob": {
        "id": "3",
        "lob": "CHIP",
        "lob_desc": "WASHINGTON APPLE HEALTH",
        "program": "MEDICAID"
      },
      "member_id": 100000
    }
  ],
  "member": [
    {
      "address_1": "67581 Krystina Coves",
      "address_2": "Suit. 46",
      "city": "Marlon ton",
      "date_of_death": "1942-01-07",
      "dob": "1989-04-19",
      "email": "eli@example.net",
      "first_name": "Manley",
      "gender": "M",
      "id": 100000,
      "last_name": "Feest",
      "middle_name": "D",
      "phone": "909-076-7027 x33365",
      "state": "CA",
      "zip": "09241"
    },
    {
      "address_1": "159 Karson Stravenue",
      "address_2": null,
      "city": "West Jordyn Nolan land",
      "date_of_death": "1994-06-07",
      "dob": "1909-09-01",
      "email": "minnie@example.com",
      "first_name": "Dustin",
      "gender": "M",
      "id": 100001,
      "last_name": "Kunze",
      "middle_name": "A",
      "phone": "464.922.5864 x23058",
      "state": "AK",
      "zip": "0023"
    }
  ]
}
```
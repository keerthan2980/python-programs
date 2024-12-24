dataset=[  {
    "userId": 1,
    "id": 1,
    "title": "sunt aut fa clear",
    "body": "hello welcome"
  },
  {
    "userId": 1,
    "id": 2,
    "title": "qui est esse",
    "body": "hello welcome"
  }]

def fakedata(**records):
    print(records)

for data in dataset:
    fakedata(**data)
    print(f"These are the titles: {data['title']}")
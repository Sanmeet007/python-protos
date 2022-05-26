from pd_df import DataFrame

data = DataFrame(
    [
        {
            "color": "red",
            "id": 1,
            "data": "Hello wolrdEnim sunt ex cupidatat occaecat eiusmod aute .",
            "uuid": "ghjk3878j321134",
        },
        {
            "id": 2,
            "data": "Ex aute adipisicing esse do excepteur dolore. ",
            "uuid": "eihr8rhre8013nqfwe-9u",
        },
        {
            "id": 3,
            "data": "Elit consectetur nisi esse fugiat anim irure.",
            "uuid": "b08349m320m=-081",
        },
        {
            "id": 4,
            "uuid": "pojetq39n06=24-081",
            "data": "Aute consectetur voluptate sit est anim culpa.",
        },
    ] 
    , ["uuid" , "id" , "data"] , indexed=True)

print(data)

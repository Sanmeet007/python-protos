from pprint import pprint


class _Create_Data(type):
    def __new__(self, class_name, bases, attributes):
        return type(class_name, (), attributes)


class DataFrame(metaclass=_Create_Data):
    data_list: list = []

    def __init__(self, data_list):
        self.data_list = data_list
        self.__add_items()
        self.__uinform_data_list()
        for key in self._item_keys:
            setattr(
                self,
                "_" + key,
                type(key,(),{
                        "__repr__": self._common_repr(key),
                        "__eq__": self._common_eq(key),
                    }),
            )
            setattr(self, key, self.__getattribute__("_" + key)())

    def __getitem__(self, item):
        if isinstance(item, self._dbool):
            count = 0
            current_list = []
            for index, ele in enumerate(item.tuple):
                if ele:
                    current_list.append(self.data_list[index])
                    count += 1
            return None if count == 0 else current_list

        return self.data_list[item]

    def __repr__(self):
        return f"Hello world"

    def _common_repr(self, key):
        def custom_repr(_self):
            return f"This is a common repr for {key}"

        return custom_repr

    def _common_eq(self, key):
        def common_eq(_self, val):
            dbool = self._dbool(self.data_list, key, val)
            return dbool

        return common_eq

    def __add_items(self):
        keys = (list(elem.keys()) for elem in self.data_list)
        final_keys = set({})
        for key in keys:
            for k in key:
                final_keys.add(k)
        self._item_keys = final_keys

    def __uinform_data_list(self):
        for item in self.data_list:
            for x in self._item_keys:
                if item.get(x, False) == False:
                    item[x] = None

    class _dbool:
        def __init__(self, data_list, key, val) -> None:
            self.data_list = data_list
            self.tuple = self._gen_tup(key, val)

        def _gen_tup(self, key, val):
            final_tup = []
            for _, elem in enumerate(self.data_list):
                final_tup.append(elem[key] == val)
            return tuple(final_tup)

        def __repr__(self) -> str:
            print(self.tuple)
            return f"_dtype : DataFrame_dbool"

        def __and__(self, comp_obj):
            final_obj = self._compare(comp_obj, "and")
            return final_obj

        def __or__(self, comp_obj):
            final_obj = self._compare(comp_obj, "or")
            return final_obj

        def _compare(self, dbool_obj, op_type):
            tup = zip(self.tuple, dbool_obj.tuple)
            final_tup = []
            for x, y in tup:
                if op_type == "and":
                    final_tup.append(x == True and y == True)
                elif op_type == "or":
                    final_tup.append(x == True or y == True)
                else:
                    raise Exception("Invalid operation type !")

            self.tuple = tuple(final_tup)
            return self


data = DataFrame(
    [
        {
            "id": 1,
            "data": "Hello wolrdEnim sunt ex cupidatat occaecat eiusmod aute ut officia. Esse esse aliqua aute excepteur ipsum reprehenderit veniam duis magna mollit. Nulla proident nostrud non non anim qui in. Ad anim nisi et dolore dolor minim duis adipisicing nostrud est cupidatat id. Velit ex dolore adipisicing duis labore officia deserunt reprehenderit tempor et dolor. Eiusmod aliqua commodo est et laboris labore mollit.",
            "uuid": "ghjk3878j321134",
            "color": "red",
        },
        {
            "id": 2,
            "data": "Ex aute adipisicing esse do excepteur dolore. Sunt deserunt sint tempor ad magna anim eu esse enim incididunt exercitation ipsum. Excepteur aliqua elit veniam consectetur exercitation eiusmod amet do incididunt cillum aliquip. Eiusmod nulla incididunt quis ex. Adipisicing mollit Lorem sunt aliqua ex voluptate exercitation. Qui ut ex qui et magna ut ad cupidatat cupidatat esse laborum dolore enim. Aliquip eiusmod quis eu ullamco veniam.",
            "uuid": "eihr8rhre8013nqfwe-9u",
        },
        {
            "id": 3,
            "data": "Elit consectetur nisi esse fugiat anim irure. Id et non eu ullamco duis Lorem elit dolor sunt do id veniam. Sit id anim reprehenderit sint irure consectetur anim. Velit deserunt reprehenderit ea officia dolore aliquip sit incididunt culpa. Nostrud magna ut laboris nulla sit enim sunt deserunt eiusmod laboris adipisicing ea excepteur.",
            "uuid": "b08349m320m=-081",
        },
    ]
)


if __name__ == "__main__":
    # I am awesome like a pandas dataframe ^_^
    # equivalent to
    # SELECT * FROM `table` WHERE color = None
    data = DataFrame(
        [
            {
                "id": 1,
                "data": "Hello wolrdEnim sunt ex cupidatat occaecat eiusmod aute ut officia. Esse esse aliqua aute excepteur ipsum reprehenderit veniam duis magna mollit. Nulla proident nostrud non non anim qui in. Ad anim nisi et dolore dolor minim duis adipisicing nostrud est cupidatat id. Velit ex dolore adipisicing duis labore officia deserunt reprehenderit tempor et dolor. Eiusmod aliqua commodo est et laboris labore mollit.",
                "uuid": "ghjk3878j321134",
                "color": "red",
            },
            {
                "id": 2,
                "data": "Ex aute adipisicing esse do excepteur dolore. Sunt deserunt sint tempor ad magna anim eu esse enim incididunt exercitation ipsum. Excepteur aliqua elit veniam consectetur exercitation eiusmod amet do incididunt cillum aliquip. Eiusmod nulla incididunt quis ex. Adipisicing mollit Lorem sunt aliqua ex voluptate exercitation. Qui ut ex qui et magna ut ad cupidatat cupidatat esse laborum dolore enim. Aliquip eiusmod quis eu ullamco veniam.",
                "uuid": "eihr8rhre8013nqfwe-9u",
                "color": "blue",
            },
            {
                "id": 3,
                "data": "Elit consectetur nisi esse fugiat anim irure. Id et non eu ullamco duis Lorem elit dolor sunt do id veniam. Sit id anim reprehenderit sint irure consectetur anim. Velit deserunt reprehenderit ea officia dolore aliquip sit incididunt culpa. Nostrud magna ut laboris nulla sit enim sunt deserunt eiusmod laboris adipisicing ea excepteur.",
                "uuid": "b08349m320m=-081",
            },
        ]
    )

    pprint(data[(data.id == 2) & (data.color == "blue")])

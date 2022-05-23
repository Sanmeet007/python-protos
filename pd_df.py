from pprint import pprint
import prettytable, json


class _Create_Data(type):
    # Class modifier
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
                f"_{key}",
                type(
                    key,
                    (),
                    {
                        "__repr__": self._common_repr(key),
                        "__eq__": self._common_eq(key),
                        "__gt__": self._common_gt(key),
                    },
                ),
            )
            setattr(self, key, self.__getattribute__("_" + key)())

    # Dundder methods
    def __getitem__(self, item):
        if isinstance(item, self._dbool):
            count = 0
            current_list = []
            for index, ele in enumerate(item.tuple):
                if ele:
                    current_list.append(self.data_list[index])
                    count += 1

            x = prettytable.PrettyTable()
            x.field_names = self._item_keys
            for z in current_list:
                z = [*z.values()]
                for i, y in enumerate(z):
                    if len(str(y)) > 18:
                        z[i] = f"{y[:17]}..."
                x.add_row([*z])

            return None if count == 0 else f"{x}"

        return self.data_list[item]

    def __repr__(self):
        x = prettytable.PrettyTable()
        x.field_names = self._item_keys
        for z in self.data_list:
            z = [*z.values()]
            for i, y in enumerate(z):
                if len(str(y)) > 18:
                    z[i] = f"{y[:17]}..."
            x.add_row([*z])

        return f"{x}"

    # Super Private methods
    def __add_items(self):
        """
        Returns all the possible stub heads
        """
        stub_heads = []

        for item in self.data_list:
            for x in item.keys():
                if x not in stub_heads:
                    stub_heads.append(x)

        self._item_keys = stub_heads

    def __uinform_data_list(self):
        """
        Modifies the data_list to make it uniform.
        NOTE : attributes with no values or if they dont exist then None will be assigned by default.

        eg .
            [{
                "id" : "_id",
                "_v" : "value",
            },
            {
                "id" : "_id"
            }]

        Here the sencond dict will be assigned a "_v" attribute with a default of None
        """
        for item in self.data_list:
            for x in self._item_keys:
                if item.get(x, False) == False:
                    item[x] = None

    # Private methods
    def _pr(self):
        pass

    # Run time subclass methods generators
    def _common_repr(self, key):
        """
        Defines the __repr__ for the subclass object generated on the fly or at run time
        """

        def custom_repr(_self):
            x = prettytable.PrettyTable()
            x.field_names = ["index", key]

            for i, z in enumerate(self.data_list):
                for k, v in z.items():
                    if k == key:
                        if len(str(v)) > 18:
                            v = f"{v[:20]}..."
                        x.add_row([i, v])

            return f"{x}\n_dtype : DataFrame_attr({key})"

        return custom_repr

    def _common_eq(self, key):
        """
        Defines the __eq__ for the subclass object generated on the fly or at run time
        """

        def common_eq(_self, val):
            dbool = self._dbool(self.data_list, key, val)
            return dbool

        return common_eq

    def _common_gt(self, key):
        """
        Defines the __gt__ for the subclass object generated on the fly or at run time
        """

        def common_gt(_self):
            pass

        return common_gt

    # Private Subclasses
    class _dbool:
        """
        This class is responisble for logically fetching the data based on the fields or the stub heads (basically the keys of dicts)
        """

        def __init__(self, data_list, key, val) -> None:
            self.data_list = data_list
            self.tuple = self._gen_tup(key, val)

        # Dundder methods
        def __repr__(self) -> str:
            """
            Prints the _dbool object using the prettytable module
            """

            x = prettytable.PrettyTable()
            x.field_names = ["index", "bool"]
            for i, z in enumerate(self.tuple):
                x.add_row([i, z])

            return f"{x}\n_dtype : DataFrame_dbool"

        def __and__(self, comp_obj):
            """
            Overloads the & to give a logical and for _dbool data
            """
            final_obj = self._compare(comp_obj, "and")
            return final_obj

        def __or__(self, comp_obj):
            """
            Overloads the | to give a logical or for _dbool data
            """
            final_obj = self._compare(comp_obj, "or")
            return final_obj

        # Private methods
        def _gen_tup(self, key, val):
            """
            Converts the data_list to tuple which is used for further comparision
            """
            final_tup = []
            for _, elem in enumerate(self.data_list):
                final_tup.append(elem[key] == val)
            return tuple(final_tup)

        def _compare(self, dbool_obj, op_type):
            """
            Used to compare the _dbool objects logically
            """
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


if __name__ == "__main__":
    # I am awesome like a pandas dataframe ^_^

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

    print("Printing the whole data table : ")
    print(data)
    print("\n")

    print("Printing the only id : ")
    print(data.id)
    print("\n")

    print("Printing the or condtion based table : ")
    print(data[(data.id == 3) | (data.color == "blue")])
    print("\n")

    print("Printing the and condtion based table : ")
    print(data[(data.id == 3) & (data.uuid == "b08349m320m=-081")])
    print("\n")

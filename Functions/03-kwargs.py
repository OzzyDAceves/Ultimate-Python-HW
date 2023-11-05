def get_product(**data):
    print(data)


def get_product_2(**data):
    print(data["id"], data["name"])


get_product(id="id",
            name="iphone",
            description="This is an iphone")

get_product_2(id="1341",
              name="Samsung",
              description="This is an iphone")

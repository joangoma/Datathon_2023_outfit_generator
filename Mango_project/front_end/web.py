import subprocess

import streamlit as st

# from ..back_end.selector import *


def user_input():
    st.sidebar.title("Navigation")
    page = st.sidebar.radio("Go to", ["User Description", "Outfit Generator"])
    return page


def user_description():
    st.title("User Description")
    gender = st.selectbox("Select Gender", ["Male", "Female", "Other"])
    age = st.slider("Select Age", 0, 100, 25, 1)
    # Add more attributes as needed

    st.write(f"Gender: {gender}")
    st.write(f"Age: {age}")

    # Store user input in st.session_state
    st.session_state.user_input = {"gender": gender, "age": age}


def outfit_generator():
    st.title("Outfit Description")

    all_clothing_options = [
        "Trousers",
        "Jeans",
        "Dresses",
        "Shirt",
        "Sweater",
        "Skirts",
        "Jewellery",
        "Bags",
        "Glasses",
        "Wallets & cases",
        "Shorts",
        "Tops",
        "Belts and Ties",
        "Jumpsuit",
        "Jackets",
        "Coats",
        "Footwear",
        "Hats, scarves and gloves",
        "T-shirt",
        "Blazers",
        "Gadgets",
        "Swimwear",
        "Vest",
        "Fragances",
        "Cardigans",
        "Trenchcoats",
        "Puffer coats",
        "Outer Vest",
        "Leggings and joggers",
        "Deco Accessories",
        "Poloshirts",
        "Intimate",
        "Sweatshirts",
        "Deco Textiles",
        "Bedding",
        "Bodysuits",
        "Leather jackets",
        "Parkas",
        "Glassware",
    ]

    selected_options = st.multiselect("Select Clothing Options", all_clothing_options)

    choosen_clothes: dict[str, tuple[int, int, int]] = dict()
    for option in selected_options:
        color = st.color_picker(f"Select Color for {option}", key=option)
        color = color.lstrip("#")
        color_rgb = tuple(int(color[i : i + 2], 16) for i in (0, 2, 4))
        choosen_clothes[option] = color_rgb

    if st.button("Generate Outfit"):
        generate_outfit(choosen_clothes)


def generate_outfit(choosen_clothes):
    user_input_data = st.session_state.user_input
    # clothes_id: list[str] | None = selector.get_closest_product()
    clothes_id = ["41085800-02", "53000586-TO", "53030601-81"]
    idsToQuery_path = "../back_end/Query/IdsToQuery.txt"
    idsOutput_path = "../back_end/Query/IdsOutput.txt"
    st.write(choosen_clothes, user_input_data)
    if clothes_id is not None:
        with open(idsToQuery_path, "w") as query_file:
            query_file.truncate()
            print(len(clothes_id), file=query_file)
            for id in clothes_id:
                print(id, file=query_file)

    # fer la crida per buscar els outfits
    # idsOutputPath conte les n i ids dels outfits
    # crida a la funcio de selector que generi les fotos
    # subprocess.run(["bash", ../back_end/Query/Query.sh])
    # les mostrem

    st.write("Generating outfit with the following options:")
    n = 0
    for i in range(n):
        st.image(
            "../dataset/new_outfit/{i}".format(),
            use_column_width=True,
        )


def main():
    page = user_input()

    if page == "User Description":
        user_description()
    elif page == "Outfit Generator":
        outfit_generator()


if __name__ == "__main__":
    main()

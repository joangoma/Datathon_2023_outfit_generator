import streamlit as st

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
    # Display more attributes as needed

def outfit_generator():
    st.title("Outfit Description")
    
    all_clothing_options = [
        'Trousers' 'Jeans' 'Dresses' 'Shirt' 'Sweater' 'Skirts' 'Jewellery'
        'Bags' 'Glasses' 'Wallets & cases' 'Shorts' 'Tops' 'Belts and Ties'
        'Jumpsuit' 'Jackets' 'Coats' 'Footwear' 'Hats, scarves and gloves'
        'T-shirt' 'Blazers' 'Gadgets' 'Swimwear' 'Vest' 'Fragances' 'Cardigans'
        'Trenchcoats' 'Puffer coats' 'Outer Vest' 'Leggings and joggers'
        'Deco Accessories' 'Poloshirts' 'Intimate' 'Sweatshirts' 'Deco Textiles'
        'Bedding' 'Bodysuits' 'Leather jackets' 'Parkas' 'Glassware'
    ]

    selected_options = st.multiselect("Select Clothing Options", all_clothing_options)
    
    clothes: dict[str, tuple[int, int, int]] = dict()
    for option in selected_options:
        color = st.color_picker(f"Select Color for {option}", key=option)
        color = color.lstrip('#')
        color_rgb =  tuple(int(color[i:i+2], 16) for i in (0, 2, 4))
        clothes[option] = color_rgb

    if st.button("Generate Outfit"):
        generate_outfit(selected_options)

def generate_outfit(selected_options):
    st.write("Generating outfit with the following options:")
    for option in selected_options:
        st.write(f"{option}: {st.session_state[option]}")

def main():
    page = user_input()

    if page == "User Description":
        user_description()
    elif page == "Outfit Generator":
        outfit_generator()

if __name__ == "__main__":
    main()

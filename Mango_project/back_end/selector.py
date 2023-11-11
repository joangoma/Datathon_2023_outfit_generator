from PIL import Image
from rembg import new_session, remove
import pandas as pd
import numpy as np
from dataclasses import dataclass

Identifier = str
Link = str

class Selector:
    """
    A class for managing outfits and product data.

    Attributes:
    - _DFoutfit: DataFrame containing outfit data
    - _DFproduct: DataFrame containing product data
    """
    _DFoutfit: pd.DataFrame
    _DFproduct: pd.DataFrame
    
    def __init__(self) -> None:
        """
        Initializes the Selector object by loading outfit and product data from CSV files.
        """
        self._DFoutfit = pd.read_csv('../dataset/outfit_data.csv')
        self._DFproduct = pd.read_csv('../dataset/product_data.csv')
    
    @staticmethod
    def get_pixel_matrix(image):
        """
        Converts an image to a pixel matrix.

        Parameters:
        - image: Image object

        Returns:
        - Pixel matrix
        """
        pixel_data = list(image.getdata())
        width, height = image.size
        pixel_matrix = [pixel_data[i * width:(i + 1) * width] for i in range(height)]
        return pixel_matrix

    def get_all_outfits(self) -> list[str]:
        """
        Gets a list of all unique outfit identifiers.

        Returns:
        - List of outfit identifiers
        """
        return self.DF_outfits()['cod_outfit'].unique()
    
    def get_all_products(self) -> list[str]:
        """
        Gets a list of all unique outfit identifiers.

        Returns:
        - List of outfit identifiers
        """
        return self.DF_products()['cod_modelo_color'].unique()

    def get_outfits_with(self, prod_id: list[Identifier]) -> list[str]:
        """
        Finds outfits that contain specific product identifiers.

        Parameters:
        - prod_id: List of product identifiers

        Returns:
        - List of outfit identifiers
        """
        return self.DF_outfits()[self.DF_outfits()['cod_modelo_color'].isin(prod_id)]['cod_outfit'].to_list()
    
    def outfits_check(self, prod_id: list[Identifier]) -> bool:
        """
        Checks if a set of product identifiers uniquely belongs to an outfit.

        Parameters:
        - prod_id: List of product identifiers

        Returns:
        - True if the set of product identifiers uniquely belongs to an outfit, False otherwise
        """
        return self.DF_outfits()[self.DF_outfits()['cod_modelo_color'].isin(prod_id)]['cod_outfit'].nunique() == 1
    
    def get_outfit_composition(self, outf_id: Identifier) -> list[Identifier]:
        """
        Gets a list of product identifiers that belong to a specific outfit.

        Parameters:
        - outf_id: Outfit identifier

        Returns:
        - List of product identifiers
        """
        return self.DF_outfits()[self.DF_outfits()['cod_outfit'] == outf_id]['cod_modelo_color'].to_list()
    
    def get_product_info(self, prod_id: Identifier) -> dict[str, str]:
        """
        Gets information about a specific product.

        Parameters:
        - prod_id: Product identifier

        Returns:
        - Dictionary containing product information
        """
        return self.DF_products().loc[self.DF_products()['cod_modelo_color'] == prod_id].iloc[0].to_dict()
    
    def get_product_image(self, prod_id: Identifier) -> str:
        """
        Gets the file path of the image associated with a specific product.

        Parameters:
        - prod_id: Product identifier

        Returns:
        - File path of the product image
        """
        filename = self.get_product_info(prod_id)['des_filename']
        return "../dataset/images/" + filename.split("/")[-1]
    
    def show_products(self, list_id: list[Identifier]) -> None:
        """
        Displays the image of a specific product.

        Parameters:
        - prod_id: Product identifier
        """
        jpg_path: str = self.get_product_info(prod_id)['des_filename']
        img = Image.open(jpg_path)
        img.show()
        return
    
    def show_outfit(self, outf_id: Identifier) -> None:
        """
        Displays the images of all products in a specific outfit as a collage.

        Parameters:
        - outf_id: Outfit identifier
        """
        products: list[Identifier] = self.get_outfit(outf_id)
        jpg_paths: list[str] = [self.get_product_image(prod_id) for prod_id in products]
        images: list = [Image.open(path) for path in jpg_paths]

        # Determine the size of the collage
        total_width = sum(img.width for img in images)
        max_height = max(img.height for img in images)

        # Create a new image with white background
        collage = Image.new('RGB', (total_width, max_height), (255, 255, 255))

        # Paste each image into the collage
        current_width = 0
        for img in images:
            collage.paste(img, (current_width, 0))
            current_width += img.width

        # Save the collage
        collage.save("../dataset/outfits/" + str(outf_id) + ".png")

    def get_rgb(self, id):
        """
        Calculates the average RGB values of an image.

        Parameters:
        - id: Product identifier

        Returns:
        - Average RGB values as a NumPy array
        """
        input_path = self.get_product_image(id)
        n = len(input_path)
        no_back_path = input_path[:n-4] + "_nback.png"
        img = None
        try:  
            img = Image.open(no_back_path)
        except FileNotFoundError:
            in_file = Image.open(input_path)
            output = remove(in_file)
            output.save(no_back_path)
            img = output
        
        pixel_matrix = self.get_pixel_matrix(img)
        width,height = img.size
        suma = np.array([0,0,0,0], dtype=float)
        print(pixel_matrix[0][0])
        cnt = 0
        for i in range(height):
            for j in range(width):
                col = np.array(pixel_matrix[i][j])
                if np.all(abs(col) != np.array([0,0,0,0])):
                    suma = suma + col
                    cnt += 1
        print(suma/cnt)
        return suma/cnt

    # ###############################   GETTERS  #######################################
    
    def DF_outfits(self) -> pd.DataFrame:
        """
        Gets the DataFrame containing outfit data.

        Returns:
        - DataFrame with outfit data
        """
        return self._DFoutfit
        
    def DF_products(self) -> pd.DataFrame:
        """
        Gets the DataFrame containing product data.

        Returns:
        - DataFrame with product data
        """
        return self._DFproducts
    
    
selector = Selector()
selector.show_product("51000622-02")
for id in [1, 2086, 4354, 3225, 5358, 6556, 6559, 6941, 3902, 7338, 7339, 6088]:
    print(selector.get_outfit_composition(id))
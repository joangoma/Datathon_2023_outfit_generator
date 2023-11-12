from PIL import Image
import pandas as pd
import numpy as nps
from typing import TypeAlias, Any


color_mapping = { 'OFFWHITE': (255, 255, 255), 'TEJANO OSCURO': (25, 25, 112), 'ROSA PASTEL': (255, 182, 193), 'MOSTAZA': (255, 255, 0), 'ROJO': (255, 0, 0), 'GRIS MEDIO VIGORE': (128, 128, 128), 'CARAMELO': (210, 105, 30), 'KHAKI': (240, 230, 140), 'GRIS OSCURO VIGORE': (40, 40, 40), 'CRUDO': (255, 235, 205), 'FRESA': (255, 0, 128), 'BEIGE': (245, 245, 220), 'CHOCOLATE': (139, 69, 19), 'NEGRO': (0, 0, 0), 'ROSA PALO': (255, 192, 203), 'TEJANO MEDIO': (70, 130, 180), 'AMARILLO': (255, 255, 0), 'BLANCO': (255, 255, 255), 'ARENA': (194, 178, 128), 'MORADO': (128, 0, 128), 'MARRON': (165, 42, 42), 'AZUL': (0, 0, 255), 'AGUA': (0, 255, 255), 'NAVY': (0, 0, 128), 'TEJANO GRIS OSCURO': (169, 169, 169), 'CAMEL': (193, 154, 107), 'VERDE': (0, 128, 0), 'ROSA': (255, 0, 255), 'FUCSIA': (255, 0, 255), 'GRIS CLARO VIGORE': (192, 192, 192), 'CUERO': (139, 69, 19), 'VISON': (184, 134, 11), 'TEJANO CLARO': (135, 206, 250), 'PLATA': (192, 192, 192), 'GRIS': (128, 128, 128), 'NUDE': (255, 222, 173), 'ORO': (255, 215, 0), 'TURQUESA': (64, 224, 208), 'TEJANO NEGRO': (0, 0, 0), 'NARANJA': (255, 165, 0), 'DIRTY': (30, 144, 255), 'HIELO': (176, 224, 230), 'CELESTE': (173, 216, 230), 'BURDEOS': (128, 0, 32), 'AMARILLO FLUOR': (255, 255, 0), 'PIEDRA': (105, 105, 105), 'MALVA': (221, 160, 221), 'ROSA LIGHT': (255, 182, 193), 'MARINO': (0, 0, 128), 'MANDARINA': (255, 165, 0), 'TERRACOTA': (204, 78, 92), 'CALDERO': (139, 69, 19), 'GRANATE': (128, 0, 0), 'TOPO': (135, 125, 115), 'VERDE PASTEL': (152, 251, 152), 'AZUL NOCHE': (25, 25, 112), 'MISTERIO': (112, 138, 144), 'LIMA': (0, 255, 0), 'COFFEE': (165, 42, 42), 'PERLA': (240, 240, 240), 'ESMERALDA': (0, 201, 87), 'OCRE': (204, 119, 34), 'VIOLETA': (238, 130, 238), 'VINO': (128, 0, 0), 'MARFIL': (255, 255, 240), 'BOTELLA': (0, 128, 0), 'ANTRACITA': (51, 51, 51), 'PEACH': (255, 218, 185), 'VAINILLA': (245, 222, 179), 'TABACO': (128, 78, 40), 'ELECTRICO': (125, 249, 255), 'AMARILLO PASTEL': (255, 255, 153), 'PORCELANA': (240, 240, 240), 'TAUPE': (72, 60, 50), 'COBRE': (184, 115, 51), 'CANELA': (210, 105, 30), 'PETROLEO': (0, 128, 128), 'CORAL': (255, 127, 80), 'LILA': (200, 162, 200), 'COGNAC': (143, 89, 34), 'OLIVA': (128, 128, 0), 'MENTA': (152, 255, 152), 'TEJANO GRIS CLARO': (192, 192, 192), 'TEJANO GRIS': (128, 128, 128), 'DIRTY OSCURO': (34, 49, 63), 'BLEACH': (255, 252, 220), 'NARANJA PASTEL': (255, 223, 186), 'CAZA': (139, 69, 19), 'BLOOD': (102, 0, 0), 'CEREZA': (222, 49, 99), 'CENIZA': (192, 192, 192), 'CURRY': (205, 185, 125), 'BLUEBLACK': (0, 0, 139), 'SALMON': (250, 128, 114), 'CHICLE': (255, 182, 193), 'TEJANO SOFT': (112, 128, 144), 'GUNMETAL': (42, 52, 57), 'MANZANA': (50, 205, 50), 'BILLAR': (0, 100, 0), 'MUSGO': (173, 223, 173), 'TINTA': (0, 0, 0), 'INDIGO': (75, 0, 130), 'ROSA FLUOR': (255, 20, 147), 'DIRTY CLARO': (220, 220, 220), 'CIRUELA': (139, 0, 139), 'BERMELLON': (227, 66, 52), 'GERANIO': (201, 0, 22), 'PIMENTON': (153, 0, 0), 'PRUSIA': (0, 49, 83), 'ASFALTO': (47, 79, 79),}
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
        self._DFproduct['RGB'] = self._DFproduct['des_color_specification_esp'].map(color_mapping)
        self._DFproduct.drop(['cod_color_code',	'des_color_specification_esp','des_agrup_color_eng'], axis=1, inplace=True)
        
    @staticmethod
    def euclidean_distance(a: list, b: list) -> float:
        """
        Calculate the Euclidean distance between two vectors.

        Parameters:
        - a: First vector
        - b: Second vector

        Returns:
        - Euclidean distance between the two vectors
        """
        return np.linalg.norm(np.array(a) - np.array(b))
    
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
        for prod_id in list_id:
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
    
    def get_closest_product(self, products: dict[str, list], profile: dict[str, str|int]) -> list[None|str]:
        closest_products: list[None|str] = list()
        threshold = 1.41
        #change age into either adult or child
        profile['age'] = 'Kids' if profile['age'] < 15 else 'Adult'
        
        for product_type, target_rgb in products.items(): #falta dterminar distancia maxima
            filtered_rows: pd.DataFrame = self.DF_products().copy()[
                (self.DF_products()['des_product_family'] == product_type) &
                (self.DF_products()['des_sex'] == profile['gender']) &
                (self.DF_products()['des_age'] == profile['age'])
            ]
            if filtered_rows.empty:
                closest_products.append(None)
            else:
                closest_index = filtered_rows['RGB'].apply(lambda x: self.euclidean_distance(x, target_rgb)).idxmin()
                closest_product_id = filtered_rows.loc[closest_index]['cod_modelo_color']
                closest_products.append(closest_product_id)
                #if self.euclidean_distance(target_rgb, closest_product) <= threshold
        
        return closest_products
    
    def get_possibilitis(self, products: dict[str, list], profile: dict[str, str|int]) -> None:
        selection: list[str|None] = self.get_closest_product(products,profile)
        if None is in selection: print("GET GUTTER")
        else:
            outfit_selection = self.get_outfits_with(selection)
            all_products = [self.get_outfit_composition(id) for id in outfit_selection]
            show

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
        return self._DFproduct
from PIL import Image
from rembg import new_session, remove
import pandas as pd
import numpy as np
from dataclasses import dataclass
import pandas as pd

Identifier = str
Link = str




class Selector:
    _DFoutfit: pd.DataFrame
    _DFproduct: pd.DataFrame
    def __init__(self) -> None:
        self._DFoutfit = pd.read_csv('../dataset/outfit_data.csv')
        self._DFproduct = pd.read_csv('../dataset/product_data.csv')
    
    @staticmethod
    def get_pixel_matrix(image):
        pixel_data = list(image.getdata())
        width, height = image.size
        pixel_matrix = [pixel_data[i * width:(i + 1) * width] for i in range(height)]
        return pixel_matrix

    def get_all_outfits(self) -> list[str]:
        return self.DF_outfits()['cod_outfit'].unique().to_list()

    def outfits_with(self, prod_id: list[Identifier]) -> list[str]:
        return self.DF_outfits() [self.DF_outfits() ['cod_modelo_color'] == prod_id]['cod_outfit'].to_list()
    
    def outfits_check(self, prod_id: list[Identifier]) -> bool:
        return self.DF_outfits() [self.DF_outfits() ['cod_modelo_color'] == prod_id]['cod_outfit'].nunique() == 1
    
    def get_outfit(self, outf_id: Identifier) -> list[Identifier]:
        return self.DF_outfits() [self.DF_outfits() ['cod_outfit'] == outf_id]['cod_modelo_color'].to_list()
    
    def get_product_info(self, prod_id: Identifier) -> dict:
        return self.DF_products().loc[prod_id].to_dict()
    
    def get_product_image(self, prod_id: Identifier) -> dict:
        filename: str = self.get_product_info(prod_id)['des_filename']
        return "../dataset/images/"+filename.split("/")[-1]
    
    def show_product(self, prod_id: Identifier) -> None:
        jpg_path: str = self.get_product_info(prod_id)['des_filename']
        img = Image.open(jpg_path)
        img.show()
        return
    
    def show_outfit(self, outf_id: Identifier) -> None:
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
        collage.save("../dataset/outfits/"+outf_id)

    def get_rgb(self, id):
        input_path = self.get_product_image(id)
        n = len(input_path)
        img = Image.open(no_back_path)
        pixel_matrix = get_pixel_matrix(img)
        width,height = img.size
        suma = np.array([0,0,0,0], dtype=float)
        print(pixel_matrix[0][0])
        cnt = 0
        for i in range(height):
            for j in range(width):
                col = np.array(pixel_matrix[i][j])[:3]
                if np.all(abs(col) != np.array([0,0,0,0])):
                    suma = suma + col
                    cnt += 1
        print(suma/cnt)
        return suma/cnt

    # GETTERS
    
    def DF_outfits(self) -> pd.DataFrame:
        return self._DFoutfit
        
    def DF_products(self) -> pd.DataFrame:
        return self._DFproduct


selector = Selector()
print(selector.get_all_outfits())
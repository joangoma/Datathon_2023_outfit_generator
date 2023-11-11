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
        
    def DF_outfits() -> pd.DataFrame:
        return self._DFoutfit
        
    def DF_products() -> pd.DataFrame:
        return self._DFproducts


class Outfit:
    _identifier: Identifier
    _clothes: list[Identifier]
    
    def __init__(self, identifier: Identifier) -> None:
        self._identifier = identifier
        self._clothes = Selector.get_outfit(identifier)



class Product:    
    _identifier: Identifier
    cod_color_code: str
    des_color_specification_esp: str
    des_agrup_color_eng: str
    des_sex: str
    des_age: str
    des_line: str
    des_fabric: str
    des_product_category: str
    des_product_aggregated_family: str
    des_product_family: str
    des_product_type: str
    des_filename: Link

    
    def __init__(self, identifier: Identifier) -> None:
        self._identifier = identifier
        self._clothes = Selector.get_clothing(identifier)
    

selector = Selector()
print(selector.DF_outfits)
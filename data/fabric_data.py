import pandas as pd

FABRIC_DATA = {
  'Fabric Name': [
    "Wool", "Cashmere", "Cotton", "Linen", "Silk", "Polyester", "Tweed", "Denim", 
    "Rayon", "Satin", "Velvet", "Leather", "Chiffon", "Organza", "Fleece", "Canvas", 
    "Spandex", "Georgette", "Nylon", "Jute", "Corduroy", "Oenim", "Flannel", "Jersey", 
    "Seersucker", "Hemp", "Velveteen", "Crepe", "Alpaca", "Angora", "Mohair", "Camel", 
    "Acetate", "Acrylic", "Fleece", "Sateen", "Chino", "Elastane", "Viscose", "Khadi", 
    "Kalamkari", "Banarasi", "Chikankari", "Sambalpuri", "Ikat", "Chanderi", 
    "Paithani Brocade", "Patola", "Pashmina", "Phulkari", "Bandhni", "Kanjivaram", 
    "Kinnauri", "Jamdani", "Muga", "Kasavu", "Plaid", "Bhagalpuri", "Lepcha", 
    "Kota Doria", "Ajrakh", "Kantha", "Kunbi", "Bagru", "Ilkal", "Mangalgiri", 
    "Sangneri", "Bomkai"
  ],
  'Fabric Type': [
    "Natural Fiber", "Natural Fiber", "Natural Fiber", "Natural Fiber", "Natural Fiber",
    "Synthetic Fiber", "Natural Fiber", "Natural Fiber Blend", "Semi-Synthetic Fiber",
    "Synthetic Fiber", "Natural/Synthetic", "Natural/Synthetic", "Synthetic Fiber",
    "Synthetic Fiber", "Synthetic Fiber", "Natural Fiber Brand", "Synthetic Fiber",
    "Synthetic Fiber", "Synthetic Fiber", "Natural Fiber", "Natural Fiber Blend",
    "Synthetic Fiber Blend", "Natural Fiber", "Synthetic/Natural Blend", "Natural Fiber",
    "Natural Fiber", "Natural/Synthetic", "Synthetic/Natural Blend", "Natural Fiber",
    "Natural Fiber", "Natural Fiber", "Natural Fiber", "Synthetic Fiber", "Synthetic Fiber",
    "Synthetic Fiber", "Synthetic Fiber", "Natural Fiber Blend", "Synthetic Fiber",
    "Semi-Synthetic Fiber", "Natural Fiber", "Natural Fiber", "Natural/Synthetic Blend",
    "Natural Fiber", "Natural Fiber", "Natural Fiber", "Natural Fiber Blend",
    "Natural/Synthetic Blend", "Natural Fiber", "Natural Fiber", "Natural Fiber",
    "Natural Fiber", "Natural Fiber", "Natural Fiber", "Natural Fiber", "Natural Fiber",
    "Natural Fiber", "Natural/Synthetic Blend", "Natural Fiber", "Natural Fiber",
    "Natural Fiber", "Natural Fiber", "Natural Fiber", "Natural Fiber", "Natural Fiber",
    "Natural Fiber", "Natural Fiber", "Natural Fiber", "Natural Fiber"
  ],
  'Durability': [
    "High", "Moderate", "Moderate", "Low", "Low", "High", "High", "High", "Low", "Low",
    "Moderate", "High", "Low", "Low", "High", "High", "High", "Low", "High", "High",
    "High", "High", "Moderate", "Moderate", "High", "High", "Moderate", "Moderate", 
    "High", "Low", "High", "High", "Moderate", "High", "High", "Moderate", "High", 
    "Moderate", "Low to Moderate", "High", "High", "High", "Moderate", "High", "High",
    "High", "High", "High", "High", "Moderate", "Moderate", "High", "High", "High",
    "High", "Moderate", "High", "High", "High", "High", "High", "Moderate", "Moderate",
    "High", "High", "High", "High", "High"
  ],
  'Texture': [
    "Rough", "Soft", "Smooth", "Smooth", "Soft", "Smooth", "Rough", "Rough", "Smooth", "Smooth",
    "Soft", "Smooth", "Soft", "Smooth", "Soft", "Rough", "Smooth", "Smooth", "Smooth", "Rough",
    "Ribbed", "Coarse, Sturdy", "Soft, Brushed", "Stretchy, Smooth", "Crinkled, Textured", "Coarse",
    "Plush, Short Pile", "Crinkled, Rough", "Soft, Silky", "Extremely Soft", "Silky, Shiny", "Smooth",
    "Silky, Glossy", "Soft, Warm", "Plush, Soft", "Glossy, Smooth", "Smooth Twill", "Elastic, Smooth",
    "Soft, Silky", "Rustic, Coarse", "Smooth, Printed", "Soft, Luxurious", "Embroidered, Soft",
    "Handwoven, Textured", "Dyed, Textured", "Lightweight, Sheer", "Luxurious, Woven", "Handwoven, Lustrous",
    "Soft, Warm", "Embroidered, Textured", "Tie-Dyed, Textured", "Heavy, Lustrous", "Coarse, Textured",
    "Fine, Lightweight", "Lustrous, Durable", "Soft, Sheer", "Checkered, Smooth", "Lustrous, Soft",
    "Coarse, Traditional", "Lightweight, Sheer", "Printed, Coarse", "Quilted, Textured", "Coarse, Striped",
    "Hand-Printed, Coarse", "Coarse, Textured", "Fine, Smooth", "Hand-Printed, Soft", "Handwoven, Textured"
  ],
  'Cost': [
    "Moderate", "High", "Low to Moderate", "Moderate", "High", "Low", "Moderate",
    "Low to Moderate", "Low to Moderate", "Moderate", "Moderate to High", "High",
    "Moderate", "Moderate", "Low", "Low", "Low to Moderate", "Moderate", "Low",
    "Low", "Moderate", "Moderate", "Moderate", "Low to Moderate", "Moderate",
    "Low", "Moderate", "Moderate", "High", "High", "High", "High", "Low", "Low",
    "Low", "Moderate", "Moderate", "Low", "Low", "Low", "Moderate", "High",
    "Moderate", "Moderate", "Moderate to High", "High", "High", "High", "High",
    "Moderate", "Moderate", "High", "High", "High", "High", "Moderate", "Moderate",
    "Moderate", "Moderate", "Moderate", "Moderate", "Low to Moderate", "Moderate",
    "Moderate", "Moderate", "Moderate", "Moderate", "Moderate"
  ],
  'Resistance': [
    "High (Durable)", "Moderate", "Moderate", "Low", "Low", "High (Synthetic)",
    "High (Durable)", "High (Durable)", "Moderate", "Low", "Low", "Very High (Durable)",
    "Low", "Low", "High (Synthetic)", "Very High (Durable)", "High (Stretchable)",
    "Low", "Very High (Synthetic)", "High", "Abrasion-Resistant", "Abrasion and Tear-Resistant",
    "Moderate", "Moderate", "High UV-Resistant", "Low to Abrasion", "Moderate",
    "Cold-Resistant", "Low", "High", "Cold-Resistant", "Low", "Heat-Resistant",
    "Cold-Resistant", "Moderate", "High", "Moderate", "Low", "High", "High", "High",
    "Moderate", "High", "Moderate", "Moderate", "High", "Moderate", "High", "Moderate",
    "Moderate", "High", "High", "Moderate", "High", "Moderate", "High", "Moderate",
    "Moderate", "High", "High", "Moderate", "Moderate", "High", "High", "Moderate",
    "Moderate", "Moderate","High"
  ],
  'Color Retention': [
    "Moderate", "Moderate", "Moderate", "Moderate", "High", "High", "Moderate",
    "Moderate", "High", "High", "High", "Low", "High", "High", "Moderate",
    "Moderate", "High", "High", "High", "Low", "High", "Moderate", "Moderate",
    "Moderate", "High", "Moderate", "High", "High", "High", "Moderate", "High",
    "Moderate", "High", "Moderate", "Moderate", "High", "Moderate", "High",
    "Moderate", "High", "High", "High", "High", "High", "High", "High", "High",
    "High", "Moderate", "High", "High", "High", "Moderate", "High", "High",
    "High", "High", "High", "High", "High", "High", "High", "Moderate", "High",
    "High", "High", "High", "High"
  ],
  'Weight': [
    "Medium to Heavy", "Light", "Light to Medium", "Light", "Light", "Medium",
    "Heavy", "Heavy", "Light", "Light", "Medium to Heavy", "Heavy", "Light",
    "Light", "Light", "Heavy", "Light", "Light", "Light", "Heavy", "Heavy",
    "Heavy", "Medium", "Light", "Light", "Medium", "Medium", "Light", "Medium",
    "Light", "Light", "Medium", "Light", "Light", "Light", "Medium", "Medium",
    "Light", "Light", "Medium", "Light", "Medium", "Light", "Medium", "Medium",
    "Light", "Medium", "Medium", "Light", "Medium", "Medium", "Heavy", "Medium",
    "Light", "Medium", "Medium", "Medium", "Medium", "Medium", "Light", "Medium",
    "Medium", "Medium", "Medium", "Medium", "Light", "Light", "Medium"
  ],
  'Combustion': [
    "Combustible", "Combustible", "Combustible", "Combustible", "Combustible",
    "Melts Under Heat", "Combustible", "Combustible", "Combustible", "Combustible",
    "Combustible", "Non-combustible", "Combustible", "Combustible", "Melts Under Heat",
    "Combustible", "Melts Under Heat", "Combustible", "Melts Under Heat", "Combustible",
    "Combustible", "Combustible", "Combustible", "Combustible", "Combustible",
    "Combustible", "Combustible", "Combustible", "Combustible", "Combustible",
    "Combustible", "Combustible", "Highly Combustible", "Highly Combustible",
    "Combustible", "Combustible", "Combustible", "Combustible", "Combustible",
    "Combustible", "Combustible", "Combustible", "Combustible", "Combustible",
    "Combustible", "Combustible", "Combustible", "Combustible", "Combustible",
    "Combustible", "Combustible", "Combustible", "Combustible", "Combustible",
    "Combustible", "Combustible", "Combustible", "Combustible", "Combustible",
    "Combustible", "Combustible", "Combustible", "Combustible", "Combustible",
    "Combustible", "Combustible", "Combustible", "Combustible"
  ],
  'Absorption': [
    "High", "High", "High", "High", "Moderate", "Low", "Moderate", "Moderate",
    "High", "Low", "Low", "Low", "Low", "Low", "Low", "Low", "Low", "Low",
    "Low", "High", "Moderate", "Moderate", "High", "Moderate", "Moderate",
    "High", "Moderate", "Low", "Moderate", "Low", "Low", "Moderate", "Low",
    "Low", "Low", "Moderate", "Moderate", "Low", "High", "High", "High",
    "Moderate", "High", "Moderate", "Moderate", "Moderate", "Moderate", "High",
    "High", "Moderate", "Moderate", "Moderate", "High", "Moderate", "Moderate",
    "Moderate", "Moderate", "Moderate", "Moderate", "High", "Moderate", "High",
    "High", "Moderate", "Moderate", "High", "Moderate", "Moderate"
  ],
  'Sustainable': [
    "Yes", "Yes", "Yes", "Yes", "Yes", "No", "Yes", "Yes", "No", "No", "No",
    "No", "No", "No", "No", "Yes", "No", "No", "No", "Yes", "Yes", "Yes",
    "Yes", "Yes", "Yes", "Highly", "Yes", "Partially", "Yes", "Yes", "Yes",
    "Yes", "No", "No", "Yes", "No", "Yes", "No", "No", "Highly", "Highly",
    "Yes", "Yes", "Yes", "Yes", "Yes", "Yes", "Yes", "Yes", "Yes", "Yes",
    "Yes", "Yes", "Yes", "Yes", "Yes", "Yes", "Yes", "Yes", "Yes", "Yes",
    "Yes", "Yes", "Yes", "Yes", "Yes", "Yes", "Yes"
  ],
  'Wear': [
    "Winter Wear", "Luxury Wear", "Casual", "Ethnic", "Summer Wear", "Formal, Luxury",
    "Casual, Active", "Winter Wear", "Casual Wear", "Formal, Casual", "Formal Wear",
    "Formal, Luxury", "Outerwear", "Formal Wear", "Luxury Wear", "Casual, Active",
    "Outdoor Gear", "Activewear", "Formal Wear", "Activewear", "Ethnic, Durable",
    "Workwear, Casual", "Casual, Durable", "Casual, Winter", "Casual, Sports",
    "Casual, Summer", "Durable", "Formal, Casual", "Formal, Luxury", "Winter Wear",
    "Luxury", "Luxury", "Winter Wear", "Casual", "Winter Wear", "Casual", "Formal",
    "Casual, Workwear", "Sportswear", "Casual, Formal", "Traditional", "Ethnic Wedding",
    "Ethnic, Casual", "Ethnic, Casual", "Ethnic, Casual", "Ethnic, Formal",
    "Ethnic, Wedding", "Ethnic, Wedding", "Winter Wear", "Ethnic, Casual",
    "Ethnic, Casual", "Wedding", "Winter Wear", "Ethnic, Formal", "Ethnic, Formal",
    "Ethnic, Formal", "Casual", "Ethnic, Casual", "Ethnic, Durable", "Ethnic, Summer",
    "Ethnic, Casual", "Ethnic, Durable", "Ethnic, Casual", "Ethnic, Casual",
    "Ethnic, Casual", "Ethnic, Formal", "Ethnic, Casual", "Ethnic, Formal"
  ],
  'geolocation' : [
    "Global Kashmir, Mongolia", "Global Europe, India", "India, China", "Global Scotland", 
    "Global USA", "Global", "Global", "Global", "Global", "Global", "Global", "Global", 
    "Global", "Global", "Global", "Global", "India, Bangladesh", "Global", "Global", 
    "USA, Europe", "Global", "India, USA", "India, China", "Europe, Global", "Global", 
    "Andes (Peru, Bolivia)", "Europe, Asia", "Africa (South Africa)", "Middle East, Asia", 
    "Global", "Global", "USA, Europe", "Europe, India", "Global", "Global", "Global", 
    "India", "India", "Varanasi, India", "Lucknow, India", "Odisha, India", 
    "Andhra Pradesh, India", "Madhya Pradesh, India", "Maharashtra, India", "Gujarat, India", 
    "Kashmir, India", "Punjab, India", "Rajasthan, India", "Tamil Nadu, India", 
    "Himachal Pradesh, India", "Bengal, India", "Assam, India", "Kerala, India", "Global", 
    "Bihar, India", "Sikkim, India", "Rajasthan, India", "Gujarat, India", "Bengal, India", 
    "Goa, India", "Rajasthan, India", "Karnataka, India", "Andhra Pradesh, India", 
    "Rajasthan, India", "Odisha, India","kashimir","Goaa","Bengal"
],

   'market_segment' :[
    "High", "High", "Mid to High", "Mid to High", "High", "Mid", "High", "High", "Mid", 
    "Mid", "High", "High", "Mid", "High", "Mid", "Mid", "Mid", "Mid to High", "Mid", 
    "Mid to High", "Mid to High", "Mid", "Mid", "Mid", "Mid", "High", "High", "High", 
    "High", "High", "High", "High", "Low", "Mid", "Mid", "Mid", "Mid", "Mid", "Mid", 
    "Mid", "High", "High", "High", "High", "High", "High", "High", "High", "Mid to High", 
    "High", "High", "High", "High", "High", "High", "Mid", "Mid to High", "High", "High", 
    "High", "Mid to High", "Mid to High", "High", "High", "High", "High", "High","High"
],

'Best Use' : [
    "Winter coats, sweaters, and suits", "Luxury scarves, sweaters, and coats",
    "Everyday wear, t-shirts, and dresses", "Summer wear, shirts, and tablecloths",
    "Evening gowns, ties, and luxury bedding", "Sportswear, outerwear, and upholstery",
    "Jackets, blazers, and skirts", "Jeans, jackets, and casual wear",
    "Dresses, blouses, and linings", "Evening wear, lingerie, and upholstery",
    "Party dresses, curtains, and upholstery", "Jackets, shoes, and bags",
    "Evening dresses, blouses, and scarves", "Bridal wear, evening gowns, and decor",
    "Blankets, jackets, and winter wear", "Bags, tents, and durable clothing",
    "Activewear, swimwear, and stretch wear", "Dresses, tops, and scarves",
    "Sportswear, hosiery, and umbrellas", "Eco-friendly bags, rugs, and mats",
    "Jackets, Pants, Upholstery", "Denim Wear, Jeans", "Shirts, Blankets",
    "T-Shirts, Dresses", "Summer Wear, Curtains", "Eco-Wear, Bags",
    "Dresses, Upholstery", "Dresses, Scarves", "Sweaters, Scarves",
    "Sweaters, Accessories", "Suits, Upholstery", "Coats, Jackets",
    "Linings, Dresses", "Blankets, Sweaters", "Jackets, Blankets",
    "Dresses, Linings", "Pants, Blazers", "Activewear, Undergarments",
    "Dresses, Blouses", "Ethnic Wear, Home Decor", "Sarees, Home Decor",
    "Bridal Wear", "Kurtas, Sarees, Dupattas", "Sarees, Dupattas",
    "Sarees, Home Decor", "Sarees, Dupattas", "Bridal Sarees",
    "Bridal Sarees, Stoles", "Shawls, Scarves", "Dupattas, Jackets",
    "Sarees, Scarves", "Bridal Sarees", "Shawls, Traditional Wear",
    "Sarees, Dupattas", "Sarees, Traditional Wear", "Sarees, Dupattas",
    "Shirts, Skirts", "Sarees, Blouses", "Shawls, Traditional Wear",
    "Sarees, Dupattas", "Stoles, Sarees", "Blankets, Stoles",
    "Sarees, Daily Wear", "Sarees, Home Decor", "Sarees, Dupattas",
    "Sarees, Shirts", "Sarees, Kurtas", "Sarees, Dupattas"
]



}

fabric_df = pd.DataFrame(FABRIC_DATA)

# Export the DataFrame and constants
FABRIC_DF = fabric_df
FABRIC_TYPES = list(fabric_df['Fabric Type'].unique())
FABRIC_DURABILITY = list(fabric_df['Durability'].unique())
FABRIC_TEXTURES = list(fabric_df['Texture'].unique())
FABRIC_COSTS = list(fabric_df['Cost'].unique())
FABRIC_WEAR = list(fabric_df['Wear'].unique())
FABRIC_SUSTAINABLE = list(fabric_df['Sustainable'].unique())

def get_fabric_types():
    """Return unique fabric types."""
    return FABRIC_TYPES

def get_fabrics_by_type(fabric_type):
    """Return fabrics filtered by type."""
    return fabric_df[fabric_df['Fabric Type'] == fabric_type]

def get_fabrics_by_durability(durability):
    """Return fabrics filtered by durability."""
    return fabric_df[fabric_df['Durability'] == durability]

def get_fabrics_by_wear(wear_type):
    """Return fabrics filtered by wear type."""
    return fabric_df[fabric_df['Wear'].str.contains(wear_type, case=False)]

def get_sustainable_fabrics(sustainable=True):
    """Return sustainable or non-sustainable fabrics."""
    return fabric_df[fabric_df['Sustainable'] == ('Yes' if sustainable else 'No')]

def search_fabrics(query):
    """
    Search fabrics by name, type, wear, or best use.
    Now includes expanded search across more attributes.
    """
    query = query.lower()
    return fabric_df[
        fabric_df['Fabric Name'].str.lower().str.contains(query) |
        fabric_df['Fabric Type'].str.lower().str.contains(query) |
        fabric_df['Wear'].str.lower().str.contains(query) |
        fabric_df['Best Use'].str.lower().str.contains(query) |
        fabric_df['geolocation'].str.lower().str.contains(query)
    ]
def get_fabrics_by_region(region):
    """Return fabrics filtered by geographical region."""
    return fabric_df[fabric_df['Geolocation'].str.contains(region, case=False)]

def get_fabrics_by_cost(cost_level):
    """Return fabrics filtered by cost level."""
    return fabric_df[fabric_df['Cost'].str.contains(cost_level, case=False)]

def get_fabric_details(fabric_name):
    """Return all details for a specific fabric."""
    return fabric_df[fabric_df['Fabric Name'].str.lower() == fabric_name.lower()]

def get_similar_fabrics(fabric_name, criteria=['Fabric Type', 'Durability', 'Texture']):
    """
    Find similar fabrics based on specified criteria.
    Default criteria are fabric type, durability, and texture.
    """
    fabric = get_fabric_details(fabric_name)
    if fabric.empty:
        return pd.DataFrame()
    
    similar = fabric_df
    for criterion in criteria:
        similar = similar[similar[criterion] == fabric[criterion].iloc[0]]
    
    return similar[similar['Fabric Name'] != fabric_name]
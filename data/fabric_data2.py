import pandas as pd

# Sample fabric data
FABRIC_DATA = {
    'Fabric Name': [
        'Wool', 'Cashmere', 'Cotton', 'Linen', 'Silk', 'Polyester', 
        'Tweed', 'Denim', 'Rayon', 'Satin', 'Velvet', 'Leather',
        'Chiffon', 'Organza', 'Fleece', 'Canvas', 'Spandex', 
        'Georgette', 'Nylon', 'Jute'
    ],
    'Fabric Type': [
        'Natural Fiber', 'Natural Fiber', 'Natural Fiber', 'Natural Fiber',
        'Natural Fiber', 'Synthetic Fiber', 'Natural Fiber', 'Natural Fiber Blend',
        'Semi-Synthetic Fiber', 'Synthetic Fiber', 'Natural/Synthetic',
        'Natural/Synthetic', 'Synthetic Fiber', 'Synthetic Fiber',
        'Synthetic Fiber', 'Natural Fiber Blend', 'Synthetic Fiber',
        'Synthetic Fiber', 'Synthetic Fiber', 'Natural Fiber'
    ],
    'Durability': [
        'High', 'Moderate', 'Moderate', 'Low', 'Low', 'High', 'High',
        'High', 'Low', 'Low', 'Moderate', 'High', 'Low', 'Low', 'High',
        'High', 'High', 'Low', 'High', 'High'
    ],
    'Texture': [
        'Rough', 'Soft', 'Smooth', 'Smooth', 'Soft', 'Smooth', 'Rough',
        'Rough', 'Smooth', 'Smooth', 'Soft', 'Smooth', 'Soft', 'Smooth',
        'Soft', 'Rough', 'Smooth', 'Smooth', 'Smooth', 'Rough'
    ],
    'Best Use': [
        'Winter coats, sweaters, and suits',
        'Luxury scarves, sweaters, and coats',
        'Everyday wear, t-shirts, and dresses',
        'Summer wear, shirts, and tablecloths',
        'Evening gowns, ties, and luxury bedding',
        'Sportswear, outerwear, and upholstery',
        'Jackets, blazers, and skirts',
        'Jeans, jackets, and casual wear',
        'Dresses, blouses, and linings',
        'Evening wear, lingerie, and upholstery',
        'Party dresses, curtains, and upholstery',
        'Jackets, shoes, and bags',
        'Evening dresses, blouses, and scarves',
        'Bridal wear, evening gowns, and decor',
        'Blankets, jackets, and winter wear',
        'Bags, tents, and durable clothing',
        'Activewear, swimwear, and stretch wear',
        'Dresses, tops, and scarves',
        'Sportswear, hosiery, and umbrellas',
        'Eco-friendly bags, rugs, and mats'
    ]
}

# Create the DataFrame
fabric_df = pd.DataFrame(FABRIC_DATA)

# Export the DataFrame and fabric types as constants
FABRIC_DF = fabric_df  # For backward compatibility
FABRIC_TYPES = list(fabric_df['Fabric Type'].unique())

def get_fabric_types():
    """Return unique fabric types."""
    return FABRIC_TYPES

def get_fabrics_by_type(fabric_type):
    """Return fabrics filtered by type."""
    return fabric_df[fabric_df['Fabric Type'] == fabric_type]

def get_fabrics_by_durability(durability):
    """Return fabrics filtered by durability."""
    return fabric_df[fabric_df['Durability'] == durability]

def search_fabrics(query):
    """Search fabrics by name, type, or best use."""
    query = query.lower()
    return fabric_df[
        fabric_df['Fabric Name'].str.lower().str.contains(query) |
        fabric_df['Fabric Type'].str.lower().str.contains(query) |
        fabric_df['Best Use'].str.lower().str.contains(query)
    ]
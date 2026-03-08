def  validate_ingredients(ingredients: str) -> str:
    validate = ["fire", "water", "earth", "air"]
    items = ingredients.lower().split()
    invalid = [item for item in items if item not in validate]
    if invalid:
        return f"{ingredients} - INVALID"
    return f"{ingredients} - VALID"

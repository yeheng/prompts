def apply_discount(cents, percent):
    """Return integer cents after a percentage discount; reject invalid inputs."""
    if cents < 0 or percent < 0 or percent > 100:
        raise ValueError("invalid discount")
    return cents * (100 - percent) // 100

def checkout(cents, coupon):
    return apply_discount(cents, coupon.get("percent", 0))

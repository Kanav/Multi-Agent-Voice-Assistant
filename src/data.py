"""
Extended static data: Larger product catalog, more diverse orders, and realistic support policies.

This file expands upon data.py with additional test samples and real-world examples.
"""

from __future__ import annotations

# ── Extended Product Catalog ───────────────────────────
PRODUCT_CATALOG: list[dict] = [
    # Existing categories expanded
    {
        "id": "PROD101",
        "name": "Dell XPS 15 (2024)",
        "category": "Electronics",
        "brand": "Dell",
        "price": 189999,
        "rating": 4.8,
        "features": ["Intel Core Ultra 7", "NVIDIA RTX 4070", "OLED Display", "1TB SSD"],
        "description": "High-performance laptop for creators and professionals.",
        "in_stock": True,
        "colors": ["Platinum Silver", "Graphite"],
    },
    {
        "id": "PROD102",
        "name": "Dyson V15 Detect Vacuum Cleaner",
        "category": "Home Appliances",
        "brand": "Dyson",
        "price": 59900,
        "rating": 4.9,
        "features": ["Laser dust detection", "HEPA filtration", "Cordless", "LCD screen"],
        "description": "Smart cordless vacuum with laser dust detection and powerful suction.",
        "in_stock": True,
        "colors": ["Yellow", "Nickel"],
    },
    {
        "id": "PROD103",
        "name": "Nike Air Zoom Pegasus 41",
        "category": "Footwear",
        "brand": "Nike",
        "price": 11999,
        "rating": 4.6,
        "features": ["Zoom Air units", "Breathable mesh", "Lightweight foam"],
        "description": "Versatile running shoes designed for comfort and performance.",
        "in_stock": True,
        "colors": ["White/Black", "Volt", "Crimson"],
    },
    {
        "id": "PROD104",
        "name": "LG 55-inch OLED evo C4 TV",
        "category": "Electronics",
        "brand": "LG",
        "price": 179999,
        "rating": 4.9,
        "features": ["4K OLED evo panel", "Dolby Vision IQ", "HDMI 2.1", "webOS 24"],
        "description": "Premium OLED TV with stunning visuals and smart features.",
        "in_stock": True,
        "colors": ["Black"],
    },
    {
        "id": "PROD105",
        "name": "KitchenAid Artisan Stand Mixer",
        "category": "Home Appliances",
        "brand": "KitchenAid",
        "price": 49999,
        "rating": 4.8,
        "features": ["10-speed control", "Tilt-head design", "5-quart bowl"],
        "description": "Iconic stand mixer for baking and cooking enthusiasts.",
        "in_stock": True,
        "colors": ["Empire Red", "Matte Black", "Aqua Sky"],
    },
    {
        "id": "PROD106",
        "name": "Apple Watch Ultra 2",
        "category": "Electronics",
        "brand": "Apple",
        "price": 89900,
        "rating": 4.9,
        "features": ["S9 chip", "100m water resistance", "Action button", "Precision dual-frequency GPS"],
        "description": "Rugged smartwatch built for adventure and endurance athletes.",
        "in_stock": True,
        "colors": ["Titanium", "Ocean Band Blue"],
    },
    {
        "id": "PROD107",
        "name": "Asus ROG Strix G16 Gaming Laptop",
        "category": "Electronics",
        "brand": "Asus",
        "price": 149999,
        "rating": 4.7,
        "features": ["Intel i9 14th Gen", "RTX 4080", "165Hz QHD+ display", "RGB keyboard"],
        "description": "High-end gaming laptop with cutting-edge performance.",
        "in_stock": True,
        "colors": ["Eclipse Gray"],
    },
    {
        "id": "PROD108",
        "name": "Sony PlayStation 5 Slim",
        "category": "Gaming",
        "brand": "Sony",
        "price": 54999,
        "rating": 4.9,
        "features": ["825GB SSD", "Ray tracing", "DualSense controller"],
        "description": "Next-gen gaming console with immersive graphics and haptics.",
        "in_stock": True,
        "colors": ["White", "Black"],
    },
]


# ── Extended Order Database ───────────────────────────
ORDER_DATABASE: dict[str, dict] = {
    "ORD201": {
        "product": "Dell XPS 15 (2024)",
        "customer_name": "Ananya Mehta",
        "customer_email": "ananya.mehta@example.com",
        "status": "Delivered",
        "price": 189999,
        "order_date": "2026-03-01",
        "estimated_delivery": "2026-03-05",
    },
    "ORD202": {
        "product": "Dyson V15 Detect Vacuum Cleaner",
        "customer_name": "Rohit Verma",
        "customer_email": "rohit.verma@example.com",
        "status": "Shipped",
        "price": 59900,
        "order_date": "2026-03-03",
        "estimated_delivery": "2026-03-07",
    },
    "ORD203": {
        "product": "Nike Air Zoom Pegasus 41",
        "customer_name": "Sneha Kapoor",
        "customer_email": "sneha.kapoor@example.com",
        "status": "Processing",
        "price": 11999,
        "order_date": "2026-03-04",
        "estimated_delivery": "2026-03-10",
    },
    "ORD204": {
        "product": "LG 55-inch OLED evo C4 TV",
        "customer_name": "Arjun Nair",
        "customer_email": "arjun.nair@example.com",
        "status": "Delayed",
        "delay_reason": "Customs clearance delay",
        "price": 179999,
        "order_date": "2026-03-02",
        "estimated_delivery": "2026-03-12",
    },
    "ORD205": {
        "product": "Apple Watch Ultra 2",
        "customer_name": "Kavya Rao",
        "customer_email": "kavya.rao@example.com",
        "status": "Ordered",
        "price": 89900,
        "order_date": "2026-03-06",
        "estimated_delivery": "2026-03-09",
    },
}


# ── Escalation Queue ───────────────────────────
ESCALATION_QUEUE: list[dict] = []


# ── Support Policies ───────────────────────────
SUPPORT_POLICIES = """
SHIPPING OPTIONS:
- Rocket (Same-day): ₹199, available before 1 PM in metro cities
- Glide (3-4 days): ₹99, express delivery
- Cruise (7-8 days): Free on orders over ₹500

RETURN POLICY:
- 7-day easy returns for unused and undamaged products
- Electronics must be returned with original packaging and accessories
- Refunds processed within 5 business days after inspection

ESCALATION CRITERIA:
- Customer explicitly requests a human agent
- Complaint involves safety, legal, or payment issues
- Customer expresses repeated dissatisfaction
- Issue unresolved after two automated attempts
""".strip()

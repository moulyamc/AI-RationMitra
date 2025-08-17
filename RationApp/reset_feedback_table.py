# reset_commodities.py

from main import app
from extensions import db
from models import Commodity, UserRationOrder  # Import your models

with app.app_context():
    # Optional: Drop the Commodity and UserRationOrder tables (uncomment to use)
    Commodity.__table__.drop(db.engine, checkfirst=True)
    UserRationOrder.__table__.drop(db.engine, checkfirst=True)

    # Recreate all tables (includes Commodity and UserRationOrder)
    db.create_all()

    # Confirm the columns in Commodity and UserRationOrder tables
    print("✅ Commodity table columns:")
    for column in Commodity.__table__.columns:
        print(f"  - {column.name} ({column.type})")

    print("\n✅ UserRationOrder table columns:")
    for column in UserRationOrder.__table__.columns:
        print(f"  - {column.name} ({column.type})")

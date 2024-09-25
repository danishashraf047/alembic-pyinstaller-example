import os
import appdirs
from alembic.config import Config

def get_alembic_config():
    data_dir = appdirs.user_data_dir("alembic-pyinstaller-example", "CodeHills")
    os.makedirs(data_dir, exist_ok=True)
    
    db_path = os.path.join(data_dir, 'my_database.db')
    
    alembic_cfg = Config(os.path.join(os.path.dirname(__file__), '..', 'alembic.ini'))
    
    alembic_cfg.set_main_option('sqlalchemy.url', f'sqlite:///{db_path}')
    
    return alembic_cfg
from alembic import command
from alembic_config import get_alembic_config # For Local
# from src.alembic_config import get_alembic_config # For PyInstaller

def create_migration(message):
    alembic_cfg = get_alembic_config()
    print(alembic_cfg.get_main_option('sqlalchemy.url'))
    command.revision(alembic_cfg, message=message, autogenerate=True)

def run_migrations():
    alembic_cfg = get_alembic_config()
    print(alembic_cfg.get_main_option('sqlalchemy.url'))
    command.upgrade(alembic_cfg, 'head')

if __name__ == "__main__":
    create_migration("Initial Migration")
    run_migrations()
    print("Migrations applied successfully!")
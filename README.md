# Alembic and PyInstaller Example

## Setup

1. **Create a Virtual Environment**:
   ```bash
   python -m venv venv
   ```

2. **Activate the Virtual Environment**:
  * On Windows:
    ```bash
    venv\Scripts\activate
    ```

  *	On macOS/Linux:
    ```bash
    source venv/bin/activate
    ```

3.	**Install Dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

## Running the Application
   ```bash
   python ./src/app.py
   ```

## Making a Build
   ```bash
   pyinstaller app.spec
   ```

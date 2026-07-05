import os
from PIL import Image


class ReceiptScanner:
    """
    Handles receipt validation and image loading.
    OCR support can be added later.
    """

    def __init__(self):
        pass

    # ==========================================
    # Check File Exists
    # ==========================================
    def file_exists(self, file_path):
        return os.path.exists(file_path)

    # ==========================================
    # Load Image
    # ==========================================
    def load_image(self, file_path):

        if not self.file_exists(file_path):
            raise FileNotFoundError("Receipt image not found.")

        return Image.open(file_path)

    # ==========================================
    # Extract Receipt Data (Placeholder)
    # ==========================================
    def extract_receipt_data(self, file_path):

        self.load_image(file_path)

        return {
            "merchant": "",
            "date": "",
            "total_amount": 0,
            "items": []
        }
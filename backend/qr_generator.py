import qrcode
import qrcode.constants
from PIL import Image

class QRGenerator:
    def __init__(self,data: str):
        self.data = data
        self.qr = None
        self.image = None

    def generate_qr_code(self):
        self.qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        self.qr.add_data(self.data)
        self.qr.make(fit=True)
        self.image = self.qr.make_image(fill='black',back_color='white')
    
    def get_qr_image(self) -> Image:
        """
        Returns the qr image generated
        """
        return self.image

    def save_qr(self,filename: str):
        """Saves the QR image into a file"""
        if self.image:
            self.image.save(filename)
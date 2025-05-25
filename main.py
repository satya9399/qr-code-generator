import qrcode
import os

def generate_qr():
    # Step 1: Ask for user input
    user_input = input("Enter the URL or text to generate a QR code: ")
    
    # Step 2: Specify the directory to save the QR code
    save_directory = "qr_codes"  # Folder to save QR codes
    if not os.path.exists(save_directory):
        os.makedirs(save_directory)  # Create the folder if it doesn't exist
    
    # Step 3: Generate the QR code
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(user_input)
    qr.make(fit=True)
    
    # Step 4: Create the QR code image
    qr_img = qr.make_image(fill_color="black", back_color="white")
    
    # Step 5: Define the file name and save location
    file_name = "qr_code.png" if len(user_input) <= 15 else f"qr_code_{hash(user_input)}.png"
    save_path = os.path.join(save_directory, file_name)
    qr_img.save(save_path)
    
    # Step 6: Provide confirmation
    print("Thank you! QR code has been saved at:", save_path)

# Run the function
if __name__ == "__main__":
    generate_qr()

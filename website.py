from flask import Flask, render_template
import qrcode
import bill

def read_amount():
    try:
        with open("amount.txt", "r") as file:
            lines = file.readlines()
            if lines:
                return lines[-1].strip()
            else:
                return "No data in amount.txt"
    except Exception as e:
        return f"Error reading amount.txt: {e}"


def read_status():
    try:
        with open("payment_status.txt", "r") as file:
            lines = file.readlines()
            if lines:
                return lines[-1].strip()
            else:
                return "No data in payment_status.txt"
    except Exception as e:
        return f"Error reading payment_status.txt: {e}"



app = Flask(__name__)

@app.route('/') 
def home():
    amt = read_amount()
    status = read_status()

    if amt == "0":
        value = "zero"
    elif status == "PAID":
        value = "alreadyPaid"
    else: 
        value = "pay"

    return render_template('index.html', value=value, amount=amt)

@app.route('/zero')
def zero():
    return render_template('zero.html')


@app.route('/alreadyPaid')
def alreadyPaid():
    return render_template('alreadypaid.html')

@app.route('/get_data')
def get_data():
    data = {'final_amount': bill.value()}
    return data


@app.route('/pay')
def pay():
    with open("payment_status.txt", "a") as status_file:
        status_file.write("\nPAID")
    return render_template('paid.html')

def generate_qr_code(url, output_path):
    qr = qrcode.QRCode(
        version=3,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(url)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    img.save(output_path)

try:
    if __name__ == "__main__":
        ngrok_url = input("Enter server url: ")  
        qr_code_output_path = "website_qr_code.png"
        generate_qr_code(ngrok_url, qr_code_output_path)

        app.run(host='0.0.0.0', port=8080)

except KeyboardInterrupt: 
    print("Exiting...")